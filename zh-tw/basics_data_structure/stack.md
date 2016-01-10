# Stack - 堆疊

堆疊是一種 LIFO(Last In First Out) 的資料結構，常用方法有添加元素，讀Stack頂元素，彈出(pop) Stack頂元素，判斷堆疊是否為空。

## 程式碼實現

### Python
```python
stack = []
len(stack) # size of stack

# more efficient stack
import collections
stack = collections.deque()
```

`list`作為最基本的`python`資料結構之一， 可以很輕鬆地實現`stack`。 如果需要更高效的`stack`， 建議使用`deque`。

#### Methods

- `len(stack) != 0` - 判斷`stack`是否為空
- `stack[-1]` - 取堆疊頂元素，不移除
- `pop()` - 移除堆疊頂元素並返回該元素
- `append(item)` - 向堆疊頂添加元素


### Java

```java
Deque<Integer> stack = new ArrayDeque<Integer>();
s.size(); // size of stack
```

JDK doc 中建議使用`Deque`代替`Stack`實現堆疊，因為`Stack`繼承自`Vector`，需要`synchronized`，性能略低。

#### Methods

- `boolean	isEmpty()` - 判斷堆疊是否為空，若使用 Stack 類構造則為 empty()
- `E peek()` - 取堆疊頂元素，不移除
- `E pop()` - 移除堆疊頂元素並返回該元素
- `E push(E item)` - 向堆疊頂添加元素
