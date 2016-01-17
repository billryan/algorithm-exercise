# 3 Sum Closest

## Question

- leetcode: [3Sum Closest | LeetCode OJ](https://leetcode.com/problems/3sum-closest/)
- lintcode: [(59) 3 Sum Closest](http://www.lintcode.com/en/problem/3-sum-closest/)

```
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. 
Return the sum of the three integers. You may assume that each input would have exactly one solution.

For example, given array S = {-1 2 1 -4}, and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
```
## 题解1 - 排序 + 2 Sum + 两根指针 + 优化过滤

和 3 Sum 的思路接近，首先对原数组排序，随后将3 Sum 的题拆解为『1 Sum + 2 Sum』的题，对于 Closest 的题使用两根指针而不是哈希表的方法较为方便。对于有序数组来说，在查找 Cloest 的值时其实是有较大的优化空间的。

### Python

```python
class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target : An integer
    @return : return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        result = 2**31 - 1
        length = len(numbers)
        if length < 3:
            return result

        numbers.sort()
        larger_count = 0
        for i, item_i in enumerate(numbers):
            start = i + 1
            end = length - 1
            # optimization 1 - filter the smallest sum greater then target
            if start < end:
                sum3_smallest = numbers[start] + numbers[start + 1] + item_i
                if sum3_smallest > target:
                    larger_count += 1
                    if larger_count > 1:
                        return result

            while (start < end):
                sum3 = numbers[start] + numbers[end] + item_i
                if abs(sum3 - target) < abs(result - target):
                    result = sum3

                # optimization 2 - filter the sum3 closest to target
                sum_flag = 0
                if sum3 > target:
                    end -= 1
                    if sum_flag == -1:
                        break
                    sum_flag = 1
                elif sum3 < target:
                    start += 1
                    if sum_flag == 1:
                        break
                    sum_flag = -1
                else:
                    return result

        return result
```

### 源码分析

1. leetcode 上不让自己导入`sys`包，保险起见就初始化了`result`为还算较大的数，作为异常的返回值。
2. 对数组进行排序。
3. 依次遍历排序后的数组，取出一个元素`item_i`后即转化为『2 Sum Cloest』问题。『2 Sum Cloest』的起始元素索引为`i + 1`，之前的元素不能参与其中。
4. 优化一——由于已经对原数组排序，故遍历原数组时比较最小的三个元素和`target`值，若第二次大于`target`果断就此罢休，后面的值肯定越来越大。
5. 两根指针求『2 Sum Cloest』，比较`sum3`和`result`与`target`的差值的绝对值，更新`result`为较小的绝对值。
6. 再度对『2 Sum Cloest』进行优化，仍然利用有序数组的特点，若处于『一大一小』的临界值时就可以马上退出了，后面的元素与`target`之差的绝对值只会越来越大。

### 复杂度分析

对原数组排序，平均时间复杂度为 $$O(n \log n)$$, 两重`for`循环，由于有两处优化，故最坏的时间复杂度才是 $$O(n^2)$$, 使用了`result`作为临时值保存最接近`target`的值，两处优化各使用了一个辅助变量，空间复杂度 $$O(1)$$.

### C++

```c++
class Solution {
public:
    int threeSumClosest(vector<int> &num, int target) 
    {
        if (num.size() <= 3) return accumulate(num.begin(), num.end(), 0);
        sort (num.begin(), num.end());

        int result = 0, n = num.size(), temp;
        result = num[0] + num[1] + num[2];
        for (int i = 0; i < n - 2; ++i)
        {
            int j = i + 1, k = n - 1;
            while (j < k)
            {
                temp = num[i] + num[j] + num[k];
                
                if (abs(target - result) > abs(target - temp))
                    result = temp;
                if (result == target)
                    return result;
                ( temp > target ) ? --k : ++j;
            }
        }
        return result;
    }
};
```
### 源码分析

和前面3Sum解法相似，同理使用i,j,k三个指针进行循环。<br>
区别在于3sum中的target为0，这里新增一个变量用于比较哪组数据与target更为相近

### 复杂度分析

时间复杂度同理为$$O(n^2)$$
运行时间 16ms

## Reference

- [3Sum Closest | 九章算法](http://www.jiuzhang.com/solutions/3sum-closest/)
