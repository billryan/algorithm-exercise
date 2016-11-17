# Linked List Cycle II

## Question

- leetcode: [Linked List Cycle II | LeetCode OJ](https://leetcode.com/problems/linked-list-cycle-ii/)
- lintcode: [(103) Linked List Cycle II](http://www.lintcode.com/en/problem/linked-list-cycle-ii/)

```
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Example
Given -21->10->4->5, tail connects to node index 1，return node 10

Challenge
Follow up:
Can you solve it without using extra space?
```

## 题解 - 快慢指针

题 [Linked List Cycle | Data Structure and Algorithm](http://algorithm.yuanbin.me/zh-hans/linked_list/linked_list_cycle.html) 的升级版，题目要求不适用额外空间，则必然还是使用快慢指针解决问题。首先设组成环的节点个数为 $$r$$, 链表中节点个数为 $$n$$. 首先我们来分析下在链表有环时都能推出哪些特性：

1. 快慢指针第一次相遇时快指针比慢指针多走整数个环, 这个容易理解，相遇问题。
2. 每次相遇都在同一个节点。第一次相遇至第二次相遇，快指针需要比慢指针多走一个环的节点个数，而快指针比慢指针多走的步数正好是慢指针自身移动的步数，故慢指针恰好走了一圈回到原点。

从以上两个容易得到的特性可知，在仅仅知道第一次相遇时的节点还不够，相遇后如果不改变既有策略则必然找不到环的入口。接下来我们分析下如何从第一次相遇的节点走到环的入口节点。还是让我们先从实际例子出发，以下图为例。

![Linked List Cycle II](../../shared-files/images/linked_list_cycle_ii.png)

`slow`和`fast`节点分别初始化为节点`1`和`2`，假设快慢指针第一次相遇的节点为`0`, 对应于环中的第`i`个节点 $$C_i$$, 那么此时慢指针正好走了 $$n - r - 1 + i$$ 步，快指针则走了 $$2 \cdot (n - r - 1 + i)$$ 步，且存在[^1]: $$n - r - 1 + i + 1= l \cdot r$$. (之所以在`i`后面加1是因为快指针初始化时多走了一步) 快慢指针第一次相遇时慢指针肯定没有走完整个环，且慢指针走的步数即为整数个环节点个数，由性质1和性质2可联合推出。

现在分析下相遇的节点和环的入口节点之间的关联，要从环中第`i`个节点走到环的入口节点，则按照顺时针方向移动[^2]:  $$(l \cdot r - i + 1)$$  个节点 ($$l$$ 为某个非负整数) 即可到达。现在来看看式[^1]和式[^2]间的关系。由式[^1]可以推知 $$n - r = l \cdot r - i$$. 从头节点走到环的入口节点所走的步数可用 $$n - r$$ 表示，故在快慢指针第一次相遇时让另一节点从头节点出发，慢指针仍从当前位置迭代，第二次相遇时的位置即为环的入口节点！

> **Note** 由于此题快指针初始化为头节点的下一个节点，故分析起来稍微麻烦些，且在第一次相遇后需要让慢指针先走一步，否则会出现死循环。

对于该题来说，快慢指针都初始化为头节点会方便很多，故以下代码使用头节点对快慢指针进行初始化。

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
     * @return: The node where the cycle begins.
     *           if there is no cycle, return null
     */
    ListNode *detectCycle(ListNode *head) {
        if (NULL == head || NULL == head->next) {
            return NULL;
        }

        ListNode *slow = head, *fast = head;
        while (NULL != fast && NULL != fast->next) {
            fast = fast->next->next;
            slow = slow->next;
            if (slow == fast) {
                fast = head;
                while (slow != fast) {
                    fast = fast->next;
                    slow = slow->next;
                }
                return slow;
            }
        }

        return NULL;
    }
};
```

###Java
```java
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        if (head == null || head.next == null) {
            return null;
        }
        
        ListNode slow = head;
        ListNode fast = head;
        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                fast = head;
                while (fast != slow) {
                    fast = fast.next;
                    slow = slow.next;
                }
                return fast;
            }
        }
        return null;
    }
}
```

### 源码分析

1. 异常处理。
2. 找第一次相遇的节点。
3. 将`fast`置为头节点，并只走一步，直至快慢指针第二次相遇，返回慢指针所指的节点。

### 复杂度分析

第一次相遇的最坏时间复杂度为 $$O(n)$$, 第二次相遇的最坏时间复杂度为 $$O(n)$$. 故总的时间复杂度近似为 $$O(n)$$, 空间复杂度 $$O(1)$$.

## Reference

- [Linked List Cycle II | 九章算法](http://www.jiuzhang.com/solutions/linked-list-cycle-ii/)
