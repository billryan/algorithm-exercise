# Word Ladder

## Question

- leetcode: [Word Ladder | LeetCode OJ](https://leetcode.com/problems/word-ladder/)
- lintcode: [(120) Word Ladder](http://www.lintcode.com/en/problem/word-ladder/)

### Problem Statement

Given two words (_start_ and _end_), and a dictionary, find the length of
shortest transformation sequence from _start_ to _end_, such that:

  1. Only one letter can be changed at a time
  2. Each intermediate word must exist in the dictionary

#### Example

Given:
_start_ = `"hit"`
_end_ = `"cog"`
_dict_ = `["hot","dot","dog","lot","log"]`

As one shortest transformation is `"hit" -> "hot" -> "dot" -> "dog" -> "cog"`,
return its length `5`.

#### Note

  * Return 0 if there is no such transformation sequence.
  * All words have the same length.
  * All words contain only lowercase alphabetic characters.

## 题解

咋一看还以为是 Edit Distance 的变体，仔细审题后发现和动态规划没啥关系。题中有两大关键点：一次只能改动一个字符；改动的中间结果必须出现在词典中。那么大概总结下来共有四种情形：

1. start 和 end 相等。
2. end 在 dict 中，且 start 可以转换为 dict 中的一个单词。
3. end 不在 dict 中，但可由 start 或者 dict 中的一个单词转化而来。
4. end 无法由 start 转化而来。

由于中间结果也必须出现在词典中，故此题相当于图搜索问题，将 start, end, dict 中的单词看做图中的节点，节点与节点（单词与单词）可通过一步转化得到，可以转换得到的节点相当于边的两个节点，边的权重为1（都是通过1步转化）。到这里问题就比较明确了，相当于搜索从 start 到 end 两点间的最短距离，即 Dijkstra 最短路径算法。**通过 BFS 和哈希表实现。**

首先将 start 入队，随后弹出该节点，比较其和 end 是否相同；再从 dict 中选出所有距离为1的单词入队，并将所有与当前节点距离为1且未访问过的节点（需要使用哈希表）入队，方便下一层遍历时使用，直至队列为空。

### Java

```java
public class Solution {
    /**
      * @param start, a string
      * @param end, a string
      * @param dict, a set of string
      * @return an integer
      */
    public int ladderLength(String start, String end, Set<String> dict) {
        if (start == null && end == null) return 0;
        if (start.length() == 0 && end.length() == 0) return 0;
        assert(start.length() == end.length());
        if (dict == null || dict.size() == 0) {
            return 0;
        }

        int ladderLen = 1;
        dict.add(end); // add end to dict, important!
        Queue<String> q = new LinkedList<String>();
        Set<String> hash = new HashSet<String>();
        q.offer(start);
        hash.add(start);
        while (!q.isEmpty()) {
            ladderLen++;
            int qLen = q.size();
            for (int i = 0; i < qLen; i++) {
                String strTemp = q.poll();

                for (String nextWord : getNextWords(strTemp, dict)) {
                    if (nextWord.equals(end)) return ladderLen;
                    // filter visited word in the dict
                    if (hash.contains(nextWord)) continue;
                    q.offer(nextWord);
                    hash.add(nextWord);
                }
            }
        }

        return 0;
    }

    private Set<String> getNextWords(String curr, Set<String> dict) {
        Set<String> nextWords = new HashSet<String>();
        for (int i = 0; i < curr.length(); i++) {
            char[] chars = curr.toCharArray();
            for (char c = 'a'; c <= 'z'; c++) {
                chars[i] = c;
                String temp = new String(chars);
                if (dict.contains(temp)) {
                    nextWords.add(temp);
                }
            }
        }

        return nextWords;
    }
}
```

### 源码分析

#### `getNextWords`的实现

首先分析给定单词`curr`并从 dict 中选出所有距离为1 的单词。常规的思路可能是将`curr`与 dict 中的单词逐个比较，并遍历每个字符串，返回距离为1的单词组。这种找距离为1的节点的方法复杂度为 $$l(length\ of\ word) \times n(size\ of\ dict)\times m(queue\ length) = O(lmn)$$. 在 dict 较长时会 TLE. 其实根据 dict 的数据结构特点，比如查找任一元素的时间复杂度可认为是 $$O(1)$$. 根据哈希表和单个单词长度通常不会太长这一特点，我们就可以根据给定单词构造到其距离为一的单词变体，然后查询其是否在 dict 中，这种实现的时间复杂度为 $$O(26(a\ to\ z) \times l \times m) = O(lm)$$, 与 dict 长度没有太大关系，大大优化了时间复杂度。

经验教训：根据给定数据结构特征选用合适的实现，遇到哈希表时多用其查找的 $$O(1)$$ 特性。

#### BFS 和哈希表的配合使用

BFS 用作搜索，哈希表用于记录已经访问节点。在可以改变输入数据的前提下，需要将 end 加入 dict 中，否则对于不在 dict 中出现的 end 会有问题。

### 复杂度分析

主要在于`getNextWords`方法的时间复杂度，时间复杂度 $$O(lmn)$$。使用了队列存储中间处理节点，空间复杂度平均条件下应该是常量级别，当然最坏条件下可能恶化为 $$O(n)$$, 即 dict 中某个点与其他点距离均为1.

## Reference

- [Word Ladder 参考程序 Java/C++/Python](http://www.jiuzhang.com/solutions/word-ladder/)
- [Java Solution using Dijkstra's algorithm, with explanation - Leetcode Discuss](https://leetcode.com/discuss/50930/java-solution-using-dijkstras-algorithm-with-explanation)
