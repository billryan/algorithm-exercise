# Rotate String

## Source

- lintcode: [(8) Rotate String](http://www.lintcode.com/en/problem/rotate-string/)

### Problem

Given a string and an offset, rotate string by offset. (rotate from left to
right)

#### Example

Given `"abcdefg"`.



    offset=0 => "abcdefg"
    offset=1 => "gabcdef"
    offset=2 => "fgabcde"
    offset=3 => "efgabcd"


#### Challenge

Rotate in-place with O(1) extra memory.

## 题解

常见的翻转法应用题，仔细观察规律可知翻转的分割点在从数组末尾数起的offset位置。先翻转前半部分，随后翻转后半部分，最后整体翻转。

### Python

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

#### 补充 :python 若要达空间复杂度为 O(1) 输入(input)须为串列(list)，若为字串(string)只能达成空间复杂度 O(n)，时间复杂度皆为O(n)
#### 以下范例为LintCode原题解法

```python
class Solution:
    # @param s: a list of char
    # @param offset: an integer 
    # @return: nothing
    def rotateString(self, A, offset):
        if A is None or len(A) == 0:
            return 
        offset %= len(A)
        self.reverse(A, 0, len(A)-offset-1)
        self.reverse(A, len(A)-offset, len(A)-1)
        self.reverse(A, 0, len(A)-1)
        return 
    def reverse(self, str, start, end):
        while start < end :            
            str[start], str[end] = str[end], str[start]             
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

### 复杂度分析

翻转一次时间复杂度近似为 $$O(n)$$, 原地交换，空间复杂度为 $$O(1)$$. 总共翻转3次，总的时间复杂度为 $$O(n)$$, 空间复杂度为 $$O(1)$$.

## Reference

- [Reverse a string in Python - Stack Overflow](http://stackoverflow.com/questions/931092/reverse-a-string-in-python)
