---
difficulty: Medium
tags:
- Big Data
- Map Reduce
- EditorsChoice
title: Top K Frequent Words (Map Reduce)
---

# Top K Frequent Words (Map Reduce)

## Problem

### Metadata

- tags: Big Data, Map Reduce, EditorsChoice
- difficulty: Medium
- source(lintcode): <https://www.lintcode.com/problem/top-k-frequent-words-map-reduce/>

### Description

Find top k frequent words with map reduce framework.

The mapper's key is the document id, value is the content of the document, words in a document are split by spaces.

For reducer, the output should be at most k key-value pairs, which are the top k words and their frequencies in this reducer. The judge will take care about how to merge different reducers' results to get the global top k frequent words, so you don't need to care about that part.

The *k* is given in the constructor of TopK class.

#### Notice

For the words with same frequency, rank them with alphabet.

#### Example

Given document A = 
```
lintcode is the best online judge
I love lintcode
```
and document B = 
```
lintcode is an online judge for coding interview
you can test your code online at lintcode
```

The top 2 words and their frequencies should be
```
lintcode, 4
online, 3
```

## 题解

使用 Map Reduce 来做 Top K, 相比传统的 Top K 多了 Map 和 Reduce 这两大步骤。Map Reduce 模型实际上是在处理分布式问题时总结出的抽象模型，主要分为 Map 和 Reduce 两个阶段。

- Map 阶段：数据分片，每个分片由一个 Map task 处理，不进行分片则无法分布式处理
- Reduce 阶段：并行对前一阶段的结果进行规约处理并得到最终最终结果

实际的 MapReduce 编程模型可由以下5个分布式步骤组成：

1. 将输入数据解析为 `<key, value>` 对
2. 将输入的 `<key, value>` map 为另一种 `<key, value>`
3. 根据 key 对 map 阶段的数据分组
4. 对上一阶段的分组数据进行规约(Reduce) 并生成新的 `<key, value>`
5. 进一步处理 Reduce 阶段的数据并进行持久化

根据题意，我们只需要实现 Map, Reduce 这两个步骤即可，输出出现频率最高的 K 个单词并对相同频率的单词按照字典序排列。如果我们使用大根堆维护，那么我们可以在输出结果时依次移除根节点即可。这种方法虽然可行，但不可避免会产生不少空间浪费，理想情况下，我们仅需要维护 K 个大小的堆即可。所以接下来的问题便是我们怎么更好地维护这种 K 大小的堆，并且在新增元素时剔除的是最末尾(最小)的节点。

### Java

```java
/**
 * Definition of OutputCollector:
 * class OutputCollector<K, V> {
 *     public void collect(K key, V value);
 *         // Adds a key/value pair to the output buffer
 * }
 * Definition of Document:
 * class Document {
 *     public int id;
 *     public String content;
 * }
 */

class KeyFreq implements Comparable<KeyFreq> {
    public String key = null;
    public int freq = 0;

    public KeyFreq(String key, int freq) {
        this.key = key;
        this.freq = freq;
    }

    @Override
    public int compareTo(KeyFreq kf) {
        if (kf.freq != this.freq) {
            return this.freq - kf.freq;
        }

        // keep small alphabet
        return kf.key.compareTo(this.key);
    }
}

public class TopKFrequentWords {

    public static class Map {
        public void map(String _, Document value,
                        OutputCollector<String, Integer> output) {
            // Write your code here
            // Output the results into output buffer.
            // Ps. output.collect(String key, int value);
            if (value == null || value.content == null) return;

            String[] splits = value.content.split(" ");
            for (String split : splits) {
                if (split.length() > 0) {
                    output.collect(split, 1);
                }
            }
        }
    }

    public static class Reduce {

        private int k = 0;
        private PriorityQueue<KeyFreq> pq = null;

        public void setup(int k) {
            // initialize your data structure here
            this.k = k;
            pq = new PriorityQueue<KeyFreq>(k);
        }

        public void reduce(String key, Iterator<Integer> values) {
            int sum = 0;
            while (values.hasNext()) {
                int value = values.next();
                sum += value;
            }

            KeyFreq kf = new KeyFreq(key, sum);

            if (pq.size() < k) {
                pq.offer(kf);
            } else {
                KeyFreq peekKf = pq.peek();
                if (peekKf.compareTo(kf) <= 0) {
                    pq.poll();
                    pq.offer(kf);
                }
            }
        }

        public void cleanup(OutputCollector<String, Integer> output) {
            // Output the top k pairs <word, times> into output buffer.
            // Ps. output.collect(String key, Integer value);

            List<KeyFreq> kfList = new ArrayList<KeyFreq>(k);
            for (int i = 0; i < k && (!pq.isEmpty()); i++) {
                kfList.add(pq.poll());
            }

            // get max k from min-heapqueue
            int kfLen = kfList.size();
            for (int i = 0; i < kfLen; i++) {
                KeyFreq kf = kfList.get(kfLen - i - 1);
                output.collect(kf.key, kf.freq);
            }
        }
    }
}
```

### 源码分析

使用 Java 自带的 PriorityQueue 来实现堆，由于需要定制大小比较，所以这里自定义类中实现了 `Comparable` 的 `compareTo` 接口，另外需要注意的是这里原生使用了小根堆，所以我们在覆写 `compareTo` 时需要注意字符串的比较，相同频率的按照字典序排序，即优先保留字典序较小的字符串，所以正好和 freq 的比较相反。最后再输出答案时，由于是小根堆，所以还需要再转置一次。此题的 Java 实现中，使用的 PriorityQueue 并非线程安全，实际使用中需要注意是否需要用到线程安全的 PriorityBlockingQueue

对于 Java, 虽然标准库中暂未有定长的 PriorityQueue 实现，但是我们常用的 Google guava 库中其实已有类似实现，见 [MinMaxPriorityQueue](https://google.github.io/guava/releases/snapshot/api/docs/com/google/common/collect/MinMaxPriorityQueue.html) 不必再自己造轮子了。

### 复杂度分析

堆的插入删除操作，定长为 K, n 个元素，故时间复杂度约 $$O(n \log K)$$, 空间复杂度为 $$O(n)$$.

## Reference

- 《大数据技术体系详解》——董西成，MapReduce 编程模型
- [九章算法 - topk-mapreduce](https://www.jiuzhang.com/solution/top-k-frequent-words-map-reduce/)