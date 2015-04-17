# Remove Duplicates from Sorted List

Question: [(112) Remove Duplicates from Sorted List](http://www.lintcode.com/en/problem/remove-duplicates-from-sorted-list/)

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

## ￼Remove Duplicates from Sorted List II

Question: [(113) Remove Duplicates from Sorted List II](http://www.lintcode.com/en/problem/remove-duplicates-from-sorted-list-ii/)
```
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
```

### 题解

上题为保留重复值节点的一个，这题删除全部重复节点，看似区别不大，但是考虑到链表头不确定(可能被删除，也可能保留)，因此若用传统方式需要较多的if条件语句。**这里介绍一个处理链表头不确定的方法——引入dummy node.**
```
ListNode *dummy = new ListNode(0);
dummy->next = head;
ListNode *node = dummy;
```
引入新的指针变量`dummy`，并将其next变量赋值为head，考虑到原来的链表头节点可能被删除，故应该从dummy处开始处理，这里复用了head变量。考虑链表`A->B->C`，删除B时，需要处理和考虑的是A和C，将A的next指向C。如果从空间使用效率考虑，可以使用head代替以上的node，含义一样，node比较好理解点。

与上题不同的是，由于此题引入了新的节点`dummy`，不可再使用`node->val == node->next->val`，因为`dummy->val`有可能与第一个节点的值相等。故在判断val是否相等时需先确定`node->next`和`node->next->next`均不为空，否则不可对其进行取值。

说多了都是泪，先看看我的错误实现：


#### C++ Wrong

```
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
class Solution{
public:
    /**
     * @param head: The first node of linked list.
     * @return: head node
     */
    ListNode * deleteDuplicates(ListNode *head) {
        if (head == NULL || head->next == NULL) {
            return NULL;
        }

        ListNode *dummy;
        dummy->next = head;
        ListNode *node = dummy;

        while (node->next != NULL && node->next->next != NULL) {
            if (node->next->val == node->next->next->val) {
                int val = node->next->val;
                while (node->next != NULL && val == node->next->val) {
                    ListNode *temp = node->next;
                    node->next = node->next->next;
                    delete temp;
                }
            } else {
                node->next = node->next->next;
            }
        }

        return dummy->next;
    }
};
```

错在什么地方？

1. 节点dummy的初始化有问题，对类的初始化应该使用`new`
2. 在else语句中`node->next = node->next->next;`改写了`dummy-next`中的内容，返回的`dummy-next`不再是队首元素，而是队尾元素。原因很微妙，应该使用`node = node->next;`，node代表节点指针变量，而node->next代表当前节点所指向的下一节点地址。具体分析可自行在纸上画图分析，可对指针和链表的理解又加深不少。

![remove_duplicates_from_sorted_listd内存分析](../figure/remove_duplicates_from_sorted_list.jpg)

图中上半部分为ListNode的内存示意图，每个框底下为其内存地址。`dummy`指针变量本身的地址为ox7fff5d0d2500，其保存着指针变量值为0x7fbe7bc04c50. `head`指针变量本身的地址为ox7fff5d0d2508，其保存着指针变量值为0x7fbe7bc04c00.

好了，接下来看看正确实现及解析。


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
class Solution{
public:
    /**
     * @param head: The first node of linked list.
     * @return: head node
     */
    ListNode * deleteDuplicates(ListNode *head) {
        if (head == NULL || head->next == NULL) {
            return NULL;
        }

        ListNode *dummy = new ListNode(0);
        dummy->next = head;
        ListNode *node = dummy;

        while (node->next != NULL && node->next->next != NULL) {
            if (node->next->val == node->next->next->val) {
                int val = node->next->val;
                while (node->next != NULL && val == node->next->val) {
                    ListNode *temp = node->next;
                    node->next = node->next->next;
                    delete temp;
                }
            } else {
                node = node->next;
            }
        }

        return dummy->next;
    }
};
```

#### 源码分析

1. 首先考虑异常情况，head和head->next均考虑可减少后面的麻烦。
2. new一个dummy变量，指向原链表头。
3. 使用新变量node并设置其为dummy头节点，遍历用。
4. 当前节点和下一节点val相同时先保存当前值，便于while循环终止条件判断和删除节点。注意这一段代码也比较精炼。
5. 最后返回`dummy->next`，即题目所要求的头节点。
