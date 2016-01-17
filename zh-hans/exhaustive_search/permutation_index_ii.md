# Permutation Index II

## Question

- lintcode: [(198) Permutation Index II](http://www.lintcode.com/en/problem/permutation-index-ii/)

### Problem Statement

Given a permutation which may contain repeated numbers, find its index in all
the permutations of these numbers, which are ordered in lexicographical order.
The index begins at 1.

#### Example

Given the permutation `[1, 4, 2, 2]`, return `3`.

## 题解

题 [Permutation Index](http://algorithm.yuanbin.me/zh-hans/exhaustive_search/permutation_index.html) 的扩展，这里需要考虑重复元素，有无重复元素最大的区别在于原来的`1!, 2!, 3!...`等需要除以重复元素个数的阶乘，颇有点高中排列组合题的味道。记录重复元素个数同样需要动态更新，引入哈希表这个万能的工具较为方便。

### Python

```python
class Solution:
    # @param {int[]} A an integer array
    # @return {long} a long integer
    def permutationIndexII(self, A):
        if A is None or len(A) == 0:
            return 0

        index = 1
        factor = 1
        for i in xrange(len(A) - 1, -1, -1):
            hash_map = {A[i]: 1}
            rank = 0
            for j in xrange(i + 1, len(A)):
                if A[j] in hash_map.keys():
                    hash_map[A[j]] += 1
                else:
                    hash_map[A[j]] = 1
                # get rank
                if A[i] > A[j]:
                    rank += 1

            index += rank * factor / self.dupPerm(hash_map)
            factor *= (len(A) - i)

        return index


    def dupPerm(self, hash_map):
        if hash_map is None or len(hash_map) == 0:
            return 0
        dup = 1
        for val in hash_map.values():
            dup *= self.factorial(val)

        return dup


    def factorial(self, n):
        r = 1
        for i in xrange(1, n + 1):
            r *= i

        return r
```

### C++

```c++
class Solution {
public:
    /**
     * @param A an integer array
     * @return a long integer
     */
    long long permutationIndexII(vector<int>& A) {
        if (A.empty()) return 0;

        long long index = 1;
        long long factor = 1;
        for (int i = A.size() - 1; i >= 0; --i) {
            int rank = 0;
            unordered_map<int, int> hash;
            ++hash[A[i]];
            for (int j = i + 1; j < A.size(); ++j) {
                ++hash[A[j]];

                if (A[i] > A[j]) {
                    ++rank;
                }
            }
            index += rank * factor / dupPerm(hash);
            factor *= (A.size() - i);
        }

        return index;
    }

private:
    long long dupPerm(unordered_map<int, int> hash) {
        if (hash.empty()) return 1;

        long long dup = 1;
        for (auto it = hash.begin(); it != hash.end(); ++it) {
            dup *= fact(it->second);
        }

        return dup;
    }

    long long fact(int num) {
        long long val = 1;
        for (int i = 1; i <= num; ++i) {
            val *= i;
        }

        return val;
    }
};
```

### Java

```java
public class Solution {
    /**
     * @param A an integer array
     * @return a long integer
     */
    public long permutationIndexII(int[] A) {
        if (A == null || A.length == 0) return 0L;

        Map<Integer, Integer> hashmap = new HashMap<Integer, Integer>();
        long index = 1, fact = 1, multiFact = 1;
        for (int i = A.length - 1; i >= 0; i--) {
            // collect its repeated times and update multiFact
            if (hashmap.containsKey(A[i])) {
                hashmap.put(A[i], hashmap.get(A[i]) + 1);
                multiFact *= hashmap.get(A[i]);
            } else {
                hashmap.put(A[i], 1);
            }
            // get rank every turns
            int rank = 0;
            for (int j = i + 1; j < A.length; j++) {
                if (A[i] > A[j]) rank++;
            }
            // do divide by multiFact
            index += rank * fact / multiFact;
            fact *= (A.length - i);
        }

        return index;
    }
}
```

### 源码分析

在计算重复元素个数的阶乘时需要注意更新`multiFact`的值即可，不必每次都去计算哈希表中的值。对元素`A[i]`需要加入哈希表 - `hash.put(A[i], 1);`，设想一下`2, 2, 1, 1`的计算即可知。

### 复杂度分析

双重 for 循环，时间复杂度为 $$O(n^2)$$, 使用了哈希表，空间复杂度为 $$O(n)$$.
