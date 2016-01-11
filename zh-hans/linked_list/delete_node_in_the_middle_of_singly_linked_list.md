# Delete Node in the Middle of Singly Linked List

## Source

- lintcode: [(372) Delete Node in the Middle of Singly Linked List](http://www.lintcode.com/en/problem/delete-node-in-the-middle-of-singly-linked-list/)

```
Implement an algorithm to delete a nodein the middle of a singly linked list,
given only access to that node.

Example
Given 1->2->3->4, and node 3. return 1->2->4
```

## 题解

根据给定的节点并删除这个节点。弄清楚题意很重要，我首先以为是删除链表的中间节点。:( 一般来说删除单向链表中的一个节点需要首先知道节点的前一个节点，改变其指向的下一个节点并删除就可以了。但是从这道题来看无法知道欲删除节点的前一个节点，那么也就是意味着无法改变前一个节点指向的下一个节点，强行删除当前节点将导致非法内存访问。

既然找不到前一个节点，那么也就意味着不能用通常的方法删除给定节点。从实际角度来看，我们关心的往往并不是真的删除了链表中的某个节点，而是访问链表时表现的行为就像是某个节点被删除了一样。这种另类『删除』方法就是——使用下一个节点的值覆盖当前节点的值，删除下一个节点。

### Java

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
     * @param node: the node in the list should be deleted
     * @return: nothing
     */
    public void deleteNode(ListNode node) {
        if (node == null) return;
        if (node.next == null) node = null;

        node.val = node.next.val;
        node.next = node.next.next;
    }
}
```

### 源码分析

注意好边界条件处理即可。

### 复杂度分析

略。$$O(1)$$.
