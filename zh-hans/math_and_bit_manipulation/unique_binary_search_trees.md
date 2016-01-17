# Unique Binary Search Trees

## Question

- leetcode: [Unique Binary Search Trees | LeetCode OJ](https://leetcode.com/problems/unique-binary-search-trees/)
- lintcode: [(163) Unique Binary Search Trees](http://www.lintcode.com/en/problem/unique-binary-search-trees/)

```
Given n, how many structurally unique BSTs (binary search trees)
that store values 1...n?

Example
Given n = 3, there are a total of 5 unique BST's.

1           3    3       2      1
 \         /    /       / \      \
  3      2     1       1   3      2
 /      /       \                  \
2     1          2                  3
```

## 题解1 - 两重循环

挺有意思的一道题，与数据结构和动态规划都有点关系。这两天在骑车路上和睡前都一直在想，始终未能找到非常明朗的突破口，直到看到这么一句话——『以i为根节点的树，其左子树由[0, i-1]构成， 其右子树由[i+1, n]构成。』这不就是 BST 的定义嘛！灵活运用下就能找到递推关系了。

容易想到这道题的动态规划状态为 count[n], count[n] 表示到正整数 i 为止的二叉搜索树个数。容易得到 count[1] = 1, 根节点为1，count[2] = 2, 根节点可为1或者2。那么 count[3] 的根节点自然可为1，2，3. 如果以1为根节点，那么根据 BST 的定义，2和3只可能位于根节点1的右边；如果以2为根节点，则1位于左子树，3位于右子树；如果以3为根节点，则1和2必位于3的左子树。

抽象一下，如果以 i 作为根节点，由基本的排列组合知识可知，其唯一 BST 个数为左子树的 BST 个数乘上右子树的 BST 个数。故对于 i 来说，其左子树由[0, i - 1]构成，唯一的 BST 个数为 count[i - 1], 右子树由[i + 1, n] 构成，其唯一的 BST 个数没有左子树直观，但是也有迹可循。对于两组有序数列「1, 2, 3] 和 [4, 5, 6]来说，**这两个有序数列分别组成的 BST 个数必然是一样的，因为 BST 的个数只与有序序列的大小有关，而与具体值没有关系。**所以右子树的 BST 个数为 count[n - i]，于是乎就得到了如下递推关系：
$$count[i] = \sum _{j = 0} ^{i - 1} (count[j] \cdot count[i - j - 1])$$

网上有很多用 count[3] 的例子来得到递推关系，恕本人愚笨，在没有从 BST 的定义和有序序列个数与 BST 关系分析的基础上，我是不敢轻易说就能得到如上状态转移关系的。

### Python

```python
class Solution:
    # @paramn n: An integer
    # @return: An integer
    def numTrees(self, n):
        if n < 0:
            return -1

        count = [0] * (n + 1)
        count[0] = 1
        for i in xrange(1, n + 1):
            for j in xrange(i):
                count[i] += count[j] * count[i - j - 1]

        return count[n]
```

### C++

```c++
class Solution {
public:
    /**
     * @paramn n: An integer
     * @return: An integer
     */
    int numTrees(int n) {
        if (n < 0) {
            return -1;
        }

        vector<int> count(n + 1);
        count[0] = 1;
        for (int i = 1; i != n + 1; ++i) {
            for (int j = 0; j != i; ++j) {
                count[i] += count[j] * count[i - j - 1];
            }
        }

        return count[n];
    }
};
```

### Java

```java
public class Solution {
    /**
     * @paramn n: An integer
     * @return: An integer
     */
    public int numTrees(int n) {
        if (n < 0) {
            return -1;
        }

        int[] count = new int[n + 1];
        count[0] = 1;
        for (int i = 1; i < n + 1; ++i) {
            for (int j = 0; j < i; ++j) {
                count[i] += count[j] * count[i - j - 1];
            }
        }

        return count[n];
    }
}
```

### 源码分析

1. 对 n 小于0特殊处理。
2. 初始化大小为 n + 1 的数组，初始值为0，但对 count[0] 赋值为1.
3. 两重 for 循环递推求得 count[i] 的值。
4. 返回 count[n] 的值。

由于需要处理空节点的子树，故初始化 count[0] 为1便于乘法处理。其他值必须初始化为0，因为涉及到累加操作。

### 复杂度分析

一维数组大小为 n + 1, 空间复杂度为 $$O(n + 1)$$. 两重 for 循环等差数列求和累计约 $$n^2 / 2$$, 故时间复杂度为 $$O(n^2)$$. 此题为 Catalan number 的一种，除了平方时间复杂度的解法外还存在 $$O(n)$$ 的解法，欲练此功，先戳 [Wikipedia](http://en.wikipedia.org/wiki/Catalan_number) 的链接。

## Reference

- [^fisherlei]: [水中的鱼: [LeetCode] Unique Binary Search Trees, Solution](http://fisherlei.blogspot.com/2013/03/leetcode-unique-binary-search-trees.html)
- [Unique Binary Search Trees | 九章算法](http://www.jiuzhang.com/solutions/unique-binary-search-trees/)
- [Catalan number - Wikipedia, the free encyclopedia](http://en.wikipedia.org/wiki/Catalan_number)
