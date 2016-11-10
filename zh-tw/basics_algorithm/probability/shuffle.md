# Shuffle and Sampling - 隨機抽樣和洗牌

## 洗牌算法

- [Shuffle a given array - GeeksforGeeks](http://www.geeksforgeeks.org/shuffle-a-given-array/)

Given an array, write a program to generate a random permutation of array elements. This question is also asked as “shuffle a deck of cards” or “randomize a given array”.

### 題解

這裡以 Fisher–Yates shuffle 演算法爲例，僞代碼如下：

```
To shuffle an array a of n elements (indices 0..n-1):
  for i from 0 downto i do
       j ← random integer such that 0 ≤ j ≤ i
       exchange a[j] and a[i]
```

轉化爲代碼爲：

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

看了算法和代碼後讓我們來使用歸納法簡單證明下這個洗牌算法的正確性。我們要證明的問題是：**數組中每個元素在每個索引處出現的機率均相等。**

對於單個元素來講，以上算法顯然正確，因爲交換後仍然只有一個元素。接下來我們不妨假設其遍歷到數組索引爲`i-1`時滿足隨機排列特性，那麼當遍歷到數組索引爲`i`時，隨機數`k`爲`i`的機率爲`1/i`, 爲`0~i-1`的機率爲`(i-1)/i`. 接下來與索引爲`i`的值交換，可以得知`card[i]`出現在索引`i`的位置的機率爲`1/i`, 在其他索引位置的機率也爲`1/i`; 而對於`card[i]`之前的元素，以索引`j`處的元素`card[j]`爲例進行分析可知其在位置`j`的機率爲`1/(i-1) * (i-1)/i = 1/i`, 具體含義爲遍歷到索引`i-1`時`card[j]`位於索引`j`的機率(`1/(i-1)`)乘以遍歷到索引`i`時隨機數未選擇與索引`j`的數進行交換的機率(`(i-1)/i`).

需要注意的是前面的`j <= i-1`, 那麼`card[j]`位於索引`i`的機率又是多少呢？要位於索引`i`，則隨機數`k`須爲`i`, 這種機率爲`1/i`.

綜上，以上算法可以實現完美洗牌（等機率）。

## Random sampling - 隨機抽樣

隨機抽樣也稱爲水池抽樣，Randomly choosing a sample of k items from a list S containing n items. 大意是從大小爲 n 的數組中隨機選出 m 個整數，要求每個元素被選中的機率相同。

### 題解

比較簡潔的有算法 Algorithm R, 僞代碼如下：

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

轉化爲代碼爲：

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

和洗牌算法類似，我們要證明的問題是：**數組中每個元素在最終採樣的數組中出現的機率均相等且爲`m/n`.** 洗牌算法中是排列，而對於隨機抽樣則爲組合。

維基百科上的證明相對容易懂一些，這裏我稍微複述下。首先將數組前 m 個元素填充進新數組`sample`, 然後從`m`開始遍歷直至數組最後一個索引。隨機數`k`的範圍爲`0~i`, 如果`k < m`，新數組的索引爲 k 的元素則和原數組索引爲`i`的元素交換；如果`k >= m`, 則不進行交換。`i == m`時，以原數組中第`j`個元素爲例，它被`nums[m]`替換的機率爲`1/(m+1)`, 也就是說保留在`sample`數組中的機率爲`m/(m+1)`. 對與第`m+1`個元素`nums[m]`來說，其位於`sample`數組中的機率則爲`m*1/(m+1)`(可替換 m 個不同的元素).

接下來仍然使用數學歸納法證明，若`i`遍歷到`r`時，其之前的元素出現的機率爲`m/(r-1)`, 那麼其之前的元素中任一元素`nums[j]`被替換的機率爲`m/r * 1/m = 1/r`, 不被替換的機率則爲`(r-1)/r`. 故元素`nums[j]`在`i`遍歷完`r`後仍然保留的機率爲`m/(r-1) * (r-1)/r = m/r`. 而對於元素`nums[r]`來說，其要被替換至`sample`數組中的機率則爲`m/r`(隨機數小於m 的個數爲 m).

綜上，以上算法在遍歷完長度爲 n 的數組後每個數出現在最終`sample`數組中的機率都爲`m/n`.

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

以十萬次試驗爲例，左側是元素`i`, 列代表在相應索引位置出現的次數。可以看出分佈還是比較隨機的。

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

- [Fisher–Yates shuffle](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle#The_modern_algorithm) - 洗牌算法的詳述，比較簡潔的演算法
- [Reservoir sampling ](https://en.wikipedia.org/wiki/Reservoir_sampling) - 水池抽樣算法
- [如何測試洗牌程序 | 酷 殼 - CoolShell.cn](http://coolshell.cn/articles/8593.html) - 借鑑了其中的一些測試方法
- 《計算機程序設計藝術》第二卷（半數值算法） - 3.4.2 隨機抽樣和洗牌
- 《編程珠璣》第十二章 - 抽樣問題
