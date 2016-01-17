# Swap Nodes in Pairs

## Question

- leetcode: [Swap Nodes in Pairs | LeetCode OJ](https://leetcode.com/problems/swap-nodes-in-pairs/)
- lintcode: [(451) Swap Nodes in Pairs](http://www.lintcode.com/en/problem/swap-nodes-in-pairs/)

### Problem Statement

Given a linked list, swap every two adjacent nodes and return its head.

#### Example

Given `1->2->3->4`, you should return the list as `2->1->4->3`.

#### Challenge

Your algorithm should use only constant space. You may not modify the values
in the list, only nodes itself can be changed.

## 题解1 - Iteration

直觉上我们能想到的是使用 dummy 处理不定头节点，但是由于这里是交换奇偶位置的链表节点，我们不妨首先使用伪代码来表示。大致可以分为如下几个步骤：

1. 保存`2.next`
2. 将`2.next`赋值为`1`
3. 将`1.next`赋值为1中保存的`2.next`
4. 将前一个链表节点的 next 指向`1`
5. 更新前一个链表节点为`1`
6. 更新当前的链表节点为1中保存的`2.next`

链表类题目看似容易，但要做到 bug-free 其实不容易，建议结合图像辅助分析，onsite 时不要急，把过程先用伪代码写出来。然后将伪代码逐行转化。

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
     * @return a ListNode
     */
    public ListNode swapPairs(ListNode head) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy, curr = head;

        while (curr != null && curr.next != null) {
            ListNode after = curr.next;
            ListNode nextCurr = after.next;
            after.next = curr;
            curr.next = nextCurr;
            // link new node after prev
            prev.next = after;
            // update prev and curr
            prev = curr;
            curr = nextCurr;
        }

        return dummy.next;
    }
}
```

### 源码分析

这里使用 dummy 处理不定头节点，首先将`prev`初始化为`dummy`, 然后按照题解中的几个步骤逐步转化，需要注意的是 while 循环中`curr`和`curr.next`都不能为`null`.

### 复杂度分析

遍历链表一遍，时间复杂度 $$O(1)$$. 使用了若干临时链表节点引用对象，空间复杂度 $$O(1)$$.

## 题解2 - Recursion

在题解1 的分析过程中我们发现比较难处理的是 `prev`和下一个头的连接，要是能直接得到链表后面新的头节点该有多好啊。首先我们可以肯定的是若`head == null || head.next == null`时应直接返回，如果不是则求得交换奇偶节点后的下一个头节点并链接到之前的奇数个节点。这种思想使用递归实现起来非常优雅！

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
     * @return a ListNode
     */
    public ListNode swapPairs(ListNode head) {
        if (head == null || head.next == null) return head;

        ListNode after = head.next;
        head.next = swapPairs(after.next);
        after.next = head;

        return after;
    }
}
```

### 源码分析

这个递归实现非常优雅，需要注意的是递归步的退出条件==>`head == null || head.next == null)`.

### 复杂度分析

每个节点最多被遍历若干次，时间复杂度 $$O(n)$$, 空间复杂度 $$O(1)$$.
