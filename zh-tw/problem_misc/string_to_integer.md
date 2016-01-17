# String to Integer

## Question

- leetcode: [String to Integer (atoi) | LeetCode OJ](https://leetcode.com/problems/string-to-integer-atoi/)
- lintcode: [(54) String to Integer(atoi)](http://www.lintcode.com/en/problem/string-to-integeratoi/)

```
Implement function atoi to convert a string to an integer.

If no valid conversion could be performed, a zero value is returned.

If the correct value is out of the range of representable values,
INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.

Example
"10" => 10

"-1" => -1

"123123123123123" => 2147483647

"1.0" => 1
```

## 題解

經典的字符串轉整數題，邊界條件比較多，比如是否需要考慮小數點，空白及非法字符的處理，正負號的處理，科學計數法等。最先處理的是空白字符，然後是正負號，接下來只要出現非法字符(包含正負號，小數點等，無需對這兩類單獨處理)即退出，否則按照正負號的整數進位加法處理。

### Java

```java
public class Solution {
    /**
     * @param str: A string
     * @return An integer
     */
    public int atoi(String str) {
        if (str == null || str.length() == 0) return 0;

        // trim left and right spaces
        String strTrim = str.trim();
        int len = strTrim.length();
        // sign symbol for positive and negative
        int sign = 1;
        // index for iteration
        int i = 0;
        if (strTrim.charAt(i) == '+') {
            i++;
        } else if (strTrim.charAt(i) == '-') {
            sign = -1;
            i++;
        }

        // store the result as long to avoid overflow
        long result = 0;
        while (i < len) {
            if (strTrim.charAt(i) < '0' || strTrim.charAt(i) > '9') {
                break;
            }
            result = 10 * result + sign * (strTrim.charAt(i) - '0');
            // overflow
            if (result > Integer.MAX_VALUE) {
                return Integer.MAX_VALUE;
            } else if (result < Integer.MIN_VALUE) {
                return Integer.MIN_VALUE;
            }
            i++;
        }

        return (int)result;
    }
}
```

### 源碼分析

符號位使用整數型表示，便於後期相乘相加。在 while 循環中需要注意判斷是否已經溢位，如果放在 while 循環外面則有可能超過 long 型範圍。


### C++
```c++
class Solution {
public:
    bool overflow(string str, string help){
        if(str.size() > help.size()) return true;
        else if(str.size() < help.size()) return false;
        for(int i = 0; i < str.size(); i++){
            if(str[i] > help[i]) return true;
            else if(str[i] < help[i]) return false;
        }
        return false;
    }
    int myAtoi(string str) {
        // ans: number, sign: +1 or -1
        int ans = 0;
        int sign = 1;
        int i = 0;
        int N = str.size();
        
        // eliminate spaces
        while(i < N){
            if(isspace(str[i]))
                i++;
            else
                break;
        }
        
        // if the whole string contains only spaces, return
        if(i == N) return ans;
        
        
        if(str[i] == '+') 
            i++;
        else if(str[i] == '-'){
            sign = -1;
            i++;
        }
        
        // "help" gets the string of valid numbers
        string help;
        while(i < N){
            if('0' <= str[i] and str[i] <= '9')
                help += str[i++];
            else
                break;
        }
        
        const string maxINT = "2147483647";
        const string minINT = "2147483648";
        
        // test whether overflow, test only number parts with both signs
        
        if(sign == 1){
            if(overflow(help, maxINT)) return INT_MAX;
        }
        else{
            if(overflow(help, minINT)) return INT_MIN;
        }
        
        for(int j=0; j<help.size(); j++){
            ans = 10 * ans + int(help[j] - '0');
        }
        
        return ans*sign;
    }
};
```

### 源碼分析
C++解法並沒有假設任何內建的string演算法，因此也適合使用在純C語言的字元陣列上，此外溢位的判斷直接使用字串用一個輔助函數比大小，這樣如果面試官要求改成string to long 也有辦法應付，不過此方法會變成machine-dependent，嚴格來說還需要寫一個輔助小函數把`INT_MAX`和`INT_MIN`轉換成字串來使用，這邊就先省略了，有興趣的同學可以自己嘗試練習。


### 複雜度分析

略

## Reference

- [String to Integer (atoi) 參考程序 Java/C++/Python](http://www.jiuzhang.com/solutions/string-to-integer-atoi/)
