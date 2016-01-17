# Min Stack

## Question

- lintcode: [(12) Min Stack](http://www.lintcode.com/en/problem/min-stack/)

```
Implement a stack with min() function,
which will return the smallest number in the stack.

It should support push, pop and min operation all in O(1) cost.

Example
Operations: push(1), pop(), push(2), push(3), min(), push(1), min() Return: 1, 2, 1

Note
min operation will never be called if there is no number in the stack
```

## 题解

『最小』栈，要求在栈的基础上实现可以在 $$O(1)$$ 的时间内找出最小值，一般这种 $$O(1)$$的实现往往就是哈希表或者哈希表的变体，这里简单起见可以另外克隆一个栈用以跟踪当前栈的最小值。

### Java

```java
public class Solution {
    public Solution() {
        stack1 = new Stack<Integer>();
        stack2 = new Stack<Integer>();
    }

    public void push(int number) {
        stack1.push(number);
        if (stack2.empty()) {
            stack2.push(number);
        } else {
            stack2.push(Math.min(number, stack2.peek()));
        }
    }

    public int pop() {
        stack2.pop();
        return stack1.pop();
    }

    public int min() {
        return stack2.peek();
    }

    private Stack<Integer> stack1; // original stack
    private Stack<Integer> stack2; // min stack
}
```

### 源码分析

取最小栈的栈顶值时需要先判断是否为空栈(而不仅是 null)。

### 复杂度分析

均为 $$O(1)$$.
