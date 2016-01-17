# Rotate List

## Question

- leetcode: [Rotate List | LeetCode OJ](https://leetcode.com/problems/rotate-list/)
- lintcode: [(170) Rotate List](http://www.lintcode.com/en/problem/rotate-list/)

### Problem Statement

Given a list, rotate the list to the right by _k_ places, where _k_ is non-
negative.

#### Example

Given `1->2->3->4->5` and k = `2`, return `4->5->1->2->3`.

## 题解

旋转链表，链表类问题通常需要找到需要处理节点处的前一个节点。因此我们只需要找到旋转节点和最后一个节点即可。需要注意的细节是 k 有可能比链表长度还要大，此时需要取模，另一个 corner case 则是链表长度和 k 等长。

### Java

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    /**
     * @param head: the List
     * @param k: rotate to the right k places
     * @return: the list after rotation
     */
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null) return head;
        ListNode fast = head, slow = head;
        int len = 1;
        for (len = 1; fast.next != null && len <= k; len++) {
            fast = fast.next;
        }
        // k mod len if k > len
        if (len <= k) {
            k = k % len;
            fast = head;
            for (int i = 0; i < k; i++) {
                fast = fast.next;
            }
        }
        // forward slow and fast
        while (fast.next != null) {
            fast = fast.next;
            slow = slow.next;
        }
        // return new head
        fast.next = head;
        head = slow.next;
        slow.next = null;
        
        return head;
    }
}
```

### 源码分析

由于需要处理的是节点的前一个节点，故最终的`while` 循环使用`fast.next != null`. k 与链表等长时包含在`len <= k`中。

### 复杂度分析

时间复杂度 $$O(n)$$, 空间复杂度 $$O(1)$$.
