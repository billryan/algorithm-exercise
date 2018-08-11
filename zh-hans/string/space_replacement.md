# Space Replacement

Tags: String, Cracking The Coding Interview, Easy

## Question

- lintcode: [Space Replacement](http://www.lintcode.com/en/problem/space-replacement/)

### Problem Statement

Write a method to replace all spaces in a string with `%20`. The string is
given in a characters array, you can assume it has enough space for
replacement and you are given the true length of the string.

You code should also return the new length of the string after replacement.

##### Notice

If you are using Java or Python，please use characters array instead of string.

**Example**

Given `"Mr John Smith"`, length = `13`.

The string after replacement should be `"Mr%20John%20Smith"`, you need to
change the string in-place and return the new length `17`.

**Challenge**

Do it in-place.


## 题解

根据题意，给定的输入数组长度足够长，将空格替换为`%20` 后也不会溢出。通常的思维为从前向后遍历，遇到空格即将`%20` 插入到新数组中，这种方法在生成新数组时很直观，但要求原地替换时就不方便了，这时可联想到插入排序的做法——从后往前遍历，空格处标记下就好了。由于不知道新数组的长度，故首先需要遍历一次原数组，字符串类题中常用方法。

需要注意的是这个题并未说明多个空格如何处理，如果多个连续空格也当做一个空格时稍有不同。

### C++

``` c++
int replaceBlank(char string[], int length) {
	int n = 0;
	for (int i=0; i<length; i++)
		if (string[i] == ' ') n++;
	   
	int new_len = length + n*2;
	for (int i=length-1; i>=0; i--) {
		if (string[i] != ' ') {
			string[--new_len] = string[i];
		} else {
			string[--new_len] = '0';
			string[--new_len] = '2';
			string[--new_len] = '%';
		}
	}
	return length + n*2;
}
```


### Java

```java
public class Solution {
    /**
     * @param string: An array of Char
     * @param length: The true length of the string
     * @return: The true length of new string
     */
    public int replaceBlank(char[] string, int length) {
        if (string == null) return 0;
        
        int space_cnt = 0;
        for (int i = 0; i < length; i++) {
            if (string[i] == ' ') {
                space_cnt++;
            }
        }
        final int new_length = 2*space_cnt + length;

        int right = new_length - 1;
        for (int i = length - 1; i >= 0; i--) {
            if (string[i] == ' ') {
                string[right--] = '0';
                string[right--] = '2';
                string[right--] = '%';
            } else {
                string[right--] = string[i];
            }
        }

        return new_length;
    }
}
```

### 源码分析

先遍历一遍求得空格数，得到『新数组』的实际长度，从后往前遍历。

### 复杂度分析

遍历两次原数组，时间复杂度近似为 $$O(n)$$, 使用了`right` 作为标记，空间复杂度 $$O(1)$$.
