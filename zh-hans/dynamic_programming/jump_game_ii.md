# Jump Game II

## Question

- lintcode: [(117) Jump Game II](http://www.lintcode.com/en/problem/jump-game-ii/)

```
Given an array of non-negative integers,
you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2.
(Jump 1 step from index 0 to 1, then 3 steps to the last index.)
```

## 题解(自顶向下-动态规划)

首先来看看使用动态规划的解法，由于复杂度较高在A元素较多时会出现TLE，因为时间复杂度接近 $$O(n^3)$$. 工作面试中给出动规的实现就挺好了。

1. State: f[i] 从起点跳到这个位置最少需要多少步
2. Function: f[i] = MIN(f[j]+1, j < i && j + A[j] >= i) 取出所有能从j到i中的最小值
3. Initialization: f[0] = 0，即一个元素时不需移位即可到达
4. Answer: f[n-1]

### C++ Dynamic Programming

```c++
class Solution {
public:
    /**
     * @param A: A list of lists of integers
     * @return: An integer
     */
    int jump(vector<int> A) {
        if (A.empty()) {
            return -1;
        }

        const int N = A.size() - 1;
        vector<int> steps(N, INT_MAX);
        steps[0] = 0;

        for (int i = 1; i != N + 1; ++i) {
            for (int j = 0; j != i; ++j) {
                if ((steps[j] != INT_MAX) && (j + A[j] >= i)) {
                    steps[i] = steps[j] + 1;
                    break;
                }
            }
        }

        return steps[N];
    }
};
```

### 源码分析

状态转移方程为
```c++
if ((steps[j] != INT_MAX) && (j + A[j] >= i)) {
    steps[i] = steps[j] + 1;
    break;
}
```
其中break即体现了MIN操作，最开始满足条件的j即为最小步数。

## 题解(贪心法-自底向上)

使用动态规划解Jump Game的题复杂度均较高，这里可以使用贪心法达到线性级别的复杂度。

贪心法可以使用自底向上或者自顶向下，首先看看我最初使用自底向上做的。对A数组遍历，找到最小的下标`min_index`，并在下一轮中用此`min_index`替代上一次的`end`, 直至`min_index`为0，返回最小跳数`jumps`。以下的实现有个 bug，细心的你能发现吗？

### C++ greedy from bottom to top, bug version

```c++
class Solution {
public:
    /**
     * @param A: A list of lists of integers
     * @return: An integer
     */
    int jump(vector<int> A) {
        if (A.empty()) {
            return -1;
        }

        const int N = A.size() - 1;
        int jumps = 0;
        int last_index = N;
        int min_index = N;

        for (int i = N - 1; i >= 0; --i) {
            if (i + A[i] >= last_index) {
                min_index = i;
            }

            if (0 == min_index) {
                return ++jumps;
            }

            if ((0 == i) && (min_index < last_index)) {
                ++jumps;
                last_index = min_index;
                i = last_index - 1;
            }
        }

        return jumps;
    }
};
```

### 源码分析

使用jumps记录最小跳数，last_index记录离终点最远的坐标，min_index记录此次遍历过程中找到的最小下标。

以上的bug在于当min_index为1时，i = 0, for循环中仍有--i，因此退出循环，无法进入`if (0 == min_index)`语句，因此返回的结果会小1个。

### C++ greedy, from bottom to top

```c++
class Solution {
public:
    /**
     * @param A: A list of lists of integers
     * @return: An integer
     */
    int jump(vector<int> A) {
        if (A.empty()) {
            return 0;
        }

        const int N = A.size() - 1;
        int jumps = 0, end = N, min_index = N;

        while (end > 0) {
            for (int i = end - 1; i >= 0; --i) {
                if (i + A[i] >= end) {
                    min_index = i;
                }
            }

            if (min_index < end) {
                ++jumps;
                end = min_index;
            } else {
                // cannot jump to the end
                return -1;
            }
        }

        return jumps;
    }
};
```

### 源码分析

之前的 bug version 代码实在是太丑陋了，改写了个相对优雅的实现，加入了是否能到达终点的判断。在更新`min_index`的内循环中也可改为如下效率更高的方式：
```c++
            for (int i = 0; i != end; ++i) {
                if (i + A[i] >= end) {
                    min_index = i;
                    break;
                }
            }
```

## 题解(贪心法-自顶向下)

看过了自底向上的贪心法，我们再来瞅瞅自顶向下的实现。自顶向下使用`farthest`记录当前坐标出发能到达的最远坐标，遍历当前`start`与`end`之间的坐标，若`i+A[i] > farthest`时更新`farthest`(寻找最小跳数)，当前循环遍历结束时递推`end = farthest`。`end >= A.size() - 1`时退出循环，返回最小跳数。

### C++

```c++
/**
 * http://www.jiuzhang.com/solutions/jump-game-ii/
 */
class Solution {
public:
    /**
     * @param A: A list of lists of integers
     * @return: An integer
     */
    int jump(vector<int> A) {
        if (A.empty()) {
            return 0;
        }

        const int N = A.size() - 1;
        int start = 0, end = 0, jumps = 0;

        while (end < N) {
            int farthest = end;
            for (int i = start; i <= end; ++i) {
                if (i + A[i] >= farthest) {
                    farthest = i + A[i];
                }
            }

            if (end < farthest) {
                ++jumps;
                start = end + 1;
                end = farthest;
            } else {
                // cannot jump to the end
                return -1;
            }
        }

        return jumps;
    }
};
```
