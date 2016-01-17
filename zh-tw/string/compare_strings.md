# Compare Strings

## Question

- lintcode: [(55) Compare Strings](http://www.lintcode.com/en/problem/compare-strings/)

```
Compare two strings A and B, determine whether A contains all of the characters in B.

The characters in string A and B are all Upper Case letters.

Example
For A = "ABCD", B = "ABC", return true.

For A = "ABCD" B = "AABC", return false.
```

## 題解

題 [Two Strings Are Anagrams | Data Structure and Algorithm](http://algorithm.yuanbin.zh-hans/string/two_strings_are_anagrams.html) 的變形題。題目意思是問B中的所有字元是否都在A中，而不是單個字元。比如B="AABC"包含兩個「A」，而A="ABCD"只包含一個「A」，故返回false. 做題時注意題意，必要時可向面試官確認。

既然不是類似 strstr 那樣的匹配，直接使用二重循環就不太合適了。題目中另外給的條件則是A和B都是全大寫單字，理解題意後容易想到的方案就是先遍歷 A 和 B 統計各字元出現的次數，然後比較次數大小即可。嗯，祭出萬能的哈希表。

### C++

```c++
class Solution {
public:
    /**
     * @param A: A string includes Upper Case letters
     * @param B: A string includes Upper Case letter
     * @return:  if string A contains all of the characters in B return true
     *           else return false
     */
    bool compareStrings(string A, string B) {
        if (A.size() < B.size()) {
            return false;
        }

        const int AlphabetNum = 26;
        int letterCount[AlphabetNum] = {0};
        for (int i = 0; i != A.size(); ++i) {
            ++letterCount[A[i] - 'A'];
        }
        for (int i = 0; i != B.size(); ++i) {
            --letterCount[B[i] - 'A'];
            if (letterCount[B[i] - 'A'] < 0) {
                return false;
            }
        }

        return true;
    }
};
```

### 源碼解析

1. 異常處理，B 的長度大於 A 時必定返回`false`, 包含了空串的特殊情況。
2. 使用額外的輔助空間，統計各字元的頻次。

### 複雜度分析

遍歷一次 A 字串，遍歷一次 B 字串，時間複雜度最壞 $$O(2n)$$, 空間複雜度為 $$O(26)$$.
