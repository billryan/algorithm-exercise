# Stack - 栈

栈是一种 LIFO(Last In First Out) 的数据结构，常用方法有添加元素，取栈顶元素，弹出栈顶元素，判断栈是否为空。

## 编程实现

### Java

```
Deque<Integer> stack = new ArrayDeque<Integer>();
s.size(); // size of stack
```

JDK doc 中建议使用`Deque`代替`Stack`实现栈，因为`Stack`继承自`Vector`，需要`synchronized`，性能略低。

#### Methods

- `boolean	isEmpty()` - 判断栈是否为空，若使用 Stack 类构造则为 empty()
- `E peek()` - 取栈顶元素，不移除
- `E pop()` - 移除栈顶元素并返回该元素
- `E push(E item)` - 向栈顶添加元素
