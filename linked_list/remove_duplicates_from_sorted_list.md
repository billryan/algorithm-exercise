# Remove Duplicates from Sorted List

## Source

- leetcode: [Remove Duplicates from Sorted List | LeetCode OJ](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)
- lintcode: [(112) Remove Duplicates from Sorted List](http://www.lintcode.com/en/problem/remove-duplicates-from-sorted-list/)

```
Given a sorted linked list,
delete all duplicates such that each element appear only once.

Example
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
```

## 题解

遍历之，遇到当前节点和下一节点的值相同时，删除下一节点，并将当前节点`next`值指向下一个节点的`next`, 当前节点首先保持不变，直到相邻节点的值不等时才移动到下一节点。

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

### 源码分析

1. 首先进行异常处理，判断head是否为NULL
2. 遍历链表，`node->val == node->next->val`时，保存`node->next`，便于后面释放内存(非C/C++无需手动管理内存)
3. 不相等时移动当前节点至下一节点，注意这个步骤必须包含在`else`中，否则逻辑较为复杂

`while` 循环处也可使用`node != null && node->next != null`, 这样就不用单独判断`head` 是否为空了，但是这样会降低遍历的效率，因为需要判断两处。

### 复杂度分析

遍历链表一次，时间复杂度为 $$O(n)$$, 使用了一个中间变量进行遍历，空间复杂度为 $$O(1)$$.

## Reference

- [Remove Duplicates from Sorted List 参考程序 | 九章](http://www.jiuzhang.com/solutions/remove-duplicates-from-sorted-list/)
