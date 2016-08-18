# Merge k Sorted Lists

## Question

- leetcode: [Merge k Sorted Lists | LeetCode OJ](https://leetcode.com/problems/merge-k-sorted-lists/)
- lintcode: [(104) Merge k Sorted Lists](http://www.lintcode.com/en/problem/merge-k-sorted-lists/)

## 题解1 - 选择归并(TLE) <i class="fa fa-thumbs-o-down"></i>

参考 [Merge Two Sorted Lists | Data Structure and Algorithm](http://algorithm.yuanbin.me/zh-hans/linked_list/merge_two_sorted_lists.html) 中对两个有序链表的合并方法，这里我们也可以采用从 k 个链表中选择其中最小值的节点链接到`lastNode->next`(和选择排序思路有点类似)，同时该节点所在的链表表头节点往后递推一个。直至`lastNode`遍历完 k 个链表的所有节点，此时表头节点均为`NULL`, 返回`dummy->next`.

这种方法非常简单直接，但是时间复杂度较高，容易出现 TLE.

### C++

```c++
/**
 * Definition of ListNode
 * class ListNode {
 * public:
 *     int val;
 *     ListNode *next;
 *     ListNode(int val) {
 *         this->val = val;
 *         this->next = NULL;
 *     }
 * }
 */

class Solution {
public:
    /**
     * @param lists: a list of ListNode
     * @return: The head of one sorted list.
     */
    ListNode *mergeKLists(vector<ListNode *> &lists) {
        if (lists.empty()) {
            return NULL;
        }

        ListNode *dummy = new ListNode(INT_MAX);
        ListNode *last = dummy;

        while (true) {
            int count = 0;
	        int index = -1, tempVal = INT_MAX;
            for (int i = 0; i != lists.size(); ++i) {
		        if (NULL == lists[i]) {
		            ++count;
                    if (count == lists.size()) {
                        last->next = NULL;
                        return dummy->next;
                    }
		            continue;
		        }

                // choose the min value in non-NULL ListNode
                if (NULL != lists[i] && lists[i]->val <= tempVal) {
                    tempVal = lists[i]->val;
                    index = i;
                }
            }

	        last->next = lists[index];
	        last = last->next;
	        lists[index] = lists[index]->next;
        }
    }
};
```

### 源码分析

1. 由于头节点不定，我们使用`dummy`节点。
2. 使用`last`表示每次归并后的新链表末尾节点。
3. `count`用于累计链表表头节点为`NULL`的个数，若与 vector 大小相同则代表所有节点均已遍历完。
4. `tempVal`用于保存每次比较 vector 中各链表表头节点中的最小值，`index`保存本轮选择归并过程中最小值对应的链表索引，用于循环结束前递推该链表表头节点。

### 复杂度分析

由于每次`for`循环只能选择出一个最小值，总的时间复杂度最坏情况下为 $$O(k \cdot \sum ^{k}_{i=1}l_i)$$. 空间复杂度近似为 $$O(1)$$.

## 题解2 - 迭代调用`Merge Two Sorted Lists`(TLE) <i class="fa fa-thumbs-o-down"></i>

鉴于题解1时间复杂度较高，题解2中我们可以反复利用时间复杂度相对较低的 [Merge Two Sorted Lists | Data Structure and Algorithm](http://algorithm.yuanbin.me/zh-hans/linked_list/merge_two_sorted_lists.html). 即先合并链表1和2，接着将合并后的新链表再与链表3合并，如此反复直至 vector 内所有链表均已完全合并[^soulmachine]。

### C++

```c++
/**
 * Definition of ListNode
 * class ListNode {
 * public:
 *     int val;
 *     ListNode *next;
 *     ListNode(int val) {
 *         this->val = val;
 *         this->next = NULL;
 *     }
 * }
 */

class Solution {
public:
    /**
     * @param lists: a list of ListNode
     * @return: The head of one sorted list.
     */
    ListNode *mergeKLists(vector<ListNode *> &lists) {
        if (lists.empty()) {
            return NULL;
        }

        ListNode *head = lists[0];
        for (int i = 1; i != lists.size(); ++i) {
            head = merge2Lists(head, lists[i]);
        }

        return head;
    }

private:
    ListNode *merge2Lists(ListNode *left, ListNode *right) {
        ListNode *dummy = new ListNode(0);
        ListNode *last = dummy;

        while (NULL != left && NULL != right) {
            if (left->val < right->val) {
                last->next = left;
                left = left->next;
            } else {
                last->next = right;
                right = right->next;
            }
            last = last->next;
        }

        last->next = (NULL != left) ? left : right;

        return dummy->next;
    }
};
```

### 源码分析

实现合并两个链表的子方法后就没啥难度了，`mergeKLists`中左半部分链表初始化为`lists[0]`, `for`循环后迭代归并`head`和`lists[i]`.

### 复杂度分析

合并两个链表时最差时间复杂度为 $$O(l_1+l_2)$$, 那么在以上的实现中总的时间复杂度可近似认为是 $$l_1 + l_1+l_2 +...+l_1+l_2+...+l_k = O(\sum _{i=1} ^{k} (k-i) \cdot l_i)$$. 比起题解1复杂度是要小一点，但量级上仍然差不太多。实际运行时间也证明了这一点，题解2的运行时间差不多时题解1的一半。那么还有没有进一步降低时间复杂度的可能呢？当然是有的，且看下题分解...

## 题解3 - 二分调用`Merge Two Sorted Lists`

题解2中`merge2Lists`优化空间不大，那咱们就来看看`mergeKLists`中的`for`循环，仔细观察可得知第`i`个链表 $$l_i$$ 被遍历了 $$k-i$$ 次，如果我们使用二分法对其进行归并呢？从中间索引处进行二分归并后，每个链表参与合并的次数变为 $$\log k$$, 故总的时间复杂度可降至 $$\log k \cdot \sum _{i=1} ^{k} l_i$$. 优化幅度较大。

### C++

```c++
/**
 * Definition of ListNode
 * class ListNode {
 * public:
 *     int val;
 *     ListNode *next;
 *     ListNode(int val) {
 *         this->val = val;
 *         this->next = NULL;
 *     }
 * }
 */

class Solution {
public:
    /**
     * @param lists: a list of ListNode
     * @return: The head of one sorted list.
     */
    ListNode *mergeKLists(vector<ListNode *> &lists) {
        if (lists.empty()) {
            return NULL;
        }

        return helper(lists, 0, lists.size() - 1);
    }

private:
    ListNode *helper(vector<ListNode *> &lists, int start, int end) {
        if (start == end) {
            return lists[start];
        } else if (start + 1 == end) {
            return merge2Lists(lists[start], lists[end]);
        }

        ListNode *left = helper(lists, start, start + (end - start) / 2);
        ListNode *right = helper(lists, start + (end - start) / 2 + 1, end);

        return merge2Lists(left, right);
    }

    ListNode *merge2Lists(ListNode *left, ListNode *right) {
        ListNode *dummy = new ListNode(0);
        ListNode *last = dummy;

        while (NULL != left && NULL != right) {
            if (left->val < right->val) {
                last->next = left;
                left = left->next;
            } else {
                last->next = right;
                right = right->next;
            }
            last = last->next;
        }
        last->next = (NULL != left) ? left : right;

        return dummy->next;
    }
};
```

### 源码分析

由于需要建立二分递归模型，另建一私有方法`helper`引入起止位置较为方便。下面着重分析`helper`。

1. 分两种边界条件处理，分别是`start == end`和`start + 1 == end`. 虽然第二种边界条件可以略去，但是加上会节省递归调用的栈空间。
2. 使用分治思想理解`helper`, `left`和`right`的边界处理建议先分析几个简单例子，做到不重不漏。
3. 注意`merge2Lists`中传入的参数，为`lists[start]`而不是`start`...

在`mergeKLists`中调用`helper`时传入的`end`参数为`lists.size() - 1`，而不是`lists.size()`.

### 复杂度分析

题解中已分析过，最坏的时间复杂度为 $$\log k \cdot \sum _{i=1} ^{k} l_i$$, 空间复杂度近似为 $$O(1)$$.

优化后的运行时间显著减少！由题解2中的500+ms 减至40ms 以内。

## Reference

- [^soulmachine]: [soulmachine的LeetCode 题解](http://7xojrx.com1.z0.glb.clouddn.com/docs/algorithm-exercise/docs/leetcode-cpp.pdf)
