---
difficulty: Medium
tags:
- Pocket Gems
- Hash Table
- Amazon
- Priority Queue
- Bloomberg
- Yelp
- Heap
- Uber
- EditorsChoice
title: Top K Frequent Words
---

# Top K Frequent Words

## Problem

### Metadata

- tags: Pocket Gems, Hash Table, Amazon, Priority Queue, Bloomberg, Yelp, Heap, Uber, EditorsChoice
- difficulty: Medium
- source(lintcode): <https://www.lintcode.com/problem/top-k-frequent-words/>
- source(leetcode): <https://leetcode.com/problems/top-k-frequent-words/>

### Description

Given a list of words and an integer k, return the top k frequent words in the list.

#### Notice

You should order the words by the frequency of them in the return list, the most frequent one comes first. If two words has the same frequency, the one with lower alphabetical order come first.

#### Example

Given

    [
        "yes", "lint", "code",
        "yes", "code", "baby",
        "you", "baby", "chrome",
        "safari", "lint", "code",
        "body", "lint", "code"
    ]

for k = `3`, return `["code", "lint", "baby"]`.

for k = `4`, return `["code", "lint", "baby", "yes"]`,

#### Challenge

Do it in O(nlogk) time and O(n) extra space.

## 题解

输出出现频率最高的 K 个单词并对相同频率的单词按照字典序排列。如果我们使用大根堆维护，那么我们可以在输出结果时依次移除根节点即可。这种方法虽然可行，但不可避免会产生不少空间浪费，理想情况下，我们仅需要维护 K 个大小的堆即可。所以接下来的问题便是我们怎么更好地维护这种 K 大小的堆，并且在新增元素时剔除的是最末尾(最小)的节点。

### Java

```java
public class Solution {
    /**
     * @param words: an array of string
     * @param k: An integer
     * @return: an array of string
     */
    public String[] topKFrequentWords(String[] words, int k) {
        // write your code here
        if (words == null || words.length == 0) return words;
        if (k <= 0) return new String[0];

        Map<String, Integer> wordFreq = new HashMap<>();
        for (String word : words) {
            wordFreq.putIfAbsent(word, 0);
            wordFreq.put(word, wordFreq.get(word) + 1);
        }

        PriorityQueue<KeyFreq> pq = new PriorityQueue<KeyFreq>(k);
        for (Map.Entry<String, Integer> entry : wordFreq.entrySet()) {
            KeyFreq kf = new KeyFreq(entry.getKey(), entry.getValue());
            if (pq.size() < k) {
                pq.offer(kf);
            } else {
                KeyFreq peek = pq.peek();
                if (peek.compareTo(kf) <= 0) {
                    pq.poll();
                    pq.offer(kf);
                }
            }
        }

        int topKSize = Math.min(k, pq.size());
        String[] topK = new String[topKSize];
        for (int i = 0; i < k && !pq.isEmpty(); i++) {
            topK[i] = pq.poll().key;
        }

        // reverse array
        for (int i = 0, j = topKSize - 1; i < j; i++, j--) {
            String temp = topK[i];
            topK[i] = topK[j];
            topK[j] = temp;
        }

        return topK;
    }

    class KeyFreq implements Comparable<KeyFreq> {
        String key;
        int freq;
        
        public KeyFreq(String key, int freq) {
            this.key = key;
            this.freq = freq;
        }

        @Override
        public int compareTo(KeyFreq kf) {
            if (this.freq != kf.freq) {
                return this.freq - kf.freq;
            }

            return kf.key.compareTo(this.key);
        }
    }
}
```


### 源码分析

使用 Java 自带的 PriorityQueue 来实现堆，由于需要定制大小比较，所以这里自定义类中实现了 `Comparable` 的 `compareTo` 接口，另外需要注意的是这里原生使用了小根堆，所以我们在覆写 `compareTo` 时需要注意字符串的比较，相同频率的按照字典序排序，即优先保留字典序较小的字符串，所以正好和 freq 的比较相反。最后再输出答案时，由于是小根堆，所以还需要再转置一次。此题的 Java 实现中，使用的 PriorityQueue 并非线程安全，实际使用中需要注意是否需要用到线程安全的 PriorityBlockingQueue

对于 Java, 虽然标准库中暂未有定长的 PriorityQueue 实现，但是我们常用的 Google guava 库中其实已有类似实现，见 [MinMaxPriorityQueue](https://google.github.io/guava/releases/snapshot/api/docs/com/google/common/collect/MinMaxPriorityQueue.html) 不必再自己造轮子了。

### 复杂度分析

堆的插入删除操作，定长为 K, n 个元素，故时间复杂度约 $$O(n \log K)$$, 空间复杂度为 $$O(n)$$.