# Two Lists Sum <i class="fa fa-star"></i><i class="fa fa-star"></i><i class="，"></i>

## Question

- LeetCode - [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)
- LintCode - [(167) Two Lists Sum](http://www.lintcode.en/problem/add-two-numbers/)

```
You have two numbers represented by a linked list, where each node contains a single digit.
The digits are stored in reverse order, such that the 1』s digit is at the head of the list.
Write a function that adds the two numbers and returns the sum as a linked list.

Example
Given two lists, 3->1->5->null and 5->9->2->null, return 8->0->8->null
```

## 題解1

一道看似簡單的進位加法題，實則殺機重重，不信你不看答案自己先做做看。

首先由十進制加法可知應該注意進位的處理，但是這道題僅注意到這點就夠了嗎？還不夠！因為兩個鏈表長度有可能不等長！因此這道題的亮點在於邊界和異常條件的處理，來瞅瞅我([@billryan](https://github.com/billryan))自認為相對優雅的實現。

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

### 源碼分析

1. 迭代能正常進行的條件為`(NULL != l1) || (NULL != l2) || (0 != carry)`, 缺一不可。
2. 對於空指針節點的處理可以用相對優雅的方式處理 - `int l1_val = (NULL == l1) ? 0 : l1->val;`
3. 生成新節點時需要先判斷迭代終止條件 - `(NULL == l1) && (NULL == l2) && (0 == carry)`, 避免多生成一位數0。

## 題解2 - Dummy node

鏈表為空一向是不好處理的邊界條件，如果允許使用少量的額外空間，一個常用的技巧是加上一個dummy node，方便我們對回傳值的頭節點操作。程式碼引用了喜刷刷的解法。

### C++
```c++
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *dummy = new ListNode(0), *p = dummy;
        int carry = 0;
        while(l1 or l2 or carry) {
            if(l1) {
                carry += l1->val;
                l1 = l1->next;
            }
            if(l2) {
                carry += l2->val;
                l2 = l2->next;
            }
            p->next = new ListNode(carry%10);
            carry /= 10;
            p = p->next;
        }
        return dummy->next;
    }
};
```



### 複雜度分析

沒啥好分析的，時間和空間複雜度均為 $$O(max(L1, L2))$$.

### C++ - Recursion

除了使用迭代，對於鏈表類問題也比較適合使用遞歸實現。

To-be done.

## Reference

- *CC150 Chapter 9.2* 題2.5，中文版 p123
- [Add two numbers represented by linked lists | Set 1 - GeeksforGeeks](http://www.geeksforgeeks.org/add-two-numbers-represented-by-linked-lists/)
- [喜刷刷](http://bangbingsyb.blogspot.de/2014/11/leetcode-add-two-numbers.html)
