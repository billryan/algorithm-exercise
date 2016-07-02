# Ugly Number

## Question

- leetcode: [Ugly Number | LeetCode OJ](https://leetcode.com/problems/ugly-number/)
- lintcode: [(4) Ugly Number](http://www.lintcode.com/en/problem/ugly-number/)

```
Ugly number is a number that only have factors 3, 5 and 7.

Design an algorithm to find the Kth ugly number.
The first 5 ugly numbers are 3, 5, 7, 9, 15 ...

Example
If K=4, return 9.
Challenge
O(K log K) or O(K) time.
```

## 题解1 - TLE

Lintcode 和 Leetcode 中质数稍微有点区别，这里以 Lintcode 上的版本为例进行说明。寻找第 K 个丑数，丑数在这里的定义是仅能被3，5，7整除。简单粗暴的方法就是挨个检查正整数，数到第 K 个丑数时即停止。

### Java

```java
class Solution {
    /**
     * @param k: The number k.
     * @return: The kth prime number as description.
     */
    public long kthPrimeNumber(int k) {
        if (k <= 0) return -1;

        int count = 0;
        long num = 1;
        while (count < k) {
            num++;
            if (isUgly(num)) {
                count++;
            }
        }

        return num;
    }

    private boolean isUgly(long num) {
        while (num % 3 == 0) {
            num /= 3;
        }
        while (num % 5 == 0) {
            num /= 5;
        }
        while (num % 7 == 0) {
            num /= 7;
        }

        return num == 1;
    }
}
```

### 源码分析

判断丑数时依次约掉质因数3，5，7，若处理完所有质因数3,5,7后不为1则不是丑数。自增 num 时应在判断是否为丑数之前。

### 复杂度分析

无法准确分析，但是估计在 $$O(n^3)$$ 以上。

## 题解2 - 二分查找

根据丑数的定义，它的质因数只含有3, 5, 7, 那么根据这一点其实可以知道后面的丑数一定可以从前面的丑数乘3,5,7得到。那么可不可以将其递推关系用数学公式表示出来呢？

我大概做了下尝试，首先根据丑数的定义可以写成 $$U_k = 3^{x_3} \cdot 5^{x_5} \cdot 7^{x_7}$$, 那么 $$U_{k+1}$$ 和 $$U_k$$ 的不同则在于 $$x_3, x_5, x_7$$ 的不同，递推关系为 $$U_{k+1} = U_k \cdot \frac{3^{y_3} \cdot 5^{y_5} \cdot 7^{y_7}}{3^{z_3} \cdot 5^{z_5} \cdot 7^{z_7}}$$,将这些分数按照从小到大的顺序排列可在 $$O(K)$$ 的时间内解决，但是问题来了，得到这些具体的 $$y, z$$ 就需要费不少时间，且人工操作极易漏解。:( 所以这种解法只具有数学意义，没有想到好的实现方法。

除了这种找相邻递推关系的方法我们还可以尝试对前面的丑数依次乘3, 5, 7，直至找到比当前最大的丑数大的一个数，对乘积后的三种不同结果取最小值即可得下一个最大的丑数。这种方法需要保存之前的 N 个丑数，由于已按顺序排好，天然的二分法。

### C++
```c++
class Solution {
public:
    /*
     * @param k: The number k.
     * @return: The kth prime number as description.
     */
    long long kthPrimeNumber(int k) {
        if (k <= 0) return -1;
        
        vector<long long> ugly(k + 1);
        ugly[0] = 1;
        int index = 0, index3 = 0, index5 = 0, index7 = 0;
        while (index <= k) {
            long long val = ugly[index3]*3 < ugly[index5]*5 ? ugly[index3]*3 : ugly[index5]*5;
            val = val < ugly[index7]*7 ? val : ugly[index7]*7;
            if (val == ugly[index3]*3) ++index3;
            if (val == ugly[index5]*5) ++index5;
            if (val == ugly[index7]*7) ++index7;
            ugly[++index] = val;
        }
        return ugly[k];
    }
};
```

### Java

```java
class Solution {
    /**
     * @param k: The number k.
     * @return: The kth prime number as description.
     */
    public long kthPrimeNumber(int k) {
        if (k <= 0) return -1;

        ArrayList<Long> nums = new ArrayList<Long>();
        nums.add(1L);
        for (int i = 0; i < k; i++) {
            long minNextUgly = Math.min(nextUgly(nums, 3), nextUgly(nums, 5));
            minNextUgly = Math.min(minNextUgly, nextUgly(nums, 7));
            nums.add(minNextUgly);
        }

        return nums.get(nums.size() - 1);
    }

    private long nextUgly(ArrayList<Long> nums, int factor) {
        int size = nums.size();
        int start = 0, end = size - 1;
        while (start + 1 < end) {
            int mid = start + (end - start) / 2;
            if (nums.get(mid) * factor > nums.get(size - 1)) {
                end = mid;
            } else {
                start = mid;
            }
        }
        if (nums.get(start) * factor > nums.get(size - 1)) {
            return nums.get(start) * factor;
        }

        return nums.get(end) * factor;
    }
}
```

### Golang

```go
var uglyNum []int

func init() {
	uglyNum = append(uglyNum, 1)
	len := 1
	i, j, k := 0, 0, 0
	for uglyNum[len-1] < math.MaxInt32 {
		tmpMin := min(uglyNum[i]*2, uglyNum[j]*3, uglyNum[k]*5)
		uglyNum = append(uglyNum, tmpMin)
		len++

		if uglyNum[i]*2 == tmpMin {
			i++
		}
		if uglyNum[j]*3 == tmpMin {
			j++
		}
		if uglyNum[k]*5 == tmpMin {
			k++
		}
	}
}

func min(a, b, c int) int {
	tmp := a
	if b < tmp {
		tmp = b
	}
	if c < tmp {
		tmp = c
	}
	return tmp
}

func nthUglyNumber(n int) int {
    if n < 1 {
		return 1
	}
	return uglyNum[n-1]
}
```


### 源码分析

`nextUgly`根据输入的丑数数组和 factor 决定下一个丑数，`nums.add(1L)`中1后面需要加 L表示 Long, 否则编译错误。

### 复杂度分析

找下一个丑数 $$O(\log K)$$, 循环 K 次，故总的时间复杂度近似 $$O(K \log K)$$, 使用了数组保存丑数，空间复杂度 $$O(K)$$.

## 题解3 - 动态规划

TBD

## Reference

- 《剑指 Offer》第五章
- [Ugly Numbers - GeeksforGeeks](http://www.geeksforgeeks.org/ugly-numbers/)
