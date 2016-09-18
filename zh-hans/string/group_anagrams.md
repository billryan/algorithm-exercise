# Group Anagrams

Tags: Hash Table, String, Medium

## Question

- leetcode: [Group Anagrams](https://leetcode.com/problems/anagrams/)
- lintcode: [Group Anagrams](http://www.lintcode.com/en/problem/anagrams/)

### Problem Statement

Given an array of strings, group anagrams together.

For example, given: `["eat", "tea", "tan", "ate", "nat", "bat"]`,  
Return:
    
    [
      ["ate", "eat","tea"],
      ["nat","tan"],
      ["bat"]
    ]

**Note:** All inputs will be in lower-case.

## 题解1 - 双重`for`循环(TLE)

题 [Two Strings Are Anagrams](../two_strings_are_anagrams.html) 的升级版，容易想到的方法为使用双重`for`循环两两判断字符串数组是否互为变位字符串。但显然此法的时间复杂度较高。还需要 $$O(n)$$ 的数组来记录字符串是否被加入到最终结果中。

### Python

```python
class Solution:
    # @param strs: A list of strings
    # @return: A list of strings
    # @return: A list of strings
    def anagrams(self, strs):

        if len(strs) < 2 :
            return strs
        result=[]
        visited=[False]*len(strs)
        for index1,s1 in enumerate(strs):
            hasAnagrams = False
            for index2,s2 in enumerate(strs):
                if index2 > index1 and not visited[index2] and self.isAnagrams(s1,s2):
                    result.append(s2)
                    visited[index2]=True
                    hasAnagrams = True
            if not visited[index1] and hasAnagrams:
                result.append(s1)
        return result

    def isAnagrams(self, str1, str2):
        if  sorted (str1) == sorted(str2):
                return True
        return False
```

### C++

```c++
class Solution {
public:
    /**
     * @param strs: A list of strings
     * @return: A list of strings
     */
    vector<string> anagrams(vector<string> &strs) {
        if (strs.size() < 2) {
            return strs;
        }

        vector<string> result;
        vector<bool> visited(strs.size(), false);
        for (int s1 = 0; s1 != strs.size(); ++s1) {
            bool has_anagrams = false;
            for (int s2 = s1 + 1; s2 < strs.size(); ++s2) {
                if ((!visited[s2]) && isAnagrams(strs[s1], strs[s2])) {
                    result.push_back(strs[s2]);
                    visited[s2] = true;
                    has_anagrams = true;
                }
            }
            if ((!visited[s1]) && has_anagrams) result.push_back(strs[s1]);
        }

        return result;
    }

private:
    bool isAnagrams(string &s, string &t) {
        if (s.size() != t.size()) {
            return false;
        }

        const int AlphabetNum = 26;
        int letterCount[AlphabetNum] = {0};
        for (int i = 0; i != s.size(); ++i) {
            ++letterCount[s[i] - 'a'];
            --letterCount[t[i] - 'a'];
        }
        for (int i = 0; i != t.size(); ++i) {
            if (letterCount[t[i] - 'a'] < 0) {
                return false;
            }
        }

        return true;
    }
};
```

### 源码分析

1. strs 长度小于等于1时直接返回。
2. 使用与 strs 等长的布尔数组表示其中的字符串是否被添加到最终的返回结果中。
3. 双重循环遍历字符串数组，注意去重即可。
4. 私有方法`isAnagrams`用于判断两个字符串是否互为变位词。

### 复杂度分析

私有方法`isAnagrams`最坏的时间复杂度为 $$O(2L)$$, 其中 $$L$$ 为字符串长度。双重`for`循环时间复杂度近似为 $$\frac {1}{2} O(n^2)$$, $$n$$ 为给定字符串数组数目。总的时间复杂度近似为 $$O(n^2 L)$$. 使用了Vector String "visited"，空间复杂度可认为是 $$O(n)$$.

## 题解2 - 排序 + hashmap

在题 [Two Strings Are Anagrams](http://algorithm.yuanbin.me/zh-hans/string/two_strings_are_anagrams.html) 中曾介绍过使用排序和 hashmap 两种方法判断变位词。这里我们将这两种方法同时引入！只不过此时的 hashmap 的 key 为字符串，value 为该字符串在 vector 中出现的次数。两次遍历字符串数组，第一次遍历求得排序后的字符串数量，第二次遍历将排序后相同的字符串取出放入最终结果中。

**leetcode 上此题的 signature 已经更新，需要将 anagrams 按组输出，稍微麻烦一点点。**

### Python lintcode

```python 
class Solution:
    # @param strs: A list of strings
    # @return: A list of strings
    # @return: A list of strings
    def anagrams(self, strs):
        strDict={}
        result=[]
        for string in strs:
            if  "".join(sorted(string)) not in strDict.keys():
                strDict["".join(sorted(string))] = 1
            else: 
                strDict["".join(sorted(string))] += 1
        for string in strs:
            if strDict["".join(sorted(string))] >1:
                result.append(string)
        return result
```


### C++ - lintcode

```c++
class Solution {
public:
    /**
     * @param strs: A list of strings
     * @return: A list of strings
     */
    vector<string> anagrams(vector<string> &strs) {
        unordered_map<string, int> hash;

        for (int i = 0; i < strs.size(); i++) {
            string str = strs[i];
            sort(str.begin(), str.end());
            ++hash[str];
        }

        vector<string> result;
        for (int i = 0; i < strs.size(); i++) {
            string str = strs[i];
            sort(str.begin(), str.end());
            if (hash[str] > 1) {
                result.push_back(strs[i]);
            }
        }

        return result;
    }
};
```

### Java - leetcode

```java
public class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> result = new ArrayList<List<String>>();
        if (strs == null) return result;
        
        // one key to multiple value multiMap
        Map<String, ArrayList<String>> multiMap = new HashMap<String, ArrayList<String>>();
        for (String str : strs) {
            char[] strChar = str.toCharArray();
            Arrays.sort(strChar);
            String strSorted = String.valueOf(strChar);
            if (multiMap.containsKey(strSorted)) {
                ArrayList<String> aList = multiMap.get(strSorted);
		        aList.add(str);
                multiMap.put(strSorted, aList);
            } else {
                ArrayList<String> aList = new ArrayList<String>();
                aList.add(str);
                multiMap.put(strSorted, aList);
            }
        }
        
        // add List group to result
        Set<String> keySet = multiMap.keySet();
        for (String key : keySet) {
            ArrayList<String> aList = multiMap.get(key);
            Collections.sort(aList);
            result.add(aList);
        }
        
        return result;
    }
}
```

### 源码分析

建立 key 为字符串，value 为相应计数器的hashmap, `unordered_map`为 C++ 11中引入的哈希表数据结构[^unordered_map], 这种新的数据结构和之前的 map 有所区别，详见[^map-unordered_map]。

第一次遍历字符串数组获得排序后的字符串计数器信息，第二次遍历字符串数组将哈希表中计数器值大于1的字符串取出。

leetcode 中题目 signature 已经有所变化，这里使用一对多的 HashMap 较为合适，使用 ArrayList<String> 作为 value. Java 中对 String 排序可先将其转换为 char[], 排序后再转换为新的 String.

### 复杂度分析

遍历一次字符串数组，复杂度为 $$O(n)$$, 对单个字符串排序复杂度近似为 $$O(L \log L)$$. 两次遍历字符串数组，故总的时间复杂度近似为 $$O(nL \log L)$$. 使用了哈希表，空间复杂度为 $$O(K)$$, 其中 K 为排序后不同的字符串个数。

## Reference

- [^unordered_map]: [unordered_map - C++ Reference](http://www.cplusplus.com/reference/unordered_map/unordered_map/)
- [^map-unordered_map]: [c++ - Choosing between std::map and std::unordered_map - Stack Overflow](http://stackoverflow.com/questions/3902644/choosing-between-stdmap-and-stdunordered-map)
- [Anagrams | 九章算法](http://www.jiuzhang.com/solutions/anagrams/)
