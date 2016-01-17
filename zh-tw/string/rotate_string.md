# Rotate String

## Question

- lintcode: [(8) Rotate String](http://www.lintcode.com/en/problem/rotate-string/)

```
Given a string and an offset, rotate string by offset. (rotate from left to right)

Example
Given "abcdefg"

for offset=0, return "abcdefg"

for offset=1, return "gabcdef"

for offset=2, return "fgabcde"

for offset=3, return "efgabcd"

...
```

## 題解

常見的翻轉法應用題，仔細觀察規律可知翻轉的分割點在從數組末尾數起的offset位置。先翻轉前半部分，隨後翻轉後半部分，最後整體翻轉。

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

### 源碼分析

1. 異常處理，A為空或者其長度為0
2. `offset`可能超出A的大小，應對`len`取餘數後再用
3. 三步翻轉法

Python 雖沒有提供字符串的翻轉，但用 slice 非常容易實現，非常 Pythonic!

### 複雜度分析

翻轉一次時間複雜度近似為 $$O(n)$$, 原地交換，空間複雜度為 $$O(1)$$. 總共翻轉3次，總的時間複雜度為 $$O(n)$$, 空間複雜度為 $$O(1)$$.

## Reference

- [Reverse a string in Python - Stack Overflow](http://stackoverflow.com/questions/931092/reverse-a-string-in-python)
