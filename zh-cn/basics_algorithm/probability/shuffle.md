# Shuffle and Sampling - 随机抽样和洗牌

## 洗牌算法

- [Shuffle a given array - GeeksforGeeks](http://www.geeksforgeeks.org/shuffle-a-given-array/)

Given an array, write a program to generate a random permutation of array elements. This question is also asked as “shuffle a deck of cards” or “randomize a given array”.

### 题解

这里以 Fisher–Yates shuffle 算法为例，伪代码如下：

```
To shuffle an array a of n elements (indices 0..n-1):
  for i from 0 downto i do
       j ← random integer such that 0 ≤ j ≤ i
       exchange a[j] and a[i]
```

转化为代码为：

```java
    /*
     * shuffle cards
     */
    public static void shuffleCard(int[] cards) {
        if (cards == null || cards.length == 0) return;

        Random rand = new Random();
        for (int i = 0; i < cards.length; i++) {
            int k = rand.nextInt(i + 1); // 0~i (inclusive)
            int temp = cards[i];
            cards[i] = cards[k];
            cards[k] = temp;
        }
    }
```

看了算法和代码后让我们来使用归纳法简单证明下这个洗牌算法的正确性。我们要证明的问题是：**数组中每个元素在每个索引处出现的概率均相等。**

对于单个元素来讲，以上算法显然正确，因为交换后仍然只有一个元素。接下来我们不妨假设其遍历到数组索引为`i-1`时满足随机排列特性，那么当遍历到数组索引为`i`时，随机数`k`为`i`的概率为`1/i`, 为`0~i-1`的概率为`(i-1)/i`. 接下来与索引为`i`的值交换，可以得知`card[i]`出现在索引`i`的位置的概率为`1/i`, 在其他索引位置的概率也为`1/i`; 而对于`card[i]`之前的元素，以索引`j`处的元素`card[j]`为例进行分析可知其在位置`j`的概率为`1/(i-1) * (i-1)/i = 1/i`, 具体含义为遍历到索引`i-1`时`card[j]`位于索引`j`的概率(`1/(i-1)`)乘以遍历到索引`i`时随机数未选择与索引`j`的数进行交换的概率(`(i-1)/i`).

需要注意的是前面的`j <= i-1`, 那么`card[j]`位于索引`i`的概率又是多少呢？要位于索引`i`，则随机数`k`须为`i`, 这种概率为`1/i`.

综上，以上算法可以实现完美洗牌（等概率）。

## Random sampling - 随机抽样

随机抽样也称为水池抽样，Randomly choosing a sample of k items from a list S containing n items. 大意是从大小为 n 的数组中随机选出 m 个整数，要求每个元素被选中的概率相同。

### 题解

比较简洁的有算法 Algorithm R, 伪代码如下：

```
/*
  S has items to sample, R will contain the result
*/
ReservoirSample(S[1..n], R[1..k])
  // fill the reservoir array
  for i = 1 to k
      R[i] := S[i]

  // replace elements with gradually decreasing probability
  for i = k+1 to n
    j := random(1, i)   // important: inclusive range
    if j <= k
        R[j] := S[i]
```

转化为代码为：

```java
    /*
     * random sample
     */
    public static int[] randomSample(int[] nums, int m) {
        if (nums == null || nums.length == 0 || m <= 0) return new int[]{};

        int[] sample = new int[m];
        for (int i = 0; i < m; i++) {
            sample[i] = nums[i];
        }

        Random random = new Random();
        for (int i = m; i < nums.length; i++) {
            int k = random.nextInt(i + 1); // 0~i(inclusive)
            if (k < m) {
                sample[k] = nums[i];
            }
        }

        return sample;
    }
```

和洗牌算法类似，我们要证明的问题是：**数组中每个元素在最终采样的数组中出现的概率均相等且为`m/n`.** 洗牌算法中是排列，而对于随机抽样则为组合。

维基百科上的证明相对容易懂一些，这里我稍微复述下。首先将数组前 m 个元素填充进新数组`sample`, 然后从`m`开始遍历直至数组最后一个索引。随机数`k`的范围为`0~i`, 如果`k < m`，新数组的索引为 k 的元素则和原数组索引为`i`的元素交换；如果`k >= m`, 则不进行交换。`i == m`时，以原数组中第`j`个元素为例，它被`nums[m]`替换的概率为`1/(m+1)`, 也就是说保留在`sample`数组中的概率为`m/(m+1)`. 对与第`m+1`个元素`nums[m]`来说，其位于`sample`数组中的概率则为`m*1/(m+1)`(可替换 m 个不同的元素).

接下来仍然使用数学归纳法证明，若`i`遍历到`r`时，其之前的元素出现的概率为`m/(r-1)`, 那么其之前的元素中任一元素`nums[j]`被替换的概率为`m/r * 1/m = 1/r`, 不被替换的概率则为`(r-1)/r`. 故元素`nums[j]`在`i`遍历完`r`后仍然保留的概率为`m/(r-1) * (r-1)/r = m/r`. 而对于元素`nums[r]`来说，其要被替换至`sample`数组中的概率则为`m/r`(随机数小于m 的个数为 m).

综上，以上算法在遍历完长度为 n 的数组后每个数出现在最终`sample`数组中的概率都为`m/n`.

## Implementation and Test case

**Talk is cheap, show me the code!**

### Java

```java
import java.util.*;
import java.util.Random;

public class Probability {
    public static void main(String[] args) {
        int[] cards = new int[10];
        for (int i = 0; i < 10; i++) {
            cards[i] = i;
        }
        // 100000 times test
        final int times = 100000;
        final int m = 5;
        int[][] count = new int[cards.length][cards.length];
        int[][] count2 = new int[cards.length][m];
        for (int i = 0; i < times; i++) {
            shuffleCard(cards);
            shuffleTest(cards, count);
            int[] sample = randomSample(cards, m);
            shuffleTest(sample, count2);
        }
        System.out.println("Shuffle cards");
        shufflePrint(count);
        System.out.println();
        System.out.println("Random sample");
        shufflePrint(count2);
    }

    /*
     * shuffle cards
     */
    public static void shuffleCard(int[] cards) {
        if (cards == null || cards.length == 0) return;

        Random rand = new Random();
        for (int i = 0; i < cards.length; i++) {
            int k = rand.nextInt(i + 1);
            int temp = cards[i];
            cards[i] = cards[k];
            cards[k] = temp;
        }
    }

    /*
     * random sample
     */
    public static int[] randomSample(int[] nums, int m) {
        if (nums == null || nums.length == 0 || m <= 0) return new int[]{};

        m = Math.min(m, nums.length);
        int[] sample = new int[m];
        for (int i = 0; i < m; i++) {
            sample[i] = nums[i];
        }

        Random random = new Random();
        for (int i = m; i < nums.length; i++) {
            int k = random.nextInt(i + 1);
            if (k < m) {
                sample[k] = nums[i];
            }
        }

        return sample;
    }

    /*
     * nums[i] = j, num j appear in index i ==> count[j][i]
     */
    public static void shuffleTest(int[] nums, int[][] count) {
        if (nums == null || nums.length == 0) return;

        for (int i = 0; i < nums.length; i++) {
            count[nums[i]][i]++;
        }
    }

    /*
     * print shuffle test
     */
    public static void shufflePrint(int[][] count) {
        if (count == null || count.length == 0) return;

        // print index
        System.out.print("   ");
        for (int i = 0; i < count[0].length; i++) {
            System.out.printf("%-7d", i);
        }
        System.out.println();
        // print num appear in index i in total
        for (int i = 0; i < count.length; i++) {
            System.out.print(i + ": ");
            for (int j = 0; j < count[i].length; j++) {
                System.out.printf("%-7d", count[i][j]);
            }
            System.out.println();
        }
    }
}
```

以十万次试验为例，左侧是元素`i`, 列代表在相应索引位置出现的次数。可以看出分布还是比较随机的。

```
Shuffle cards
   0      1      2      3      4      5      6      7      8      9
0: 10033  9963   10043  9845   9932   10020  9964   10114  10043  10043
1: 9907   9951   9989   10071  10059  9966   10054  10023  10015  9965
2: 10042  10046  9893   10080  10050  9994   10024  9852   10098  9921
3: 10039  10023  10039  10024  9919   10057  10188  9916   9907   9888
4: 9944   9913   10196  10059  9838   10205  9899   9945   9850   10151
5: 10094  9971   10054  9958   10022  9922   10047  9978   9965   9989
6: 9995   10147  9824   10015  10023  9804   10050  10192  9939   10011
7: 9941   10131  9902   9920   10040  10121  10010  9928   9984   10023
8: 10010  9926   9883   10098  10083  10028  9801   9936   10200  10035
9: 9995   9929   10177  9930   10034  9883   9963   10116  9999   9974

Random sample
   0      1      2      3      4
0: 9966   10026  10078  9966   9891
1: 9958   9806   10066  10022  10039
2: 9923   9936   9964   10051  10083
3: 10165  10088  10184  9928   9916
4: 9998   9990   9973   9931   9832
5: 10026  9932   9873   10085  10035
6: 9942   9972   9990   10030  10026
7: 9903   10153  9997   10051  10044
8: 10082  10066  9804   9899   10147
9: 10037  10031  10071  10037  9987
```

## Reference

- [Fisher–Yates shuffle](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle#The_modern_algorithm) - 洗牌算法的详述，比较简洁的算法
- [Reservoir sampling ](https://en.wikipedia.org/wiki/Reservoir_sampling) - 水池抽样算法
- [如何测试洗牌程序 | 酷 壳 - CoolShell.cn](http://coolshell.cn/articles/8593.html) - 借鉴了其中的一些测试方法
- 《计算机程序设计艺术》第二卷（半数值算法） - 3.4.2 随机抽样和洗牌
- 《编程珠玑》第十二章 - 抽样问题
