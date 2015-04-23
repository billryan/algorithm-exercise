# Remove Duplicates from Sorted List


## Source

- lintcode: [(112) Remove Duplicates from Sorted List](http://www.lintcode.com/en/problem/remove-duplicates-from-sorted-list/)


```
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
```

### 题解

遍历之，遇到当前节点和下一节点的值相同时，删除下一节点，改变当前节点next的指针值。

#### C++

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
     * @return: head node
     */
    ListNode *deleteDuplicates(ListNode *head) {
        if (head == NULL) {
            return NULL;
        }

        ListNode *node = head;
        while (node->next) {
            if (node->val == node->next->val) {
                ListNode *temp = node->next;
                node->next = node->next->next;
                delete temp;
            } else {
                node = node->next;
            }
        }

        return head;
    }
};
```

#### 源码分析

1. 首先进行异常处理，判断head是否为NULL
2. 遍历链表，`node->val == node->next->val`时，保存`node->next`，便于后面进行delete
3. 不相等时往后指针往后遍历。

#### Java

```java
/**
 * http://www.jiuzhang.com/solutions/remove-duplicates-from-sorted-list/
 */

public class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null) {
            return null;
        }

        ListNode node = head;
        while (node.next != null) {
            if (node.val == node.next.val) {
                node.next = node.next.next;
            } else {
                node = node.next;
            }
        }
        return head;
    }
}
```

Java版有个好处：不用自己管理内存，故不需要进行delete操作。
