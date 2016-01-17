# Remove Linked List Elements

## Question

- leetcode: [Remove Linked List Elements | LeetCode OJ](https://leetcode.com/problems/remove-linked-list-elements/)
- lintcode: [(452) Remove Linked List Elements](http://www.lintcode.com/en/problem/remove-linked-list-elements/)

### Problem Statement

Remove all elements from a linked list of integers that have value `val`.

#### Example

Given `1->2->3->3->4->5->3`, val = 3, you should return the list as
`1->2->4->5`

## 题解

删除链表中指定值，找到其前一个节点即可，将 next 指向下一个节点即可。

### Python

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        while curr.next is not None:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return dummy.next
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
    /**
     * @param head a ListNode
     * @param val an integer
     * @return a ListNode
     */
    public ListNode removeElements(ListNode head, int val) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode curr = dummy;
        while (curr.next != null) {
            if (curr.next.val == val) {
                curr.next = curr.next.next;
            } else {
                curr = curr.next;
            }
        }

        return dummy.next;
    }
}
```

### 源码分析

while 循环中使用`curr.next`较为方便，if 语句中比较时也使用`curr.next.val`也比较简洁，如果使用`curr`会比较难处理。

### 复杂度分析

略
