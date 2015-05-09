# Copy List with Random Pointer

## Source

- lintcode: [(105) Copy List with Random Pointer](http://www.lintcode.com/en/problem/copy-list-with-random-pointer/)

```
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
```

## 题解

这题要求**深度拷贝**一个带有 random 指针的链表，random 可能指向空，也可能指向链表中的任意一个节点。

### Solution 1

所有类似的**深度拷贝**题目的传统做法，都是维护一个 `hash table`。即先按照复制一个正常链表的方式复制，复制的时候把复制的结点做一个 `hash table`，以旧结点为 key，新节点为 value。这么做的目的是为了第二遍扫描的时候我们按照这个哈希表把结点的 random 指针接上。

####C++
```c++
class Solution {
public:
    RandomListNode *copyRandomList(RandomListNode *head) {
        if(head == NULL) {
            return NULL;
        }

        RandomListNode dummy(0);
        RandomListNode* n = &dummy;
        RandomListNode* h = head;
        map<RandomListNode*, RandomListNode*> m;
        while(h) {
            RandomListNode* node = new RandomListNode(h->label);
            n->next = node;
            n = node;

            node->random = h->random;

            m[h] = node;

            h = h->next;
        }

        h = dummy.next;
        while(h) {
            if(h->random != NULL) {
                h->random = m[h->random];
            }
            h = h->next;
        }

        return dummy.next;
    }
};
```

#### 复杂度分析

总共要进行两次扫描，所以时间复杂度是O(2*n)=O(n)。空间上需要一个哈希表来做结点的映射，所以空间复杂度也是O(n)。

### Solution 1.5
####C++
```c++
class Solution {
public:
    RandomListNode *copyRandomList(RandomListNode *head) {
        if(head == NULL) {
            return NULL;
        }

        RandomListNode *dummy = new RandomListNode(0);
        RandomListNode *prev = dummy;
        map<RandomListNode *, RandomListNode *> random_map;
        
        while (head != NULL) {
            RandomListNode *newNode = new RandomListNode(head->label);
            random_map[head] = newNode;
            prev->next = newNode;
            
            if (head->random != NULL) {
                if (random_map.find(head->random) == random_map.end()) {
                    newNode->random = new RandomListNode(head->random->label);
                    random_map[head->random] = newNode->random;
                } else {
                    newNode->random = random_map[head->random];
                }
            }
            
            prev = newNode;
            head = head->next;
        }
        return dummy->next;
    }
};
```

####Java
```java
public class Solution {
    public RandomListNode copyRandomList(RandomListNode head) {
        if (head == null) {
            return null;
        }

        HashMap<RandomListNode, RandomListNode> map = new HashMap<RandomListNode, RandomListNode>();
        RandomListNode dummy = new RandomListNode(0);
        RandomListNode pre = dummy, newNode;
        while (head != null) {
            if (map.containsKey(head)) {
                newNode = map.get(head);
            } else {
                newNode = new RandomListNode(head.label);
                map.put(head, newNode);
            }
            pre.next = newNode;

            if (head.random != null) {
                if (map.containsKey(head.random)) {
                    newNode.random = map.get(head.random);
                } else {
                    newNode.random = new RandomListNode(head.random.label);
                    map.put(head.random, newNode.random);
                }
            }

            pre = newNode;
            head = head.next;
        }

        return dummy.next;
    }
}
```

#### 复杂度分析

可以算作是 Solution 1.5 的版本，因为这样不需要遍历两次。而是在同一次遍历中，如果遇到 random 的指针指向的结点还没有访问过的情况，就当即存入 map 即可。但是时间复杂度还是 $$O(n)$$。


### Solution 2

上面的解法很显然，需要额外的空间。这个额外的空间是由 `hash table` 的维护造成的。因为当我们访问一个结点时可能它的 random 指针指向的结点还没有访问过，结点还没有创建，所以需要用 `hash table` 的额外线性空间维护。

但我们可以通过链表原来结构中的 `next` 指针来替代 `hash table` 做哈希。假设有如下链表：

```
|------------|
|            v
1  --> 2 --> 3 --> 4

```

节点1的 random 指向了3。首先我们可以通过 next 遍历链表，依次拷贝节点，并将其添加到原节点后面，如下：

```
|--------------------------|
|                          v
1  --> 1' --> 2 --> 2' --> 3 --> 3' --> 4 --> 4'
       |                   ^
       |-------------------|
```

因为我们只是简单的复制了 random 指针，所以新的节点的 random 指向的仍然是老的节点，譬如上面的1和1'都是指向的3。

调整新的节点的 random 指针，对于上面例子来说，我们需要将1'的 random 指向3'，其实也就是原先 random 指针的next节点。

```
|--------------------------|
|                          v
1  --> 1' --> 2 --> 2' --> 3 --> 3' --> 4 --> 4'
       |                         ^
       |-------------------------|
```

最后，拆分链表，就可以得到深度拷贝的链表了。

总结起来，实际我们对链表进行了三次扫描，第一次扫描对每个结点进行复制，然后把复制出来的新节点接在原结点的 next 指针上，也就是让链表变成一个重复链表，就是新旧更替；第二次扫描中我们把旧结点的随机指针赋给新节点的随机指针，因为新结点都跟在旧结点的下一个，所以赋值比较简单，就是 `node->next->random = node->random->next`，其中 `node->next` 就是新结点，因为第一次扫描我们就是把新结点接在旧结点后面。现在我们把结点的随机指针都接好了，最后一次扫描我们把链表拆成两个，第一个还原原链表，而第二个就是我们要求的复制链表。因为现在链表是旧新更替，只要把每隔两个结点分别相连，对链表进行分割即可。
```c++
class Solution {
public:
    RandomListNode *copyRandomList(RandomListNode *head) {
        if(head == NULL) {
            return NULL;
        }

        //遍历并插入新的节点
        RandomListNode* n = NULL;
        RandomListNode* h = head;
        while(h) {
            RandomListNode* node = new RandomListNode(h->label);
            node->random = h->random;

            n = h->next;

            h->next = node;
            node->next = n;
            h = n;
        }

        //调整random
        h = head->next;
        while(h) {
            if(h->random != NULL) {
                h->random = h->random->next;
            }
            if(!h->next) {
                break;
            }
            h = h->next->next;
        }

        //断开链表
        h = head;
        RandomListNode dummy(0);
        RandomListNode* p = &dummy;
        while(h) {
            n = h->next;
            p->next = n;
            p = n;
            RandomListNode* nn = n->next;
            h->next = n->next;
            h = n->next;
        }

        return dummy.next;
    }
};
```
#### 复杂度分析

Solution 2 总共进行三次线性扫描，所以时间复杂度是 $$O(n)$$。但不再需要额外空间的 `hash table`，所以空间复杂度是 $$O(1)$$。



## Reference

- [Copy List with Random Pointer - siddontang's leetcode Solution Book](http://siddontang.gitbooks.io/leetcode-solution/content/linked_list/copy_list_with_random_pointer.html/)
- 

- [Copy List with Random Pointer - Code Ganker](http://blog.csdn.net/linhuanmars/article/details/22463599)
