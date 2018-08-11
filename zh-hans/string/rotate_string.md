# Rotate String

Tags: String, Easy

## Question

- lintcode: [Rotate String](http://www.lintcode.com/en/problem/rotate-string/)

### Problem Statement

Given a string and an offset, rotate string by offset. (rotate from left to
right)

**Example**

Given `"abcdefg"`.

    
    
    offset=0 => "abcdefg"
    offset=1 => "gabcdef"
    offset=2 => "fgabcde"
    offset=3 => "efgabcd"
    

**Challenge**

Rotate in-place with O(1) extra memory.

## 题解

常见的翻转法应用题，仔细观察规律可知翻转的分割点在从数组末尾数起的offset位置。先翻转前半部分，随后翻转后半部分，最后整体翻转。

### Python - immutable string

```python
class Solution:
    """
    param A: A string
    param offset: Rotate string with offset.
    return: Rotated string.
    """
    def rotateString(self, A, offset):
        if A is None or len(A) == 0:
            return A

        offset %= len(A)
        before = A[:len(A) - offset]
        after = A[len(A) - offset:]
        # [::-1] means reverse in Python
        A = before[::-1] + after[::-1]
        A = A[::-1]

        return A
```

### Python - mutable list

```python
class Solution:
    # @param A: a list of char
    # @param offset: an integer
    # @return: nothing
    def rotateString(self, A, offset):
        if A is None or len(A) == 0:
            return

        offset %= len(A)
        self.reverse(A, 0, len(A)-offset-1)
        self.reverse(A, len(A)-offset, len(A)-1)
        self.reverse(A, 0, len(A)-1)

    def reverse(self, str_l, start, end):
        while start < end:
            str_l[start], str_l[end] = str_l[end], str_l[start]
            start += 1
            end -= 1
```

### C++

```c++
class Solution {
public:
  /**
     * param A: A string
     * param offset: Rotate string with offset.
     * return: Rotated string.
     */
    string rotateString(string A, int offset) {
        if (A.empty() || A.size() == 0) {
            return A;
        }

        int len = A.size();
        offset %= len;
        reverse(A, 0, len - offset - 1);
        reverse(A, len - offset, len - 1);
        reverse(A, 0, len - 1);
        return A;
    }

private:
    void reverse(string &str, int start, int end) {
        while (start < end) {
            char temp = str[start];
            str[start] = str[end];
            str[end] = temp;
            start++;
            end--;
        }
    }
};
```

### Java

```java
public class Solution {
    /*
     * param A: A string
     * param offset: Rotate string with offset.
     * return: Rotated string.
     */
    public char[] rotateString(char[] A, int offset) {
        if (A == null || A.length == 0) {
            return A;
        }

        int len = A.length;
        offset %= len;
        reverse(A, 0, len - offset - 1);
        reverse(A, len - offset, len - 1);
        reverse(A, 0, len - 1);

        return A;
    }

    private void reverse(char[] str, int start, int end) {
        while (start < end) {
            char temp = str[start];
            str[start] = str[end];
            str[end] = temp;
            start++;
            end--;
        }
    }
};
```

### 源码分析

1. 异常处理，A为空或者其长度为0
2. `offset`可能超出A的大小，应模`len`后再用
3. 三步翻转法

Python 虽没有提供字符串的翻转，但用 slice 非常容易实现，非常 Pythonic!

**通常来说，字符串在各种编程语言中的实现一般为 immutable 的，对字符串做改变时往往会生成新的字符串，所以如果要达到空间复杂度为 O(1) 的效果，需要用可变数据结构来实现。**

### 复杂度分析

翻转一次时间复杂度近似为 $$O(n)$$, 原地交换的空间复杂度为 $$O(1)$$, 非原地交换的空间复杂度为 $$O(n)$$. 总共翻转3次，所以总的时间复杂度为 $$O(n)$$, 空间复杂度为 $$O(1)$$ 或者 $$O(n)$$.

## Reference

- [Reverse a string in Python](http://stackoverflow.com/questions/931092/reverse-a-string-in-python)
- [What’s New in Python 2.3 — Extended Slices](https://docs.python.org/2/whatsnew/2.3.html#extended-slices)
- 