# Merge Two Sorted Lists

## Question

- lintcode: [(165) Merge Two Sorted Lists](http://www.lintcode.com/en/problem/merge-two-sorted-lists/)
- leetcode: [Merge Two Sorted Lists | LeetCode OJ](https://leetcode.com/problems/merge-two-sorted-lists/)

```
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.

Example
Given 1->3->8->11->15->null, 2->null , return 1->2->3->8->11->15->null
```

## 題解

此題為兩個鏈表的合併，合併後的表頭節點不一定，故應聯想到使用`dummy`節點。鏈表節點的插入主要涉及節點`next`指標值的改變，兩個鏈表的合併操作則涉及到兩個節點的`next`值變化，若每次合併一個節點都要改變兩個節點`next`的值且要對`NULL`指標做異常處理，勢必會異常麻煩。嗯，第一次做這題時我就是這麼想的... 下面看看相對較好的思路。

首先`dummy`節點還是必須要用到，除了`dummy`節點外還引入一個`lastNode`節點充當下一次合併時的頭節點。在`l1`或者`l2`的某一個節點為空指標`NULL`時，退出`while`循環，並將非空鏈表的頭部鏈接到`lastNode->next`中。

### C++

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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
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

        // do not forget this line!
        lastNode->next =  (NULL != l1) ? l1 : l2;

        return dummy->next;
    }
};
```

### 源碼分析

1. 異常處理，包含在`dummy->next`中。
2. 引入`dummy`和`lastNode`節點，此時`lastNode`指向的節點為`dummy`
3. 對非空l1,l2循環處理，將l1/l2的較小者鏈接到`lastNode->next`，往後遞推`lastNode`
4. 最後處理l1/l2中某一鏈表為空退出while循環，將非空鏈表頭鏈接到`lastNode->next`
5. 返回`dummy->next`，即最終的首指標

注意`lastNode`的遞推並不影響`dummy->next`的值，因為`lastNode`和`dummy`是兩個不同的指標變量。

> **Note** 鏈表的合併為常用操作，務必非常熟練，以上的模板非常精煉，有兩個地方需要記牢。1. 循環結束條件中為條件與操作；2. 最後處理`lastNode->next`指標的值。

### 複雜度分析

最好情況下，一個鏈表為空，時間複雜度為 $$O(1)$$. 最壞情況下，`lastNode`遍曆兩個鏈表中的每一個節點，時間複雜度為 $$O(l1+l2)$$. 空間複雜度近似為 $$O(1)$$.


## Reference

- [Merge Two Sorted Lists | 九章算法](http://www.jiuzhang.com/solutions/merge-two-sorted-lists/)
