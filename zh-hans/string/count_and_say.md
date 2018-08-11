# Count and Say

Tags: String, Easy

## Question

- leetcode: [Count and Say](https://leetcode.com/problems/count-and-say/)
- lintcode: [Count and Say](http://www.lintcode.com/en/problem/count-and-say/)

### Problem Statement

The count-and-say sequence is the sequence of integers beginning as follows:  
`1, 11, 21, 1211, 111221, ...`

`1` is read off as `"one 1"` or `11`.  
`11` is read off as `"two 1s"` or `21`.  
`21` is read off as `"one 2`, then `one 1"` or `1211`.  

Given an integer _n_, generate the _n_th sequence.

Note: The sequence of integers will be represented as a string.

## 题解1 - 迭代

题目大意是找第 n 个数(字符串表示)，规则则是对于连续字符串，表示为重复次数+数本身。那么其中的核心过程则是根据上一个字符串求得下一个字符串，从 `'1'` 开始迭代 n - 1 次即可。

### Python

```python
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 0:
            return ''
        seq = '1'
        for _ in range(n - 1):
            seq = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), seq)

        return seq
```

### Python

```python
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 0:
            return ''

        curr_seq = '1'
        for j in range(n - 1):
            curr_seq = self._get_next_seq(curr_seq)

        return curr_seq

    def _get_next_seq(self, seq):
        next_seq = ''
        cnt = 1
        for i in range(len(seq)):
            if i + 1 < len(seq) and seq[i] == seq[i + 1]:
                cnt += 1
            else:
                next_seq += str(cnt)
                next_seq += seq[i]
                cnt = 1

        return next_seq
```

### C++

```cpp
class Solution {
public:
    string countAndSay(int n) {
        if (n <= 0) return "";

        string curr_seq = "1";
        while (--n) {
            curr_seq = getNextSeq(curr_seq);
        }

        return curr_seq;
    }

private:
    string getNextSeq(string seq) {
        string next_seq = "";
        int cnt = 1;
        for (int i = 0; i < seq.length(); i++) {
            if (i + 1 < seq.length() && seq[i] == seq[i + 1]) {
                cnt++;
            } else {
                next_seq.push_back('0' + cnt);
                next_seq.push_back(seq[i]);
                cnt = 1;
            }
        }

        return next_seq;
    }
};
```

### Java

```java
public class Solution {
    public String countAndSay(int n) {
        assert n > 0;
        StringBuilder currSeq = new StringBuilder("1");
        for (int i = 1; i < n; i++) {
            currSeq = getNextSeq(currSeq);
        }
        return currSeq.toString();
    }

    private StringBuilder getNextSeq(StringBuilder seq) {
        StringBuilder nextSeq = new StringBuilder();
        int cnt = 1;
        for (int i = 0; i < seq.length(); i++) {
            if (i + 1 < seq.length() && seq.charAt(i) == seq.charAt(i + 1)) {
                cnt++;
            } else {
                nextSeq.append(cnt).append(seq.charAt(i));
                cnt = 1;
            }
        }
        return nextSeq;
    }
}
```

### 源码分析

字符串是动态生成的，Python 中 `next_seq` 使用了两次 append 而不是字符串直接拼接，实测性能有一定提升，C++ 中对整型使用了 `push_back('0' + cnt)`, 容易证明 `cnt` 不会超过3，因为若出现`1111`，则逆向可得两个连续的1，而根据规则应为`21`，其他如`2222`推理方法类似。Java 中使用 StringBuilder 更为合适。除了通常方法外还可以使用正则表达式这一利器！

### 复杂度分析

略，与选用的数据结构有关。

## 题解2 - 递归

注意递归终止条件即可，核心过程差不多。

### Python

```python
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 0:
            return ''
        if n == 1:
            return '1'
        seq = self.countAndSay(n - 1)
        next_seq = ''
        cnt = 1
        for i in range(len(seq)):
            if i + 1 < len(seq) and seq[i] == seq[i + 1]:
                cnt += 1
            else:
                next_seq += str(cnt)
                next_seq += seq[i]
                cnt = 1

        return next_seq
```

### C++

``` c++
class Solution {
public:
    string countAndSay(int n) {
        if (n <= 0) return "";
        if (n == 1) return "1";

        string seq = countAndSay(n - 1);
        string next_seq = "";
        int cnt = 1;
        for (int i = 0; i < seq.length(); i++) {
            if (i + 1 < seq.length() && seq[i] == seq[i + 1]) {
                cnt++;
            } else {
                next_seq.push_back('0' + cnt);
                next_seq.push_back(seq[i]);
                cnt = 1;
            }
        }

        return next_seq;
    }
};
```

### Java

```java
public class Solution {
    public String countAndSay(int n) {
        assert n > 0;
        if (n == 1) return "1";

        String seq = countAndSay(n - 1);
        StringBuilder nextSeq = new StringBuilder();
        int cnt = 1;
        for (int i = 0; i < seq.length(); i++) {
            if (i + 1 < seq.length() && seq.charAt(i) == seq.charAt(i + 1)) {
                cnt++;
            } else {
                nextSeq.append(cnt).append(seq.charAt(i));
                cnt = 1;
            }
        }

        return nextSeq.toString();
    }
}
```

### 源码分析

判断相邻字符是否相同时需要判断索引是否越界。

### 复杂度分析

略，与选用的数据结构有关。

## Reference

- [4-5 lines Python solutions](https://discuss.leetcode.com/topic/32023/4-5-lines-python-solutions)