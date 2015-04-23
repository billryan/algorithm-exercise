# Two Lists Sum <i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star-half-o"></i>

## Source


- CC150 - [(167) Two Lists Sum](http://www.lintcode.com/en/problem/two-lists-sum/)

```
You have two numbers represented by a linked list, where each node contains a single digit.
The digits are stored in reverse order, such that the 1’s digit is at the head of the list.
Write a function that adds the two numbers and returns the sum as a linked list.

Example
Given two lists, 3->1->5->null and 5->9->2->null, return 8->0->8->null
```

## 题解

一道看似简单的进位加法题，实则杀机重重，不信你不看答案自己先做做看。

首先由十进制加法可知应该注意进位的处理，但是这道题仅注意到这点就够了吗？还不够！因为两个链表长度有可能不等长！因此这道题的亮点在于边界和异常条件的处理，来瞅瞅我自认为相对优雅的实现。

### C++ - Iteration

```c++
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
    /**
     * @param l1: the first list
     * @param l2: the second list
     * @return: the sum list of l1 and l2
     */
    ListNode *addLists(ListNode *l1, ListNode *l2) {
        if (NULL == l1 && NULL == l2) {
            return NULL;
        }

        ListNode *sumlist = new ListNode(0);
        ListNode *templist = sumlist;

        int carry = 0;
        while ((NULL != l1) || (NULL != l2) || (0 != carry)) {
            // padding for NULL
            int l1_val = (NULL == l1) ? 0 : l1->val;
            int l2_val = (NULL == l2) ? 0 : l2->val;

            templist->val = (carry + l1_val + l2_val) % 10;
            carry = (carry + l1_val + l2_val) / 10;

            if (NULL != l1) l1 = l1->next;
            if (NULL != l2) l2 = l2->next;

            // return sumlist before generating new ListNode
            if ((NULL == l1) && (NULL == l2) && (0 == carry)) {
                return sumlist;
            }
            templist->next = new ListNode(0);
            templist = templist->next;
        }

        return sumlist;
    }
};
```

### 源码分析

1. 迭代能正常进行的条件为`(NULL != l1) || (NULL != l2) || (0 != carry)`, 缺一不可。
2. 对于空指针节点的处理可以用相对优雅的方式处理 - `int l1_val = (NULL == l1) ? 0 : l1->val;`
3. 生成新节点时需要先判断迭代终止条件 - `(NULL == l1) && (NULL == l2) && (0 == carry)`, 避免多生成一位数0。

### 复杂度分析

没啥好分析的，时间和空间复杂度均为 $$O(max(L1, L2))$$.

### C++ - Recursion

除了使用迭代，对于链表类问题也比较适合使用递归实现。

To-be done.

## Reference

- *CC150 Chapter 9.2* 题2.5，中文版 p123
- [Add two numbers represented by linked lists | Set 1 - GeeksforGeeks](http://www.geeksforgeeks.org/add-two-numbers-represented-by-linked-lists/)
