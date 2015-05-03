# 2 Sum

## Source

- leetcode: [Two Sum | LeetCode OJ](https://leetcode.com/problems/two-sum/)
- lintcode: [(56) 2 Sum](http://www.lintcode.com/en/problem/2-sum/)

```
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers
such that they add up to the target, where index1 must be less than index2.
Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
```

## 题解1 - 哈希表

找两数之和是否为`target`, 如果是找数组中一个值为`target`该多好啊！遍历一次就知道了，我只想说，too naive... 难道要将数组中所有元素的两两组合都求出来与`target`比较吗？时间复杂度显然为 $$O(n^2)$$, 显然不符题目要求。找一个数时直接遍历即可，那么可不可以将两个数之和转换为找一个数呢？我们先来看看两数之和为`target`所对应的判断条件—— $$x_i + x_j = target$$, 可进一步转化为 $$x_i = target - x_j$$, 其中 $$i$$ 和 $$j$$ 为数组中的下标。一段神奇的数学推理就将找两数之和转化为了找一个数是否在数组中了！可见数学是多么的重要...

基本思路有了，现在就来看看怎么实现，显然我们需要额外的空间(也就是哈希表)来保存已经处理过的 $$x_j$$, 如果不满足等式条件，那么我们就往后遍历，并把之前的元素加入到哈希表中，如果`target`减去当前索引后的值在哈希表中找到了，那么就将哈希表中相应的索引返回，大功告成！

### C++

```c++
class Solution {
public:
    /*
     * @param numbers : An array of Integer
     * @param target : target = numbers[index1] + numbers[index2]
     * @return : [index1+1, index2+1] (index1 < index2)
     */
    vector<int> twoSum(vector<int> &nums, int target) {
        vector<int> result;
        const int length = nums.size();
        if (0 == length) {
            return result;
        }

        // first value, second index
        unordered_map<int, int> hash(length);
        for (int i = 0; i != length; ++i) {
            if (hash.find(target - nums[i]) != hash.end()) {
                result.push_back(hash[target - nums[i]]);
                result.push_back(i + 1);
                return result;
            } else {
                hash[nums[i]] = i + 1;
            }
        }

        return result;
    }
};
```

### 源码分析

1. 异常处理。
2. 使用 C++ 11 中的哈希表实现`unordered_map`映射值和索引。
3. 找到满足条件的解就返回，找不到就加入哈希表中。注意题中要求返回索引值的含义。

### 复杂度分析

哈希表用了和数组等长的空间，空间复杂度为 $$O(n)$$, 遍历一次数组，时间复杂度为 $$O(n)$$.

## 题解2 - 排序后使用两根指针

但凡可以用空间换时间的做法，往往也可以使用时间换空间。另外一个容易想到的思路就是先对数组排序，然后使用两根指针分别指向首尾元素，逐步向中间靠拢，直至找到满足条件的索引为止。

### C++

```c++
class Solution {
public:
    /*
     * @param numbers : An array of Integer
     * @param target : target = numbers[index1] + numbers[index2]
     * @return : [index1+1, index2+1] (index1 < index2)
     */
    vector<int> twoSum(vector<int> &nums, int target) {
        vector<int> result;
        const int length = nums.size();
        if (0 == length) {
            return result;
        }

        // first num, second is index
        vector<pair<int, int> > num_index(length);
        // map num value and index
        for (int i = 0; i != length; ++i) {
            num_index[i].first = nums[i];
            num_index[i].second = i + 1;
        }

        sort(num_index.begin(), num_index.end());
        int start = 0, end = length - 1;
        while (start < end) {
            if (num_index[start].first + num_index[end].first > target) {
                --end;
            } else if(num_index[start].first + num_index[end].first == target) {
                int min_index = min(num_index[start].second, num_index[end].second);
                int max_index = max(num_index[start].second, num_index[end].second);
                result.push_back(min_index);
                result.push_back(max_index);
                return result;
            } else {
                ++start;
            }
        }

        return result;
    }
};
```

### 源码分析

1. 异常处理。
2. 使用`length`保存数组的长度，避免反复调用`nums.size()`造成性能损失。
3. 使用`pair`组合排序前的值和索引，避免排序后找不到原有索引信息。
4. 使用标准库函数排序。
5. 两根指针指头尾，逐步靠拢。

### 复杂度分析

遍历一次原数组得到`pair`类型的新数组，时间复杂度为 $$O(n)$$, 空间复杂度也为 $$O(n)$$. 标准库中的排序方法时间复杂度近似为 $$O(n \log n)$$, 两根指针遍历数组时间复杂度为 $$O(n)$$.

> **Note** lintcode 上的题要求时间复杂度在 $$O(n \log n)$$ 时，空间复杂度为 $$O(1)$$, 但问题是排序后索引会乱掉，如果要保存之前的索引，空间复杂度一定是 $$O(n)$$，所以个人认为不存在较为简洁的 $$O(1)$$ 实现。
