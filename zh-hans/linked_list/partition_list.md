# Partition List

## Question

- leetcode: [Partition List | LeetCode OJ](https://leetcode.com/problems/partition-list/)
- lintcode: [(96) Partition List](http://www.lintcode.com/en/problem/partition-list/)


### Problem Statement

Given a linked list and a value _x_, partition it such that all nodes less
than _x_ come before nodes greater than or equal to _x_.

You should preserve the original relative order of the nodes in each of the
two partitions.

For example,  
Given `1->4->3->2->5->2` and _x_ = 3,  
return `1->2->2->4->3->5`.

## 题解

此题出自 *CTCI* 题 2.4，依据题意，是要根据值x对链表进行分割操作，具体是指将所有小于x的节点放到不小于x的节点之前，咋一看和快速排序的分割有些类似，但是这个题的不同之处在于只要求将小于x的节点放到前面，而并不要求对元素进行排序。

这种分割的题使用两路指针即可轻松解决。左边指针指向小于x的节点，右边指针指向不小于x的节点。由于左右头节点不确定，我们可以使用两个dummy节点。

### Python

```python
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of linked list.
    @param x: an integer
    @return: a ListNode
    """
    def partition(self, head, x):
        if head is None:
            return None

        leftDummy = ListNode(0)
        left = leftDummy
        rightDummy = ListNode(0)
        right = rightDummy
        node = head
        while node is not None:
            if node.val < x:
                left.next = node
                left = left.next
            else:
                right.next = node
                right = right.next
            node = node.next
        # post-processing
        right.next = None
        left.next = rightDummy.next

        return leftDummy.next
```

### C++

```c++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        if (head == NULL) return NULL;

        ListNode *leftDummy = new ListNode(0);
        ListNode *left = leftDummy;
        ListNode *rightDummy = new ListNode(0);
        ListNode *right = rightDummy;
        ListNode *node = head;
        while (node != NULL) {
            if (node->val < x) {
                left->next = node;
                left = left->next;
            } else {
                right->next = node;
                right = right->next;
            }
            node = node->next;
        }
        // post-processing
        right->next = NULL;
        left->next = rightDummy->next;

        return leftDummy->next;
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
    public ListNode partition(ListNode head, int x) {
        ListNode leftDummy = new ListNode(0);
        ListNode leftCurr = leftDummy;
        ListNode rightDummy = new ListNode(0);
        ListNode rightCurr = rightDummy;
        
        ListNode runner = head;
        while (runner != null) {
            if (runner.val < x) {
                leftCurr.next = runner;
                leftCurr = leftCurr.next;
            } else {
                rightCurr.next = runner;
                rightCurr = rightCurr.next;
            }
            runner = runner.next;
        }
        
        // cut off ListNode after rightCurr to avoid cylic
        rightCurr.next = null;
        leftCurr.next = rightDummy.next;
        
        return leftDummy.next;
    }
}
```

### 源码分析

1. 异常处理
2. 引入左右两个dummy节点及left和right左右尾指针
3. 遍历原链表
4. 处理右链表，置`right->next`为空(否则如果不为尾节点则会报错，处理链表时 以 null 为判断)，将右链表的头部链接到左链表尾指针的next，返回左链表的头部

### 复杂度分析

遍历链表一次，时间复杂度近似为 $$O(n)$$, 使用了两个 dummy 节点及中间变量，空间复杂度近似为 $$O(1)$$.
