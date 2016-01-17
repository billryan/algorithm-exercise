# Zero Sum Subarray

## Question

- lintcode: [(138) Subarray Sum](http://www.lintcode.com/en/problem/subarray-sum/)
- GeeksforGeeks: [Find if there is a subarray with 0 sum - GeeksforGeeks](http://www.geeksforgeeks.org/find-if-there-is-a-subarray-with-0-sum/)

```
Given an integer array, find a subarray where the sum of numbers is zero.
Your code should return the index of the first number and the index of the last number.

Example
Given [-3, 1, 2, -3, 4], return [0, 2] or [1, 3].

Note
There is at least one subarray that it's sum equals to zero.
```

## 题解1 - 两重 for 循环

题目中仅要求返回一个子串(连续)中和为0的索引，而不必返回所有可能满足题意的解。最简单的想法是遍历所有子串，判断其和是否为0，使用两重循环即可搞定，最坏情况下时间复杂度为 $$O(n^2)$$, 这种方法显然是极其低效的，极有可能会出现 TLE. 下面就不浪费篇幅贴代码了。

## 题解2 - 比较子串和(TLE)

两重 for 循环显然是我们不希望看到的解法，那么我们再来分析下题意，题目中的对象是分析子串和，那么我们先从常见的对数组求和出发，$$f(i) = \sum _{0} ^{i} nums[i]$$ 表示从数组下标 0 开始至下标 i 的和。子串和为0，也就意味着存在不同的 $$i_1$$ 和 $$i_2$$ 使得 $$f(i_1) - f(i_2) = 0$$, 等价于 $$f(i_1) = f(i_2)$$. 思路很快就明晰了，使用一 vector 保存数组中从 0 开始到索引`i`的和，在将值 push 进 vector 之前先检查 vector 中是否已经存在，若存在则将相应索引加入最终结果并返回。

### C++

```c++
class Solution {
public:
    /**
     * @param nums: A list of integers
     * @return: A list of integers includes the index of the first number
     *          and the index of the last number
     */
    vector<int> subarraySum(vector<int> nums){
        vector<int> result;

        int curr_sum = 0;
        vector<int> sum_i;
        for (int i = 0; i != nums.size(); ++i) {
            curr_sum += nums[i];

            if (0 == curr_sum) {
                result.push_back(0);
                result.push_back(i);
                return result;
            }

            vector<int>::iterator iter = find(sum_i.begin(), sum_i.end(), curr_sum);
            if (iter != sum_i.end()) {
                result.push_back(iter - sum_i.begin() + 1);
                result.push_back(i);
                return result;
            }

            sum_i.push_back(curr_sum);
        }

        return result;
    }
};
```

### 源码分析

使用`curr_sum`保存到索引`i`处的累加和，`sum_i`保存不同索引处的和。执行`sum_i.push_back`之前先检查`curr_sum`是否为0，再检查`curr_sum`是否已经存在于`sum_i`中。是不是觉得这种方法会比题解1好？错！时间复杂度是一样一样的！根本原因在于`find`操作的时间复杂度为线性。与这种方法类似的有哈希表实现，哈希表的查找在理想情况下可认为是 $$O(1)$$.

### 复杂度分析

最坏情况下 $$O(n^2)$$, 实测和题解1中的方法运行时间几乎一致。

## 题解3 - 哈希表

终于到了祭出万能方法时候了，题解2可以认为是哈希表的雏形，而哈希表利用空间换时间的思路争取到了宝贵的时间资源 :)

### C++

```c++
class Solution {
public:
    /**
     * @param nums: A list of integers
     * @return: A list of integers includes the index of the first number
     *          and the index of the last number
     */
    vector<int> subarraySum(vector<int> nums){
        vector<int> result;
        // curr_sum for the first item, index for the second item
        map<int, int> hash;
        hash[0] = 0;

        int curr_sum = 0;
        for (int i = 0; i != nums.size(); ++i) {
            curr_sum += nums[i];
            if (hash.find(curr_sum) != hash.end()) {
                result.push_back(hash[curr_sum]);
                result.push_back(i);
                return result;
            } else {
                hash[curr_sum] = i + 1;
            }
        }

        return result;
    }
};
```

### 源码分析

为了将`curr_sum == 0`的情况也考虑在内，初始化哈希表后即赋予 `<0, 0>`. 给 `hash`赋值时使用`i + 1`, `push_back`时则不必再加1.

由于 C++ 中的`map`采用红黑树实现，故其并非真正的「哈希表」，C++ 11中引入的`unordered_map`用作哈希表效率更高，实测可由1300ms 降至1000ms.

### 复杂度分析

遍历求和时间复杂度为 $$O(n)$$, 哈希表检查键值时间复杂度为 $$O(\log L)$$, 其中 $$L$$ 为哈希表长度。如果采用`unordered_map`实现，最坏情况下查找的时间复杂度为线性，最好为常数级别。

## 题解4 - 排序

除了使用哈希表，我们还可使用排序的方法找到两个子串和相等的情况。这种方法的时间复杂度主要集中在排序方法的实现。由于除了记录子串和之外还需记录索引，故引入`pair`记录索引，最后排序时先按照`sum`值来排序，然后再按照索引值排序。如果需要自定义排序规则可参考[^sort_pair_second].

### C++

```c++
class Solution {
public:
    /**
     * @param nums: A list of integers
     * @return: A list of integers includes the index of the first number
     *          and the index of the last number
     */
    vector<int> subarraySum(vector<int> nums){
        vector<int> result;
        if (nums.empty()) {
            return result;
        }

        const int num_size = nums.size();
        vector<pair<int, int> > sum_index(num_size + 1);
        for (int i = 0; i != num_size; ++i) {
            sum_index[i + 1].first = sum_index[i].first + nums[i];
            sum_index[i + 1].second = i + 1;
        }

        sort(sum_index.begin(), sum_index.end());
        for (int i = 1; i < num_size + 1; ++i) {
            if (sum_index[i].first == sum_index[i - 1].first) {
                result.push_back(sum_index[i - 1].second);
                result.push_back(sum_index[i].second - 1);
                return result;
            }
        }

        return result;
    }
};
```

### 源码分析

没啥好分析的，注意好边界条件即可。这里采用了链表中常用的「dummy」节点方法，`pair`排序后即为我们需要的排序结果。这种排序的方法需要先求得所有子串和然后再排序，最后还需要遍历排序后的数组，效率自然是比不上哈希表。但是在某些情况下这种方法有一定优势。

### 复杂度分析

遍历求子串和，时间复杂度为 $$O(n)$$, 空间复杂度 $$O(n)$$. 排序时间复杂度近似 $$O(n \log n)$$, 遍历一次最坏情况下时间复杂度为 $$O(n)$$. 总的时间复杂度可近似为 $$O(n \log n)$$. 空间复杂度 $$O(n)$$.

## 扩展

这道题的要求是找到一个即可，但是要找出所有满足要求的解呢？Stackoverflow 上有这道延伸题的讨论[^stackoverflow].

另一道扩展题来自 Google 的面试题 - [Find subarray with given sum - GeeksforGeeks](http://www.geeksforgeeks.org/find-subarray-with-given-sum/).

## Reference

- [^stackoverflow]: [algorithm - Zero sum SubArray - Stack Overflow](http://stackoverflow.com/questions/5534063/zero-sum-subarray)
- [^sort_pair_second]: [c++ - How do I sort a vector of pairs based on the second element of the pair? - Stack Overflow](http://stackoverflow.com/questions/279854/how-do-i-sort-a-vector-of-pairs-based-on-the-second-element-of-the-pair)
