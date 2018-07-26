---
difficulty: Easy
tags:
- Linked List
- Two Pointers
title: Remove Nth Node From End of List
---

# Remove Nth Node From End of List

## Problem

### Metadata

- tags: Linked List, Two Pointers
- difficulty: Easy
- source(lintcode): <https://www.lintcode.com/problem/remove-nth-node-from-end-of-list/>
- source(leetcode): <https://leetcode.com/problems/remove-nth-node-from-end-of-list/>

### Description

Given a linked list, remove the n<sup>th</sup> node from the end of list and return its head.


#### Notice

The minimum number of nodes in list is *n*.

#### Example

Given linked list: `1->2->3->4->5->null`, and *n* = `2`.

After removing the second node from the end, the linked list becomes `1->2->3->5->null`.


#### Challenge

Can you do it without getting the length of the linked list?

## 题解

简单题，使用快慢指针解决此题，需要注意最后删除的是否为头节点。让快指针先走`n`步，直至快指针走到终点，找到需要删除节点之前的一个节点，改变`node->next`域即可。见基础数据结构部分的链表解析。

### C++

```cpp
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
     * @param n: An integer.
     * @return: The head of linked list.
     */
    ListNode *removeNthFromEnd(ListNode *head, int n) {
        if (NULL == head || n < 1) {
            return head;
        }

        ListNode dummy(0);
        dummy.next = head;
        ListNode *preDel = dummy;

        for (int i = 0; i != n; ++i) {
            if (NULL == head) {
                return NULL;
            }
            head = head->next;
        }

        while (head) {
            head = head->next;
            preDel = preDel->next;
        }
        preDel->next = preDel->next->next;

        return dummy.next;
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
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if (head == nul) return head;

        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode fast = head;
        ListNode slow = dummy;
        for (int i = 0; i < n; i++) {
            fast = fast.next;
        }

        while(fast != null) {
            fast = fast.next;
            slow = slow.next;
        }

        // gc friendly
        // ListNode toBeDeleted = slow.next;
        slow.next = slow.next.next;
        // toBeDeleted.next = null;
        // toBeDeleted = null;

        return dummy.next;
    }
}
```

### 源码分析

引入`dummy`节点后画个图分析下就能确定`head`和`preDel`的转移关系了。 注意 while 循环中和快慢指针初始化的关系，否则容易在顺序上错一。

### 复杂度分析

极限情况下遍历两遍链表，时间复杂度为 $$O(n)$$.
