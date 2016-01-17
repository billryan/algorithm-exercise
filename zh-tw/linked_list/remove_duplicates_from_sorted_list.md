# Remove Duplicates from Sorted List

## Question

- leetcode: [Remove Duplicates from Sorted List | LeetCode OJ](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)
- lintcode: [(112) Remove Duplicates from Sorted List](http://www.lintcode.com/en/problem/remove-duplicates-from-sorted-list/)

```
Given a sorted linked list,
delete all duplicates such that each element appear only once.

Example
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
```

## 題解

遍歷之，遇到當前節點和下一節點的值相同時，刪除下一節點，並將當前節點`next`值指向下一個節點的`next`, 當前節點首先保持不變，直到相鄰節點的值不等時才移動到下一節點。

### Python

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        if head is None:
            return None

        node = head
        while node.next is not None:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next

        return head

```

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
     * @return: head node
     */
    ListNode *deleteDuplicates(ListNode *head) {
        if (head == NULL) {
            return NULL;
        }

        ListNode *node = head;
        while (node->next != NULL) {
            if (node->val == node->next->val) {
                ListNode *temp = node->next;
                node->next = node->next->next;
                delete temp;
            } else {
                node = node->next;
            }
        }

        return head;
    }
};
```

### Java

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null) return null;

        ListNode node = head;
        while (node.next != null) {
            if (node.val == node.next.val) {
                node.next = node.next.next;
            } else {
                node = node.next;
            }
        }

        return head;
    }
}
```

### 源碼分析

1. 首先進行異常處理，判斷head是否為NULL
2. 遍歷鏈表，`node->val == node->next->val`時，保存`node->next`，便於後面釋放記憶體(非C/C++無需手動管理記憶體)
3. 不相等時移動當前節點至下一節點，注意這個步驟必須包含在`else`中，否則邏輯較為複雜

`while` 循環處也可使用`node != null && node->next != null`, 這樣就不用單獨判斷`head` 是否為空了，但是這樣會降低遍歷的效率，因為需要判斷兩處。

### 複雜度分析

遍歷鏈表一次，時間複雜度為 $$O(n)$$, 使用了一個變數進行遍歷，空間複雜度為 $$O(1)$$.

## Reference

- [Remove Duplicates from Sorted List 參考程序 | 九章](http://www.jiuzhang.com/solutions/remove-duplicates-from-sorted-list/)
