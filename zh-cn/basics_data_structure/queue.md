# Queue - 队列

Queue 是一个 FIFO（先进先出）的数据结构，并发中使用较多，可以安全地将对象从一个任务传给另一个任务。

## 编程实现

### Python

Queue 和 Stack 在 Python 中都是有 `list` ,`[]` 实现的。 在python 中list是一个dynamic array, 可以通过`append`在list的尾部添加元素， 通过`pop()`在list的尾部弹出元素实现`Stack`的`FILO`， 如果是`pop(0)`则弹出头部的元素实现`Queue`的`FIFO`。
```python
queue = []  # same as list()
size = len(queue)
queue.append(1)
queue.append(2)
queue.pop(0) # return 1
queue[0] # return 2 examine the first element
```

#### Methods
| \ | methods |
| -- | -- |
| Insert | queue.append(e) |
| Remove | queue.pop(0) |
| Examine | queue[0] |

### Java

Queue 在 Java 中是 Interface, 一种实现是 LinkedList, LinkedList 向上转型为 Queue, Queue 通常不能存储 `null` 元素，否则与 `poll()` 等方法的返回值混淆。

```java
Queue<Integer> q = new LinkedList<Integer>();
int qLen = q.size(); // get queue length
```

#### Methods

| 0:0 | Throws exception | Returns special value |
| -- | -- | -- |
| Insert | add(e) | offer(e) |
| Remove | remove() | poll() |
| Examine | element() | peek() |

优先考虑右侧方法，右侧元素不存在时返回 `null`. 判断非空时使用`isEmpty()`方法，继承自 Collection.

## Priority Queue - 优先队列

应用程序常常需要处理带有优先级的业务，优先级最高的业务首先得到服务。因此优先队列这种数据结构应运而生。优先队列中的每个元素都有各自的优先级，优先级最高的元素最先得到服务；优先级相同的元素按照其在优先队列中的顺序得到服务。

优先队列可以使用数组或链表实现，从时间和空间复杂度来说，往往用二叉堆来实现。

### Python

Python 中提供`heapq`的lib来实现 priority queue. 提供`push`和`pop`两个基本操作和`heapify`初始化操作.

| \ | methods | time complexity |
| -- | -- | -- |
| enqueue | heapq.push(queue, e) | $$O(\log n)$$ |
| dequeue | heapq.pop(queue) | $$O(\log n)$$ |
| init | heapq.heapify(queue) | $$O(n\log n)$$ |
| peek | queue[0]| $$O(1)$$ |


### Java

Java 中提供`PriorityQueue`类，该类是 Interface Queue 的另外一种实现，和`LinkedList`的区别主要在于排序行为而不是性能，基于 priority heap 实现，非`synchronized`，故多线程下应使用`PriorityBlockingQueue`. 默认为自然序（小根堆），需要其他排序方式可自行实现`Comparator`接口，选用合适的构造器初始化。使用迭代器遍历时不保证有序，有序访问时需要使用`Arrays.sort(pq.toArray())`.

不同方法的时间复杂度：

- enqueuing and dequeuing: `offer`, `poll`, `remove()` and `add` - $$O(\log n)$$
- Object: `remove(Object)` and `contains(Object)` - $$O(n)$$
- retrieval: `peek`, `element`, and `size` - $$O(1)$$.

## Deque - 双端队列

双端队列（deque，全名double-ended queue）可以让你在任何一端添加或者移除元素，因此它是一种具有队列和栈性质的数据结构。

### Python

Python 的`list`就可以执行类似于`deque`的操作， 但是效率会过于慢。 为了提升数据的处理效率， 一些高效的数据结构放在了`collections`中。 在`collections` 中提供了`deque`的类， 如果需要多次对`list`执行头尾元素的操作， 请使用`deque`。

```python
dq = collections.deque();
```

#### Methods

| \ | methods | time complexity |
| -- | -- | -- |
| enqueue left | dq.appendleft(e) | $$O(1)$$ |
| enqueue right | dq.append(e) | $$O(1)$$ |
| dequeue left | dq.popleft() | $$O(1)$$ |
| dequeue right | dq.pop() | $$O(1)$$ |
| peek left | dq[0] | $$O(1)$$ |
| peek right | dq[-1] | $$O(1)$$ |

### Java

Java 在1.6之后提供了 Deque 接口，既可使用`ArrayDeque`（数组）来实现，也可以使用`LinkedList`（链表）来实现。前者是一个数组外加首尾索引，后者是双向链表。

```java
Deque<Integer> deque = new ArrayDeque<Integer>();
```

#### Methods

<table>
  <tr>
    <td></td>
    <td colspan="2">First Element (Head)</td>
    <td colspan="2">Last Element (Tail)</td>
  </tr>
  <tr>
    <td></td>
    <td>Throws exception</td>
    <td>Special value</td>
    <td>Throws exception</td>
    <td>Special value</td>
  </tr>
  <tr>
    <td>Insert</td>
    <td>`addFirst(e)`</td>
    <td>`offerFirst(e)`</td>
    <td>`addLast(e)`</td>
    <td>`offerLast(e)`</td>
  </tr>
  <tr>
    <td>Remove</td>
    <td>`removeFirst()`</td>
    <td>`pollFirst()`</td>
    <td>`removeLast()`</td>
    <td>`pollLast()`</td>
  </tr>
  <tr>
    <td>Examine</td>
    <td>`getFirst()`</td>
    <td>`peekFirst()`</td>
    <td>`getLast()`</td>
    <td>`peekLast()`</td>
  </tr>
</table>

其中`offerLast`和 Queue 中的`offer`功能相同，都是从尾部插入。

## Reference

- [優先佇列 - 维基百科，自由的百科全书](http://zh.wikipedia.org/zh/%E5%84%AA%E5%85%88%E4%BD%87%E5%88%97)
- [双端队列 - 维基百科，自由的百科全书](https://zh.wikipedia.org/wiki/%E5%8F%8C%E7%AB%AF%E9%98%9F%E5%88%97)
