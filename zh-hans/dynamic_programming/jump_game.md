# Jump Game

## Question

- lintcode:

[(116) Jump Game](http://www.lintcode.com/en/problem/jump-game/)
```
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
```

## 题解(自顶向下-动态规划)

1. State: f[i] 从起点出发能否达到i
2. Function: `f[i] = OR (f[j], j < i ~\&\&~ j + A[j] \geq i)`, 状态 $$j$$ 转移到 $$i$$, 所有小于i的下标j的元素中是否存在能从j跳转到i得
3. Initialization: f[0] = true;
4. Answer: 递推到第 N - 1 个元素时，f[N-1]

这种自顶向下的方法需要使用额外的 $$O(n)$$ 空间，保存小于N-1时的状态。且时间复杂度在恶劣情况下有可能变为 $$1 + 2 + \cdots + n = O(n^2)$$, 出现 TLE 无法AC的情况，不过工作面试能给出这种动规的实现就挺好的了。

### C++ from top to bottom

```c++
class Solution {
public:
    /**
     * @param A: A list of integers
     * @return: The boolean answer
     */
    bool canJump(vector<int> A) {
        if (A.empty()) {
            return true;
        }

        vector<bool> jumpto(A.size(), false);
        jumpto[0] = true;

        for (int i = 1; i != A.size(); ++i) {
            for (int j = i - 1; j >= 0; --j) {
                if (jumpto[j] && (j + A[j] >= i)) {
                    jumpto[i] = true;
                    break;
                }
            }
        }

        return jumpto[A.size() - 1];
    }
};
```

## 题解(自底向上-贪心法)

题意为问是否能从起始位置到达最终位置，我们首先分析到达最终位置的条件，从坐标i出发所能到达最远的位置为 $$f[i] = i + A[i]$$，如果要到达最终位置，即存在某个 $$i$$ 使得$$f[i] \geq N - 1$$, 而想到达 $$i$$, 则又需存在某个 $$j$$ 使得 $$f[j] \geq i - 1$$. 依此类推直到下标为0.

**以下分析形式虽为动态规划，实则贪心法！**

1. State: f[i] 从 $$i$$ 出发能否到达最终位置
2. Function: $$f[j] = j + A[j] \geq i$$, 状态 $$j$$ 转移到 $$i$$, 置为`true`
3. Initialization: 第一个为`true`的元素为 `A.size() - 1`
4. Answer: 递推到第 0 个元素时，若其值为`true`返回`true`

### C++ greedy, from bottom to top

```c++
class Solution {
public:
    /**
     * @param A: A list of integers
     * @return: The boolean answer
     */
    bool canJump(vector<int> A) {
        if (A.empty()) {
            return true;
        }

        int index_true = A.size() - 1;
        for (int i = A.size() - 1; i >= 0; --i) {
            if (i + A[i] >= index_true) {
                index_true = i;
            }
        }

        return 0 == index_true ? true : false;
    }
};
```

## 题解(自顶向下-贪心法)

针对上述自顶向下可能出现时间复杂度过高的情况，下面使用贪心思想对i进行递推，每次遍历A中的一个元素时更新最远可能到达的元素，最后判断最远可能到达的元素是否大于 `A.size() - 1`

### C++ greedy, from top to bottom

```c++
class Solution {
public:
    /**
     * @param A: A list of integers
     * @return: The boolean answer
     */
    bool canJump(vector<int> A) {
        if (A.empty()) {
            return true;
        }

        int farthest = A[0];

        for (int i = 1; i != A.size(); ++i) {
            if ((i <= farthest) && (i + A[i] > farthest)) {
                farthest = i + A[i];
            }
        }

        return farthest >= A.size() - 1;
    }
};
```
