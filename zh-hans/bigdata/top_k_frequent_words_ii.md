---
difficulty: Hard
tags:
- Heap
- Data Structure Design
- Hash Table
title: Top K Frequent Words II
---

# Top K Frequent Words II

## Problem

### Metadata

- tags: Heap, Data Structure Design, Hash Table
- difficulty: Hard
- source(lintcode): <https://www.lintcode.com/problem/top-k-frequent-words-ii/>

### Description

Find top *k* frequent words in realtime data stream.

Implement three methods for *Topk* Class:

1. `TopK(k)`. The constructor.
2. `add(word)`. Add a new word.
3. `topk()`. Get the current top *k* frequent words.

#### Notice

If two words have the same frequency, rank them by alphabet.

#### Example

```
TopK(2)
add("lint")
add("code")
add("code")
topk()
>> ["code", "lint"]
```

## 题解

此题较难，实际上和 Redis 的有序集合类似，综合使用字典和排序集合可完美解决。

### Java

```java
public class TopK {
    private int k;
    private Map<String, Integer> wordFreq = null;
    private TreeSet<String> topkSet = null;

    class TopkComparator implements Comparator<String> {
        public int compare(String s1, String s2) {
            int s1Freq = wordFreq.get(s1), s2Freq = wordFreq.get(s2);
            if (s1Freq != s2Freq) {
                return s2Freq - s1Freq;
            } else {
                return s1.compareTo(s2);
            }
        }
    }

    /*
    * @param k: An integer
    */public TopK(int k) {
        // do intialization if necessary
        this.k = k;
        wordFreq = new HashMap<String, Integer>(k);
        topkSet = new TreeSet<String>(new TopkComparator());
    }

    /*
     * @param word: A string
     * @return: nothing
     */
    public void add(String word) {
        // write your code here
        if (wordFreq.containsKey(word)) {
            if (topkSet.contains(word)) {
                topkSet.remove(word);
            }
            wordFreq.put(word, wordFreq.get(word) + 1);
        } else {
            wordFreq.put(word, 1);
        }

        topkSet.add(word);
        if (topkSet.size() > k) {
            topkSet.pollLast();
        }
    }

    /*
     * @return: the current top k frequent words.
     */
    public List<String> topk() {
        // write your code here
        List<String> result = new ArrayList<String>(k);
        Iterator<String> it = topkSet.iterator();
        while (it.hasNext()) {
            result.add(it.next());
        }

        return result;
    }
}
```

### 源码分析

略

### 复杂度分析

待续