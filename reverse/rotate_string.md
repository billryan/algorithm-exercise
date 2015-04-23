# Rotate String

## Source

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

### 题解

常见的翻转法应用题，仔细观察规律可知翻转的分割点在从数组末尾数起的offset位置。

#### C++

```c++
class Solution {
public:
  /**
     * param A: A string
     * param offset: Rotate string with offset.
     * return: Rotated string.
     */
    string rotateString(string A, int offset) {
        if (A.empty()) {
            return A;
        }

        string::size_type sizeA = A.size();
        offset %= sizeA;
        if (offset == 0) {
            return A;
        }

        reverse(A, 0, sizeA - offset - 1);
        reverse(A, sizeA - offset, sizeA - 1);
        reverse(A, 0, sizeA - 1);

        return A;
    }

private:
    void reverse(string &str, string::size_type start, string::size_type end) {
        for (string::size_type i = start, j = end; i < j; ++i, --j) {
            char temp = str[i];
            str[i] = str[j];
            str[j] = temp;
        }
    }
};

```

#### 源码分析

1. 异常处理，A为空或者offset模sizeA后为0
2. offset可能超出A的大小，应模sizeA后再用
3. 三步翻转法
