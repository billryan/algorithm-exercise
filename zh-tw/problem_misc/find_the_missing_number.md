# Find the Missing Number

## Question

- lintcode: [(196) Find the Missing Number](http://www.lintcode.com/en/problem/find-the-missing-number/)
- [Find the Missing Number - GeeksforGeeks](http://www.geeksforgeeks.org/find-the-missing-number/)

### Problem Statement

Given an array contains _N_ numbers of 0 .. _N_, find which number doesn't exist in the array.

#### Example

Given _N_ = `3` and the array `[0, 1, 3]`, return `2`.

#### Challenge

Do it in-place with $$O(1)$$ extra memory and $$O(n)$$ time.

## 題解1 - 位運算

和找單數的題類似，這裡我們不妨試試位運算中 Exlcusive Or (XOR) 的思路。最開始自己想到的是利用相鄰項異或結果看是否會有驚喜，然而發現 `a^(a+1) != a^a + a^1` 之後眼淚掉下來... 如果按照找單數的做法，首先對陣列所有元素異或，得到數`x1`, 現在的問題是如何利用`x1`得到缺失的數，由於找單數中其他數都是成對出現的，故最後的結果即是單數，這裏每個數都是單數，怎麼辦呢？我們現在再來分析下如果沒有缺失數的話會是怎樣呢？假設所有元素異或得到數`x2`, 數`x1`和`x2`有什麼差異呢？假設缺失的數是`x0`，那麼容易知道`x2 = x1 ^ x0`, 相當於現在已知`x1`和`x2`，要求`x0`. 根據 [Bit Manipulation](http://algorithm.yuanbin.me/zh-hans/basics_misc/bit_manipulation.html) 中總結的交換律，`x0 = x1 ^ x2`.

位運算的題往往比較靈活，需要好好利用常用等式變換。

### Java

```java
public class Solution {
    /**
     * @param nums: an array of integers
     * @return: an integer
     */
    public int findMissing(int[] nums) {
        if (nums == null || nums.length == 0) return -1;

        // get xor from 0 to N excluding missing number
        int x1 = 0;
        for (int i : nums) {
            x1 ^= i;
        }

        // get xor from 0 to N
        int x2 = 0;
        for (int i = 0; i <= nums.length; i++) {
            x2 ^= i;
        }

        // missing = x1 ^ x2;
        return x1 ^ x2;
    }
}
```

### 源碼分析

略

### 複雜度分析

遍歷原陣列和 N+1大小的陣列，時間複雜度 $$O(n)$$, 空間複雜度 $$O(1)$$.

## 題解2 - 桶排序

非常簡單直觀的想法——排序後檢查缺失元素，但是此題中要求時間複雜度爲 $$O(n)$$, 因此如果一定要用排序來做，那一定是使用非比較排序如桶排序或者計數排序。題中另一提示則是要求只使用 $$O(1)$$ 的額外空間，那麼這就是在提示我們應該使用原地交換。根據題意，元素應無重複，可考慮使用桶排，索引和值一一對應即可。第一重 for 循環遍歷原陣列，內循環使用 while, 調整索引處對應的值，直至相等或者索引越界爲止，for 循環結束時桶排結束。最後再遍歷一次陣列找出缺失元素。

初次接觸這種題還是比較難想到使用桶排這種思想的，尤其是利用索引和值一一對應這一特性找出缺失元素，另外此題在實際實現時不容易做到 bug-free, while 循環處容易出現死循環。

### Java

```java
public class Solution {
    /**
     * @param nums: an array of integers
     * @return: an integer
     */
    public int findMissing(int[] nums) {
        if (nums == null || nums.length == 0) return -1;

        bucketSort(nums);
        // find missing number
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != i) {
                return i;
            }
        }

        return nums.length;
    }

    private void bucketSort(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            while (nums[i] != i) {
		        // ignore nums[i] == nums.length
                if (nums[i] == nums.length) {
                    break;
                }
                int nextNum = nums[nums[i]];
                nums[nums[i]] = nums[i];
		        nums[i] = nextNum;
            }
        }
    }
}
```

### 源碼分析

難點一在於正確實現桶排，難點二在於陣列元素中最大值 N 如何處理。N 有三種可能：

1. N 不在原陣列中，故最後應該返回 N
2. N 在原陣列中，但不在陣列中的最後一個元素
3. N 在原陣列中且在陣列最後一個元素

其中情況1在遍歷桶排後的陣列時無返回，最後返回 N.

其中2和3在 while 循環處均會遇到 break 跳出，即當前這個索引所對應的值要麼最後還是 N，要麼就是和索引相同的值。如果最後還是 N, 也就意味着原陣列中缺失的是其他值，如果最後被覆蓋掉，那麼桶排後的陣列不會出現 N, 且缺失的一定是 N 之前的數。

綜上，這裏的實現無論 N 出現在哪個索引都能正確返回缺失值。實現上還是比較巧妙的，所以說在沒做過這類題時要在短時間內 bug-free 比較難，當然也可能是我比較菜...

另外一個難點在於如何保證或者證明 while 一定不會出現死循環，可以這麼理解，如果 while 條件不成立且未出現`nums.length`這個元素，那麼就一定會使得一個元素正確入桶，又因爲沒有重復元素出現，故一定不會出現死循環。

### 複雜度分析

桶排時間複雜度 $$O(n)$$, 空間複雜度 $$O(1)$$. 遍歷原陣列找缺失數時間複雜度 $$O(n)$$. 故總的時間複雜度爲 $$O(n)$$, 空間複雜度 $$O(1)$$.
