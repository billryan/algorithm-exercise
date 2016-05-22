# Reverse Linked List

## Question

- leetcode: [Reverse Linked List | LeetCode OJ](https://leetcode.com/problems/reverse-linked-list/)
- lintcode: [(35) Reverse Linked List](http://www.lintcode.com/en/problem/reverse-linked-list/)

```
Reverse a linked list.

Example
For linked list 1->2->3, the reversed linked list is 3->2->1

Challenge
Reverse it in-place and in one-pass
```

## 題解1 - 非遞迴

聯想到同樣也可能需要翻轉的數組，在數組中由於可以利用下標隨機訪問，翻轉時使用下標即可完成。而在單向鏈表中，僅僅只知道頭節點，而且只能單向往前走，故需另尋出路。分析由`1->2->3`變為`3->2->1`的過程，由於是單向鏈表，故只能由1開始遍曆，1和2最開始的位置是`1->2`，最後變為`2->1`，故從這裡開始尋找突破口，探討如何交換1和2的節點。

```
temp = head->next;
head->next = prev;
prev = head;
head = temp;
```

要點在於維護兩個指針變量`prev`和`head`, 翻轉相鄰兩個節點之前保存下一節點的值，分析如下圖所示：

![Reverse Linked List](../../shared-files/images/reverse_linked_list_i.jpg)

1. 保存head下一節點
2. 將head所指向的下一節點改為prev
3. 將prev替換為head，波浪式前進
4. 將第一步保存的下一節點替換為head，用於下一次循環

### Python

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        prev = None
        curr = head
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        # fix head
        head = prev

        return head
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
    ListNode* reverse(ListNode* head) {
        ListNode *prev = NULL;
        ListNode *curr = head;
        while (curr != NULL) {
            ListNode *temp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = temp;
        }
        // fix head
        head = prev;

        return head;
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
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;
        while (curr != null) {
            ListNode temp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = temp;
        }
        // fix head
        head = prev;

        return head;
    }
}
```

### 源碼分析

題解中基本分析完畢，代碼中的prev賦值操作精煉，值得借鑒。

### 複雜度分析

遍歷一次鏈表，時間複雜度為 $$O(n)$$, 使用了輔助變數，空間複雜度 $$O(1)$$.

## 題解2 - 遞迴

遞迴的終止步分三種情況討論：

1. 原鏈表為空，直接返回空鏈表即可。
2. 原鏈表僅有一個元素，返回該元素。
3. 原鏈表有兩個以上元素，由於是單向鏈表，故翻轉需要自尾部向首部逆推。

由尾部向首部逆推時大致步驟為先翻轉當前節點和下一節點，然後將當前節點指向的下一節點置空(否則會出現死循環和新生成的鏈表尾節點不指向空)，如此遞迴到頭節點為止。新鏈表的頭節點在整個遞迴過程中一直沒有變化，逐層向上返回。

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
    @param head: The first node of the linked list.
    @return: You should return the head of the reversed linked list.
                  Reverse it in-place.
    """
    def reverse(self, head):
        # case1: empty list
        if head is None:
            return head
        # case2: only one element list
        if head.next is None:
            return head
        # case3: reverse from the rest after head
        newHead = self.reverse(head.next)
        # reverse between head and head->next
        head.next.next = head
        # unlink list from the rest
        head.next = None

        return newHead
```

### C++

```c++
/**
 * Definition of ListNode
 *
 * class ListNode {
 * public:
 *     int val;
 *     ListNode *next;
 *
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
     * @return: The new head of reversed linked list.
     */
    ListNode *reverse(ListNode *head) {
        // case1: empty list
        if (head == NULL) return head;
        // case2: only one element list
        if (head->next == NULL) return head;
        // case3: reverse from the rest after head
        ListNode *newHead = reverse(head->next);
        // reverse between head and head->next
        head->next->next = head;
        // unlink list from the rest
        head->next = NULL;

        return newHead;
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
    public ListNode reverse(ListNode head) {
        // case1: empty list
        if (head == null) return head;
        // case2: only one element list
        if (head.next == null) return head;
        // case3: reverse from the rest after head
        ListNode newHead = reverse(head.next);
        // reverse between head and head->next
        head.next.next = head;
        // unlink list from the rest
        head.next = null;

        return newHead;
    }
}
```

### 源碼分析

case1 和 case2 可以合在一起考慮，case3 返回的為新鏈表的頭節點，整個遞迴過程中保持不變。

### 複雜度分析

遞迴嵌套層數為 $$O(n)$$, 時間複雜度為 $$O(n)$$, 空間(不含函數堆疊空間)複雜度為 $$O(1)$$.

## Reference

- [全面分析再動手的習慣：鏈表的反轉問題（遞迴和非遞迴方式） - 木棉和木槿 - 博客園](http://www.cnblogs.com/kubixuesheng/p/4394509.html)
- [data structures - Reversing a linked list in Java, recursively - Stack Overflow](http://stackoverflow.com/questions/354875/reversing-a-linked-list-in-java-recursively)
- [反轉單向鏈表的四種實現（遞迴與非遞迴，C++） | 寧心勉學，慎思篤行](http://ceeji.net/blog/reserve-linked-list-cpp/)
- [iteratively and recursively Java Solution - Leetcode Discuss](https://leetcode.com/discuss/37804/iteratively-and-recursively-java-solution)
