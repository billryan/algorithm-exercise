# Sort List

## Question

- leetcode: [Sort List | LeetCode OJ](https://leetcode.com/problems/sort-list/)
- lintcode: [(98) Sort List](http://www.lintcode.com/en/problem/sort-list/)

```
Sort a linked list in O(n log n) time using constant space complexity.
```

## 题解1 - 归并排序(链表长度求中间节点)

链表的排序操作，对于常用的排序算法，能达到 $$O(n \log n)$$的复杂度有快速排序(平均情况)，归并排序，堆排序。快速排序不一定能保证其时间复杂度一定满足要求，归并排序和堆排序都能满足复杂度的要求。在数组排序中，归并排序通常需要使用 $$O(n)$$ 的额外空间，也有原地归并的实现，代码写起来略微麻烦一点。但是对于链表这种非随机访问数据结构，所谓的「排序」不过是指针`next`值的变化而已，主要通过指针操作，故仅需要常数级别的额外空间，满足题意。堆排序通常需要构建二叉树，在这道题中不太适合。

既然确定使用归并排序，我们就来思考归并排序实现的几个要素。

1. 按长度等分链表，归并虽然不严格要求等分，但是等分能保证线性对数的时间复杂度。由于链表不能随机访问，故可以先对链表进行遍历求得其长度。
2. 合并链表，细节已在 [Merge Two Sorted Lists | Data Structure and Algorithm](http://algorithm.yuanbin.me/zh-hans/linked_list/merge_two_sorted_lists.html) 中详述。

在按长度等分链表时进行「后序归并」——先求得左半部分链表的表头，再求得右半部分链表的表头，最后进行归并操作。

由于递归等分链表的操作需要传入链表长度信息，故需要另建一辅助函数。新鲜出炉的源码如下。

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
     * @param head: The first node of linked list.
     * @return: You should return the head of the sorted linked list,
                    using constant space complexity.
     */
    ListNode *sortList(ListNode *head) {
        if (NULL == head) {
            return NULL;
        }

        // get the length of List
        int len = 0;
        ListNode *node = head;
        while (NULL != node) {
            node = node->next;
            ++len;
        }

        return sortListHelper(head, len);
    }

private:
    ListNode *sortListHelper(ListNode *head, const int length) {
        if ((NULL == head) || (0 >= length)) {
            return head;
        }

        ListNode *midNode = head;

        int count = 1;
        while (count < length / 2) {
            midNode = midNode->next;
            ++count;
        }

        ListNode *rList = sortListHelper(midNode->next, length - length / 2);
        midNode->next = NULL;
        ListNode *lList = sortListHelper(head, length / 2);

        return mergeList(lList, rList);
    }

    ListNode *mergeList(ListNode *l1, ListNode *l2) {
        ListNode *dummy = new ListNode(0);
        ListNode *lastNode = dummy;
        while ((NULL != l1) && (NULL != l2)) {
            if (l1->val < l2->val) {
                lastNode->next = l1;
                l1 = l1->next;
            } else {
                lastNode->next = l2;
                l2 = l2->next;
            }

            lastNode = lastNode->next;
        }

        lastNode->next = (NULL != l1) ? l1 : l2;

        return dummy->next;
    }
};
```

### 源码分析

1. 归并子程序没啥好说的了，见 [Merge Two Sorted Lists | Data Structure and Algorithm](http://algorithm.yuanbin.me/zh-hans/linked_list/merge_two_sorted_lists.html).
2. 在递归处理链表长度时，分析方法和 [Convert Sorted List to Binary Search Tree | Data Structure and Algorithm](http://algorithm.yuanbin.me/zh-hans/binary_search_tree/convert_sorted_list_to_binary_search_tree.html) 一致，**`count`表示遍历到链表中间时表头指针需要移动的节点数。**在纸上分析几个简单例子后即可确定，由于这个题需要的是「左右」而不是二叉搜索树那道题需要三分——「左中右」，故将`count`初始化为1更为方便，左半部分链表长度为`length / 2`, 这两个值的确定最好是先用纸笔分析再视情况取初值，不可死记硬背。
3. 找到中间节点后首先将其作为右半部分链表处理，然后将其`next`值置为`NULL`, 否则归并子程序无法正确求解。这里需要注意的是`midNode`是左半部分的最后一个节点，`midNode->next`才是链表右半部分的起始节点。
4. 递归模型中**左、右、合并**三者的顺序可以根据分治思想确定，即先找出左右链表，最后进行归并(因为归并排序的前提是两个子链表各自有序)。

### 复杂度分析

遍历求得链表长度，时间复杂度为 $$O(n)$$, 「折半取中」过程中总共有 $$\log(n)$$ 层，每层找中点需遍历 $$n/2$$ 个节点，故总的时间复杂度为 $$ n/2 \cdot O(\log n)$$ (折半取中), 每一层归并排序的时间复杂度介于 $$O(n/2)$$ 和 $$O(n)$$之间，故总的时间复杂度为 $$O(n \log n)$$, 空间复杂度为常数级别，满足题意。

## 题解2 - 归并排序(快慢指针求中间节点)

除了遍历链表求得总长外，还可使用看起来较为巧妙的技巧如「快慢指针」，快指针每次走两步，慢指针每次走一步，最后慢指针所指的节点即为中间节点。使用这种特技的关键之处在于如何正确确定快慢指针的起始位置。

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
     * @param head: The first node of linked list.
     * @return: You should return the head of the sorted linked list,
                    using constant space complexity.
     */
    ListNode *sortList(ListNode *head) {
        if (NULL == head || NULL == head->next) {
            return head;
        }

        ListNode *midNode = findMiddle(head);
        ListNode *rList = sortList(midNode->next);
        midNode->next = NULL;
        ListNode *lList = sortList(head);

        return mergeList(lList, rList);
    }

private:
    ListNode *findMiddle(ListNode *head) {
        if (NULL == head || NULL == head->next) {
            return head;
        }

        ListNode *slow = head, *fast = head->next;
        while(NULL != fast && NULL != fast->next) {
            fast = fast->next->next;
            slow = slow->next;
        }

        return slow;
    }

    ListNode *mergeList(ListNode *l1, ListNode *l2) {
        ListNode *dummy = new ListNode(0);
        ListNode *lastNode = dummy;
        while ((NULL != l1) && (NULL != l2)) {
            if (l1->val < l2->val) {
                lastNode->next = l1;
                l1 = l1->next;
            } else {
                lastNode->next = l2;
                l2 = l2->next;
            }

            lastNode = lastNode->next;
        }

        lastNode->next = (NULL != l1) ? l1 : l2;

        return dummy->next;
    }
};
```
###Java
```java
/**
 * Definition for ListNode.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int val) {
 *         this.val = val;
 *         this.next = null;
 *     }
 * }
 */ 
public class Solution {
    /**
     * @param head: The head of linked list.
     * @return: You should return the head of the sorted linked list,
                    using constant space complexity.
     */
    public ListNode sortList(ListNode head) {
        // write your code here
        if (head == null || head.next == null) return head;
        ListNode mid = findMid(head);
        ListNode head1 = head;
        ListNode head2 = mid.next;
        mid.next = null;
        ListNode left = sortList(head1);
        ListNode right = sortList(head2);
        return merge(left, right);
    }
    
    // find mid
    public ListNode findMid(ListNode head) {
        if (head == null) return null;
        ListNode fast = head.next;
        ListNode slow = head;
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }
        return slow;
    }
    
    // merge
    public ListNode merge(ListNode head1, ListNode head2) {
        ListNode dummy = new ListNode(0);
        ListNode head = dummy;
        while (head1 != null || head2 != null) {
            int a = head1 == null ? Integer.MAX_VALUE : head1.val;
            int b = head2 == null ? Integer.MAX_VALUE : head2.val;
            if (a < b) {
                head.next = new ListNode(a);
                if (head1 != null) head1 = head1.next;
            } else {
                head.next = new ListNode(b);
                if (head2 != null) head2 = head2.next;
            }
            head = head.next;
        }
        return dummy.next;
    }
    
}

```

### 源码分析

1. 异常处理不仅考虑了`head`, 还考虑了`head->next`, 可减少辅助程序中的异常处理。
2. 使用快慢指针求中间节点时，将`fast`初始化为`head->next`可有效避免无法分割两个节点如`1->2->null`[^fast_slow_pointer]。
    - 求中点的子程序也可不做异常处理，但前提是主程序`sortList`中对`head->next`做了检测。
3. 最后进行`merge`归并排序。

> **Note** 在递归和迭代程序中，需要尤其注意终止条件的确定，以及循环语句中变量的自增，以防出现死循环或访问空指针。

### 复杂度分析

同上。

## 题解3 - 归并排序(自底向上)

归并排序，总的时间复杂度是（nlogn),但是递归的空间复杂度并不是常数（和递归的层数有着关；递归的过程是自顶向下，好理解；这里提供自底向上的非递归方法；

### C++
```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* sortList(ListNode* head) {
        int len_list = 0;
        ListNode *p=head;
        while(p){
            p = p->next;
            len_list++;
        }
        ListNode *l_list,*r_list,**p_merge_list;
        for(int i = 1; i < len_list; i <<= 1){
            r_list = l_list = head;
            p_merge_list = &head;
            for(int j = 0; j < len_list - i ; j += i << 1){

                for(int k = 0; k < i; ++k) r_list=r_list->next;
                int l_len=i,r_len=min(i, len_list - j - i);

                while(l_len || r_len ){
                    if(r_len > 0 && (l_len == 0 || r_list->val <= l_list->val)){
                        *p_merge_list = r_list;
                        p_merge_list=&(r_list->next);
                        r_list = r_list->next;
                        --r_len;
                    }
                    else{
                        *p_merge_list = l_list;
                        p_merge_list=&(l_list->next);
                        l_list = l_list->next;

                        --l_len;
                    }
                }
                l_list=r_list;
            }
            *p_merge_list = r_list;

        }
        return head;
    }
};
```

### 复杂度分析

归并排序，分解子问题的过程是O(logn),合并子问题的过程是O(n);


## Reference

- [Sort List | 九章算法](http://www.jiuzhang.com/solutions/sort-list/)
- [^fast_slow_pointer]: [LeetCode: Sort List 解题报告 - Yu's Garden - 博客园](http://www.cnblogs.com/yuzhangcmu/p/4131885.html)
