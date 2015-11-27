# Remove Nth Node From End of List

## Source

- lintcode: [(174) Remove Nth Node From End of List](http://www.lintcode.com/en/problem/remove-nth-node-from-end-of-list/)

```
Given a linked list, remove the nth node from the end of list and return its head.

Note
The minimum number of nodes in list is n.

Example
Given linked list: 1->2->3->4->5->null, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5->null.

Challenge
O(n) time
```

## 题解

简单题，
使用快慢指针解决此题，需要注意最后删除的是否为头节点。让快指针先走`n`步，直至快指针走到终点，找到需要删除节点之前的一个节点，改变`node->next`域即可。

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
     * @param n: An integer.
     * @return: The head of linked list.
     */
    ListNode *removeNthFromEnd(ListNode *head, int n) {
        if (NULL == head || n < 0) {
            return NULL;
        }

        ListNode *preN = head;
        ListNode *tail = head;
        // slow fast pointer
        int index = 0;
        while (index < n) {
            if (NULL == tail) {
                return NULL;
            }
            tail = tail->next;
            ++index;
        }

        if (NULL == tail) {
            return head->next;
        }

        while (tail->next) {
            tail = tail->next;
            preN = preN->next;
        }
        preN->next = preN->next->next;

        return head;
    }
};
```

以上代码单独判断了是否需要删除头节点的情况，在遇到头节点不确定的情况下，引入`dummy`节点将会使代码更加优雅，改进的代码如下。

### C++ dummy node

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

### 源码分析

引入`dummy`节点后画个图分析下就能确定`head`和`preDel`的转移关系了。
