# Space Replacement

## Question

- lintcode: [(212) Space Replacement](http://www.lintcode.com/en/problem/space-replacement/)

```
Write a method to replace all spaces in a string with %20. 
The string is given in a characters array, you can assume it has enough space 
for replacement and you are given the true length of the string.

Example
Given "Mr John Smith", length = 13.

The string after replacement should be "Mr%20John%20Smith".

Note
If you are using Java or Python，please use characters array instead of string.

Challenge
Do it in-place.
```

## 題解

根據題意，給定的輸入陣列長度足夠長，將空格替換為`%20` 後也不會overflow。通常的思維為從前向後遍歷，遇到空格即將`%20` 插入到新陣列中，這種方法在生成新陣列時很直觀，但要求原地替換時就不方便了，這時可聯想到插入排序的做法——從後往前遍歷，空格處標記下就好了。由於不知道新陣列的長度，故首先需要遍歷一次原陣列，字符串類題中常用方法。

需要注意的是這個題並未說明多個空格如何處理，如果多個連續空格也當做一個空格時稍有不同。

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
        
        int space = 0;
        for (char c : string) {
            if (c == ' ') space++;
        }
        
        int r = length + 2 * space - 1;
        for (int i = length - 1; i >= 0; i--) {
            if (string[i] != ' ') {
                string[r] = string[i];
                r--;
            } else {
                string[r--] = '0';
                string[r--] = '2';
                string[r--] = '%';
            }
        }
        
        return length + 2 * space;
    }
}
```

```c++
class Solution {
public:
    /**
     * @param string: An array of Char
     * @param length: The true length of the string
     * @return: The true length of new string
     */
    int replaceBlank(char string[], int length) {
        int space = 0;
        for (int i = 0; i < length; i++) {
            if (string[i] == ' ') space++;
        }
        
        int r = length + 2 * space - 1;
        for (int i = length - 1; i >= 0; i--) {
            if (string[i] != ' ') {
                string[r] = string[i];
                r--;
            } else {
                string[r--] = '0';
                string[r--] = '2';
                string[r--] = '%';
            }
        }
        
        return length + 2 * space;
    }
};
```
    
### 源碼分析

先遍歷一遍求得空格數，得到『新陣列』的實際長度，從後往前遍歷。

### 複雜度分析

遍歷兩次原陣列，時間複雜度近似為 $$O(n)$$, 使用了`r` 作為標記，空間複雜度 $$O(1)$$.
