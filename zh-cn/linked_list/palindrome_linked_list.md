# Palindrome Linked List

## Source

- leetcode: [Palindrome Linked List | LeetCode OJ](https://leetcode.com/problems/palindrome-linked-list/)
- lintcode: [Palindrome Linked List](http://www.lintcode.com/en/problem/palindrome-linked-list/)
- [Function to check if a singly linked list is palindrome - GeeksforGeeks](http://www.geeksforgeeks.org/function-to-check-if-a-singly-linked-list-is-palindrome/)

### Problem

Implement a function to check if a linked list is a palindrome.

#### Example

Given `1->2->1`, return true

#### Challenge

Could you do it in O(n) time and O(1) space?


## 题解1 - 使用辅助栈

根据栈的特性(FILO)，可以首先遍历链表并入栈(最后访问栈时则反过来了)，随后再次遍历链表并比较当前节点和栈顶元素，若比较结果完全相同则为回文。 又根据回文的特性，实际上还可以只遍历链表前半部分节点，再用栈中的元素和后半部分元素进行比较，分链表节点个数为奇数或者偶数考虑即可。由于链表长度未知，因此可以考虑使用快慢指针求得。

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
     * @return a boolean
     */
    public boolean isPalindrome(ListNode head) {
        if (head == null || head.next == null) return true;

        Deque<Integer> stack = new ArrayDeque<Integer>();
        // find middle
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            stack.push(slow.val);
            slow = slow.next;
            fast = fast.next.next;
        }

        // skip mid node if the number of ListNode is odd
        if (fast != null) slow = slow.next;

        ListNode rCurr = slow;
        while (rCurr != null) {
            if (rCurr.val != stack.pop()) return false;
            rCurr = rCurr.next;
        }

        return true;
    }
}
```

### 源码分析

注意区分好链表中个数为奇数还是偶数就好了，举几个简单例子辅助分析。

### 复杂度分析

使用了栈作为辅助空间，空间复杂度为 $$O(\frac{1}{2}n)$$, 分别遍历链表的前半部分和后半部分，时间复杂度为 $$O(n)$$.

## 题解2 - 原地翻转

题解 1 的解法使用了辅助空间，在可以改变原来的链表的基础上，可使用原地翻转，思路为翻转前半部分，然后迭代比较。具体可分为以下四个步骤。

1. 找中点。
2. 翻转链表的后半部分。
3. 逐个比较前后部分节点值。
4. 链表复原，翻转后半部分链表。

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
     * @return a boolean
     */
    public boolean isPalindrome(ListNode head) {
        if (head == null || head.next == null) return true;

        // find middle
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        // skip mid node if the number of ListNode is odd
        if (fast != null) slow = slow.next;

        // reverse right part of List
        ListNode rHead = reverse(slow);
        ListNode lCurr = head, rCurr = rHead;
        while (rCurr != null) {
            if (rCurr.val != lCurr.val) {
                reverse(rHead);
                return false;
            }
            lCurr = lCurr.next;
            rCurr = rCurr.next;
        }
        // recover right part of List
        reverse(rHead);

        return true;
    }

    private ListNode reverse(ListNode head) {
        ListNode prev = null;
        while (head != null) {
            ListNode after = head.next;
            head.next = prev;
            prev = head;
            head = after;
        }

        return prev;
    }
}
```

### 源码分析

连续翻转两次右半部分链表即可复原原链表，将一些功能模块如翻转等尽量模块化。

### 复杂度分析

遍历链表若干次，时间复杂度近似为 $$O(n)$$, 使用了几个临时遍历，空间复杂度为 $$O(1)$$.

## 题解3 - 递归(TLE)

递归需要两个重要条件，递归步的建立和递归终止条件。对于回文比较，理所当然应该递归比较第 i 个节点和第 n-i 个节点，那么问题来了，如何构建这个递归步？大致可以猜想出来递归的传入参数应该包含两个节点，用以指代第 i 个节点和第 n-i 个节点。返回参数应该包含布尔值(用以提前返回不是回文的情况)和左半部分节点的下一个节点(用以和右半部分的节点进行比较)。由于需要返回两个值，在 Java 中需要使用自定义类进行封装，C/C++ 中则可以使用指针改变在**递归调用后**进行比较时节点的值。

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

class Result {
    ListNode lNode;
    boolean isP;
    Result(ListNode node, boolean isP) {
        this.lNode = node;
        this.isP = isP;
    }
}

public class Solution {
    /**
     * @param head a ListNode
     * @return a boolean
     */
    public boolean isPalindrome(ListNode head) {
        Result result = new Result(head, true);
        helper(head, head, result);

        return result.isP;
    }

    private void helper(ListNode left, ListNode right, Result result) {
        if (right != null) {
            helper(left, right.next, result);
            boolean equal = (result.lNode.val == right.val);
            result.isP = equal && result.isP;
            result.lNode = result.lNode.next;
        }
    }
}
```

### 源码分析

核心代码为如何在递归中推进左半部分节点而对右半部分使用栈的方式逆向获取节点。左半部分的推进需要借助辅助数据结构`Result`.

### 复杂度分析

递归调用 n 层，时间复杂度近似为 $$O(n)$$, 使用了几个临时变量，空间复杂度为 $$O(1)$$.

## Reference

- [Function to check if a singly linked list is palindrome - GeeksforGeeks](http://www.geeksforgeeks.org/function-to-check-if-a-singly-linked-list-is-palindrome/)
- [回文判断 | The-Art-Of-Programming-By-July/01.04.md](https://github.com/julycoding/The-Art-Of-Programming-By-July/blob/master/ebook/zh/01.04.md)
- [ctci/QuestionB.java at master · gaylemcd/ctci](https://github.com/gaylemcd/ctci/blob/master/java/Chapter%202/Question2_7/QuestionB.java)
