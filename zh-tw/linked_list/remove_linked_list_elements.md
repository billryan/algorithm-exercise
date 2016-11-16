# Remove Linked List Elements

## Question

- leetcode: [Remove Linked List Elements | LeetCode OJ](https://leetcode.com/problems/remove-linked-list-elements/)
- lintcode: [(452) Remove Linked List Elements](http://www.lintcode.com/en/problem/remove-linked-list-elements/)

### Problem Statement

Remove all elements from a linked list of integers that have value `val`.

#### Example

Given `1->2->3->3->4->5->3`, val = 3, you should return the list as
`1->2->4->5`

## 題解

刪除鏈表中指定值，找到其前一個節點即可，將 next 指向下一個節點即可。

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

### 源碼分析

while 循環中使用`curr.next`較爲方便，if 語句中比較時也使用`curr.next.val`也比較簡潔，如果使用`curr`會比較難處理。

### 複雜度分析

略
