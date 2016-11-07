# Linked List - 鏈表

鏈表是線性表(linear list)的一種。線性表是最基本、最簡單、也是最常用的一種資料結構。線性表中數據元素之間的關係是一對一的關系，即除了第一個和最後一個數據元素之外，其它數據元素都是首尾相接的。線性表有兩種儲存方式，一種是順序儲存結構，另一種是鏈式儲存結構。我們常用的陣列(array)就是一種典型的順序儲存結構。

相反，鏈式儲存結構就是兩個相鄰的元素在記憶體中可能不是物理相鄰的，每一個元素都有一個指標，指標一般是儲存著到下一個元素的指標。這種儲存方式的**優點**是已知插入位置時，定點插入和定點刪除的時間複雜度為 O(1)，不會浪費太多記憶體，添加元素的時候才會申請記憶體空間，刪除元素會釋放記憶體空間。缺點是訪問的時間複雜度最壞為 O(n)。

順序表的特性是隨機讀取，也就是循下標訪問(call-by-index)一個元素的時間複雜度是O(1)，鏈式表的特性是插入和刪除的時間複雜度為O(1)。

鏈表就是鏈式儲存的線性表。根據指標域的不同，鏈表分為單向鏈表、雙向鏈表、循環鏈表等等。

## 程式碼實現

### Python

```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
```

###C++
```cpp
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int val, ListNode *next=NULL):val(val),next(next){}
};

```

### Java

```java
public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int val) {
        this.val = val;
        this.next = null;
    }
}
```

## 鏈表的基本操作

### 反轉單向鏈表(singly linked list)

鏈表的基本形式是：`1 -> 2 -> 3 -> null`，反轉需要變為 `3 -> 2 -> 1 -> null`。這裡要注意：
- 訪問某個節點 curt.next 時，要檢驗 curt 是否為 null。
- 要把反轉後的最後一個節點（即反轉前的第一個節點）指向 null。

```java
public ListNode reverse(ListNode head) {
    ListNode prev = null;
    while (head != null) {
        ListNode next = head.next;
        head.next = prev;
        prev = head;
        head = next;
    }
    return prev;
}
```

#### 雙向鏈表

和單向鏈表的區別在於：雙向鏈表的反轉核心在於`next`和`prev`域的交換，還需要注意的是目前節點和上一個節點的遞推。

### Python

```python
class DListNode:
    def __init__(self, val):
        self.val = val
        self.prev = self.next = null

    def reverse(self, head):
        curt = None
        while head:
            curt = head
            head = curt.next
            curt.next = curt.prev
            curt.prev = head
        return curt
```

### Java

```java
class DListNode {
    int val;
    DListNode prev, next;
    DListNode(int val) {
        this.val = val;
        this.prev = this.next = null;
    }
}

public DListNode reverse(DListNode head) {
    DListNode curr = null;
    while (head != null) {
        curr = head;
        head = curr.next;
        curr.next = curr.prev;
        curr.prev = head;
    }
    return curr;
}
```

### 刪除鏈表中的某個節點

刪除鏈表中的某個節點一定需要知道這個點的前繼節點，所以需要一直有指標指向前繼節點。

然後只需要把 `prev -> next = prev -> next -> next` 即可。但是由於鏈表表頭可能在這個過程中產生變化，導致我們需要一些特別的技巧去處理這種情況。就是下面提到的 Dummy Node。

## 鏈表指標的強健性(robustness)

綜合上面討論的兩種基本操作，鏈表操作時的強健性問題主要包含兩個情況：
- 當訪問鏈表中某個節點 curt.next 時，一定要先判斷 curt 是否為 null。
- 全部操作結束後，判斷是否有環；若有環，則置其中一端為 null。

## Dummy Node

Dummy node 是鏈表問題中一個重要的技巧，中文翻譯叫「啞節點」或者「假人頭結點」。

Dummy node 是一個虛擬節點，也可以認為是標竿節點。Dummy node 就是在鏈表表頭 head 前加一個節點指向 head，即 dummy -> head。Dummy node 的使用多針對單向鏈表沒有前向指標的問題，保證鏈表的 head 不會在刪除操作中遺失。除此之外，還有一種用法比較少見，就是使用 dummy node 來進行head的刪除操作，比如 [Remove Duplicates From Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)，一般的方法current = current.next 是無法刪除 head 元素的，所以這個時候如果有一個dummy node在head的前面。

所以，當鏈表的 head 有可能變化（被修改或者被刪除）時，使用 dummy node 可以簡化程式碼及很多邊界情況的處理，最終返回 dummy.next 即新的鏈表。

## 快慢指標(fast/slow pointer)

快慢指標也是一個可以用於很多問題的技巧。所謂快慢指標中的快慢指的是指標向前移動的步長，每次移動的步長較大即為快，步長較小即為慢，常用的快慢指標一般是在單向鏈表中讓快指標每次向前移動2，慢指標則每次向前移動1。快慢兩個指標都從鏈表頭開始遍曆，於是快指標到達鏈表末尾的時候慢指標剛好到達中間位置，於是可以得到中間元素的值。快慢指標在鏈表相關問題中主要有兩個應用：
- 快速找出未知長度單向鏈表的中間節點
	設置兩個指標 `*fast`、`*slow` 都指向單向鏈表的頭節點，其中`*fast`的移動速度是`*slow`的2倍，當`*fast`指向末尾節點的時候，`slow`正好就在中間了。此方法可以有效避免多次遍歷鏈表
- 判斷單向鏈表是否有環
	利用快慢指標的原理，同樣設置兩個指標 `*fast`、`*slow` 都指向單向鏈表的頭節點，其中 `*fast`的移動速度是`*slow`的2倍。如果 `*fast = NULL`，說明該單向鏈表 以 `NULL`結尾，不是循環鏈表；如果 `*fast = *slow`，則快指標追上慢指標，說明該鏈表是循環鏈表。


### Python

```python
class NodeCircle:
    def __init__(self, val):
        self.val = val
        self.next = None

    def has_circle(self, head):
        slow = head
        fast = head
        while (slow and fast):
            fast = fast.next
            slow = slow.next
            if fast:
                fast = fast.next
            if fast == slow:
                break
        if fast and slow and (fast == slow):
            return True
        else:
            return False
```
