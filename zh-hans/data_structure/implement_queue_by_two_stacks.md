# Implement Queue by Two Stacks

## Question

- lintcode: [(40) Implement Queue by Two Stacks](http://www.lintcode.com/en/problem/implement-queue-by-two-stacks/)

```
As the title described, you should only use two stacks to implement a queue's actions.

The queue should support push(element), 
pop() and top() where pop is pop the first(a.k.a front) element in the queue.

Both pop and top methods should return the value of first element.

Example
For push(1), pop(), push(2), push(3), top(), pop(), you should return 1, 2 and 2

Challenge
implement it by two stacks, do not use any other data structure and push, 
pop and top should be O(1) by AVERAGE.
```

## 题解

两个栈模拟队列，栈是 LIFO, 队列是 FIFO, 故用两个栈模拟队列时可结合栈1和栈2, LIFO + LIFO ==> FIFO, 即先将一个栈元素全部 push 到另一个栈，效果即等价于 Queue.

### Java

```java
public class Solution {
    private Stack<Integer> stack1;
    private Stack<Integer> stack2;

    public Solution() {
        // source stack
        stack1 = new Stack<Integer>();
        // target stack
        stack2 = new Stack<Integer>();
    }

    public void push(int element) {
        stack1.push(element);
    }

    public int pop() {
        if (stack2.empty()) {
            stack1ToStack2(stack1, stack2);
        }
        return stack2.pop();
    }

    public int top() {
        if (stack2.empty()) {
            stack1ToStack2(stack1, stack2);
        }
        return stack2.peek();
    }

    private void stack1ToStack2(Stack<Integer> stack1, Stack<Integer> stack2) {
        while (!stack1.empty()) {
            stack2.push(stack1.pop());
        }
    }
}
```

### 源码分析

将栈1作为原始栈，将栈1元素压入栈2是公共方法，故写成一个私有方法。

### 复杂度分析

视连续 push 的元素而定，时间复杂度近似为 $$O(1)$$.

## Reference

- [Implement Queue by Two Stacks 参考程序 Java/C++/Python](http://www.jiuzhang.com/solutions/implement-queue-by-two-stacks/)
