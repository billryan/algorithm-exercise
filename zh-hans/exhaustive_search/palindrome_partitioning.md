# Palindrome Partitioning

- tags: [palindrome]

## Question

- leetcode: [Palindrome Partitioning | LeetCode OJ](https://leetcode.com/problems/palindrome-partitioning/)
- lintcode: [(136) Palindrome Partitioning](http://www.lintcode.com/en/problem/palindrome-partitioning/)

```
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["aa","b"],
    ["a","a","b"]
  ]
```

## 题解1 - DFS

罗列所有可能，典型的 DFS. 此题要求所有可能的回文子串，即需要找出所有可能的分割，使得分割后的子串都为回文。凭借高中的排列组合知识可知这可以用『隔板法』来解决，具体就是在字符串的每个间隙为一个隔板，对于长度为 n 的字符串，共有 n-1 个隔板可用，每个隔板位置可以选择放或者不放，总共有 $$O(2^{n-1})$$ 种可能。由于需要满足『回文』条件，故实际上需要穷举的状态数小于 $$O(2^{n-1})$$.

回溯法看似不难，但是要活学活用起来还是不容易的，核心抓住两点：**深搜的递归建立和剪枝函数的处理。**

根据『隔板法』的思想，我们首先从第一个隔板开始挨个往后取，若取到的子串不是回文则立即取下一个隔板，直到取到最后一个隔板。若取到的子串是回文，则将当前子串加入临时列表中，接着从当前隔板处字符开始递归调用回溯函数，直至取到最后一个隔板，最后将临时列表中的子串加入到最终返回结果中。接下来则将临时列表中的结果一一移除，这个过程和 subsets 模板很像，代码比这个文字描述更为清晰。

### Python

```python
class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        result = []
        if not s:
            return result
        
        palindromes = []
        self.dfs(s, 0, palindromes, result)
        return result
    
    def dfs(self, s, pos, palindromes, ret):
        if pos == len(s):
            ret.append([] + palindromes)
            return
        
        for i in xrange(pos + 1, len(s) + 1):
            if not self.isPalindrome(s[pos:i]):
                continue
            
            palindromes.append(s[pos:i])
            self.dfs(s, i, palindromes, ret)
            palindromes.pop()
    
    def isPalindrome(self, s):
        if not s:
            return False
        # reverse compare
        return s == s[::-1]
```

### C++

```c++
class Solution {
public:
    /**
     * @param s: A string
     * @return: A list of lists of string
     */
    vector<vector<string>> partition(string s) {
        vector<vector<string> > result;
        if (s.empty()) return result;
        
        vector<string> palindromes;
        dfs(s, 0, palindromes, result);
        
        return result;
    }
    
private:
    void dfs(string s, int pos, vector<string> &palindromes, 
             vector<vector<string> > &ret) {
        
        if (pos == s.size()) {
            ret.push_back(palindromes);
            return;
        }
        
        for (int i = pos + 1; i <= s.size(); ++i) {
            string substr = s.substr(pos, i - pos);
            if (!isPalindrome(substr)) {
                continue;
            }
            
            palindromes.push_back(substr);
            dfs(s, i, palindromes, ret);
            palindromes.pop_back();
        }
    }
    
    bool isPalindrome(string s) {
        if (s.empty()) return false;
        
        int n = s.size();
        for (int i = 0; i < n; ++i) {
            if (s[i] != s[n - i - 1]) return false;
        }
        
        return true;
    }
};
```

### Java

```java
public class Solution {
    /**
     * @param s: A string
     * @return: A list of lists of string
     */
    public List<List<String>> partition(String s) {
        List<List<String>> result = new ArrayList<List<String>>();
        if (s == null || s.isEmpty()) return result;
        
        List<String> palindromes = new ArrayList<String>();
        dfs(s, 0, palindromes, result);
        
        return result;
    }
    
    private void dfs(String s, int pos, List<String> palindromes, 
                     List<List<String>> ret) {

        if (pos == s.length()) {
            ret.add(new ArrayList<String>(palindromes));
            return;
        }
        
        for (int i = pos + 1; i <= s.length(); i++) {
            String substr = s.substring(pos, i);
            if (!isPalindrome(substr)) {
                continue;
            }
            
            palindromes.add(substr);
            dfs(s, i, palindromes, ret);
            palindromes.remove(palindromes.size() - 1);
        }
    }
    
    private boolean isPalindrome(String s) {
        if (s == null || s.isEmpty()) return false;
        
        int n = s.length();
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) != s.charAt(n - i - 1)) return false;
        }
        
        return true;
    }
}
```

### 源码分析

回文的判断采用了简化的版本，没有考虑空格等非字母数字字符要求。Java 中 ArrayList 和 List 的实例化需要注意下。Python 中 result 的初始化为[], 不需要初始化为 [[]] 画蛇添足。C++ 中的`.substr(pos, n)` 含义为从索引为 pos 的位置往后取 n 个(含) 字符，注意与 Java 中区别开来。

### 复杂度分析

DFS，状态数最多 $$O(2^{n-1})$$, 故时间复杂度为 $$O(2^n)$$, 使用了临时列表，空间复杂度为 $$O(n)$$.

## Reference

- [Palindrome Partitioning 参考程序 Java/C++/Python](http://www.jiuzhang.com/solutions/palindrome-partitioning/)
- soulmachine 的 Palindrome Partitioning
