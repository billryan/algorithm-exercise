# Problem A. Farthest Point（圆周上最远整点）

## Source

- [hihoCoder](http://hihocoder.com/contest/mstest2015sept2/problem/1)

### Problem

时间限制:5000ms

单点时限:1000ms

内存限制:256MB

### 描述

Given a circle on a two-dimentional plane.

Output the **integral** point in or on the boundary of the circle which has
the largest distance from the center.

### 输入

One line with three floats which are all accurate to three decimal places,
indicating the coordinates of the center x, y and the radius r.

For 80% of the data: |x|,|y|&lt;=1000, 1&lt;=r&lt;=1000

For 100% of the data: |x|,|y|&lt;=100000, 1&lt;=r&lt;=100000

### 输出

One line with two integers separated by one space, indicating the answer.

If there are multiple answers, print the one with the largest x-coordinate.

If there are still multiple answers, print the one with the largest
y-coordinate.



#### 样例输入

    1.000 1.000 5.000

#### 样例输出

    6 1

## 题解1 - 圆周枚举

其实自己最开始做这道题时用的就是枚举，但是似乎忘记加圆心坐标了，一直 WA... 题目要求是返回最大的 x, 所以我们首先根据半径范围将 x 的整数解范围求出来。然后求出可能的 y, 由于题中给出的解有3位小数，如果要精确求解的话，可以将圆方程两边同乘1000，然后判断是否为整数。

### Java

```java
import java.io.*;
import java.util.*;
import java.util.Queue;

class Point {
    long x;
    long y;
    Point(long x, long y) {
        this.x = x;
        this.y = y;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        double xd = in.nextDouble(), yd = in.nextDouble(), rd = in.nextDouble();
        Point result = solve(xd, yd, rd);
        System.out.println(result.x + " " + result.y);
    }

    private static Point solve(double x0, double y0, double r) {
        // convert double to long(accurate)
        long xl0 = (long)(x0 * 1000), yl0 = (long)(y0 * 1000), rl0 = (long)(r * 1000);
        Point res = new Point(Long.MIN_VALUE, Long.MIN_VALUE);
        int lower_x = (int)Math.ceil(x0 - r), upper_x = (int)Math.floor(x0 + r);
        for (int i = upper_x; i >= lower_x; i--) {
            // circle above
            long y1l = yl0 + (long)(Math.sqrt(rl0*rl0 - (i*1000 - xl0)*(i*1000 - xl0)) + 0.5);
            if ((i*1000 - xl0)*(i*1000 - xl0) + (y1l - yl0)*(y1l - yl0) == rl0*rl0) {
                // ensure y1 is integer
                if (y1l % 1000 == 0) {
                    res.x = i;
                    res.y = y1l / 1000;
                    return res;
                }
            }
            // circle below
            y1l = yl0 - (long)(Math.sqrt(rl0*rl0 - (i*1000 - xl0)*(i*1000 - xl0)) + 0.5);
            if ((i*1000 - xl0)*(i*1000 - xl0) + (y1l - yl0)*(y1l - yl0) == rl0*rl0) {
                // ensure y1 is integer
                if (y1l % 1000 == 0) {
                    res.x = i;
                    res.y = y1l / 1000;
                    return res;
                }
            }
        }

        return res;
    }
}
```

### 源码分析

自右向左枚举，先枚举圆的上半部分，再枚举圆的下半部分。注意1000的转换。

### 复杂度分析

最坏情况下 $$O(R)$$.

## 题解2 - 整数分解

看似容易实则比较难的一道题，现场通过率非常低。我们仔细审下题，求圆周上的整点，有多个整点时输出最大的 x 和最大的 y. 容易想到的方案是枚举所有可能的 x 和 y, 然后代入等式测试是否相等，这个过不了大的 x 和 y. 如果用开方的方法必然有误差，我用这种方法不知道贡献了多少 WA, 泪流满面... 作为在线测试，**更为合理的方案应为先暴力搜索拿到百分之八十的分数。**

从 Microsoft 和 Google APAC 在线测试的风格来看是偏向于程序设计竞赛的，那么题目的考点自然就在竞赛范围之内，这道题看似是浮点型的数据，~~实际上考的却是整数中数论的基础。~~**注意题中的 accurate to three decimal places, 那么也就意味着我们对给定的数据同乘 $$10^3$$ 后一定是整数！！**！这个关键的信息我在测试过程中也没注意到，直到第二天早上醒来后突然就想到了！兴奋地六点多就爬起来了。

首先肯定是要写出圆方程的，设圆心坐标为 $$(x_0, y_0)$$, 半径为 $$r$$, 那么我们有：
$$
(x - x_0)^2 + (y - y_0)^2 = r^2
$$

设 $$m = 10^3(x - x_0)$$, $$n = 10^3(y - y_0)$$, $$R = 10^3r$$, 那么我们有新的圆方程：
$$
m^2 + n^2 = R^2
$$
其中 `m, n, R` 均为整数。接下来我们看看给出的数据范围，x, y, r 均是 $$10^6$$ 以内，那么圆方程两边同乘 $$10^6$$ （括号内的数即乘上 $$10^3$$）后数据在 $$10^{18}$$ 以内。我们来估算下整数的范围，$$2^{10} \approx 10^3$$, Java 中 int 型为4个字节，最大为 $$2^{31} - 1 \approx 2 \cdot 10^9$$, long 型为8个字节，最大为 $$2^{63} - 1 \approx 2^3 \cdot 10^{18}$$, 估算下来应该选用 long 保存 m, n, R.

接下来就是数论部分的推导了，先来一个简单的推导，勾股数部分的推导不直观。首先从已知部分出发，已知的只有勾股数方程和 m, n 均是整数，那么接下来肯定是要利用整数的理论无疑了。我们首先对以上圆方程移项开方，考虑到圆的对称性，我们其实只需要考虑圆的八分之一即可。这里考虑`0 < m < r`部分，`m == 0`表示在点在轴上，最后单独加上。

$$
m = \sqrt{R^2 - n^2} = \sqrt{(R + n)(R - n)}
$$
由于 m 一定是整数，故根号内一定为完全平方数，由于排除了轴上的点，那么`-R < n < R`, 设`G = gcd(R + n, R - n)`, $$p^2 = (R + n) / G$$, $$q^2 = (R - n) / G$$, 于是我们有`m = Gpq`, `p > q`, 由于`G` 是`R + n` 和`R - n` 的最大公约数，故`p` 和`q`一定互质，且有：
$$
p^2 + q^2 = 2R / G
$$
由于`p`,`q` 都大于等于1，那么我们能推断出`G` 一定是 `2R` 的约数！根据约数(素数)部分的基础理论，我们可以在 $$O(\sqrt{2R})$$ 时间内找出所有约数。然后对以上等式进行缩放得到`p` 的范围，枚举求解，判断`p^2` 和`q^2` 是否互质(最大公约数是否为1)。

### Java

```java
import java.io.*;
import java.util.*;

class Point {
    long x;
    long y;
    Point(long x, long y) {
        this.x = x;
        this.y = y;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        double xd = in.nextDouble(), yd = in.nextDouble(), rd = in.nextDouble();
        // convert double to long(accurate)
        long x0 = (long)(xd * 1000), y0 = (long)(yd * 1000), r0 = (long)(rd * 1000);
        Point result = solve(x0, y0, r0);
        System.out.println(result.x + " " + result.y);
    }

    private static Point solve(long x0, long y0, long r) {
        Point res = new Point(Long.MIN_VALUE, Long.MIN_VALUE);
        long x_max = Long.MIN_VALUE, y_max = Long.MIN_VALUE;
        // p^2 + q^2 = 2R/divisor, p > q >= 1
        // 1 <= q^2 < R/G < p^2 < 2R/G ==> p >= 2
        List<Long> divisors = getDivisor(r << 1);
        for (long divisor : divisors) {
            long lower = Math.max(2, (long)Math.sqrt(r * 1.0/ divisor));
            // long upper = (long)Math.sqrt(2.0 * r / divisor);
            for (long p = lower; p * p <= 2 * r / divisor; p++) {
                long q = (long)Math.sqrt(2.0 * r / divisor - p * p);
                // check if q is integer
                if (p * p + q * q != 2 * r / divisor) continue;
                // ensure p^2 and q^2 have no common divisor
                if (gcd(p * p, q * q) == 1) {
                    long m = divisor * p * q;
                    long n = r - p * p * divisor;
                    List<Point> points = new ArrayList<Point>();
                    points.add(new Point(m + x0, n + y0));
                    points.add(new Point(m + x0, -1 * n + y0));
                    points.add(new Point(-1 * m + x0, n + y0));
                    points.add(new Point(-1 * m + x0, -1 * n + y0));
                    for (Point point : points) {
                        updateAns(point, res);
                    }
                }
            }
        }

        // axis point check
        List<Point> axis = new ArrayList<Point>();
        axis.add(new Point(x0 + r, y0));
        axis.add(new Point(x0 - r, y0));
        axis.add(new Point(x0, y0 + r));
        axis.add(new Point(x0, y0 - r));
        for (Point point : axis) {
            updateAns(point, res);
        }
        // divide by 1000
        res.x /= 1000;
        res.y /= 1000;

        return res;
    }

    public static void updateAns(Point p, Point res) {
        // point(x, y) in integer
        if ((p.x % 1000 == 0) && (p.y % 1000 == 0)) {
            if (p.x > res.x) {
                res.x = p.x;
                res.y = p.y;
            } else if (p.x == res.x && p.y > res.y) {
                res.y = p.y;
            }
        }
    }

    // enumerate all the divisor for n
    public static List<Long> getDivisor(long n) {
        List<Long> result = new ArrayList<Long>();
        for (long i = 1; i * i <= n; i++) {
            if (n % i == 0) {
                result.add(i);
                // i * i <= n ==> i <= n / i
                if (i != n / i) result.add(n / i);
            }
        }
        Collections.sort(result);
        return result;
    }

    public static long gcd(long a, long b) {
        return (b == 0L) ? a : gcd(b, a % b);
    }
}
```

### 源码分析

由于更新结果的操作非常频繁，单独写一个方法较好。

### 复杂度分析

求所有素数时间复杂度 $$O(\sqrt{n})$$, 判断是否互质时间复杂度 $$O(\log n)$$. 枚举最大公约数时间复杂度约 $$(\sqrt{n})$$，总的时间复杂度估算应该比 $$O(n)$$ 小一些，但是小的不明显。**所以说，这种方法费了老大劲，但是吃力不讨好！笔试中这种方法极不可取！**

## 题解3 - 勾股数

除了以上使用数论部分整数分解的方法外，还可以巧用勾股数的特性，这种方法需要熟知勾股数的特性。设正整数 $$m, n, r$$ 满足：
$$
m^2 + n^2 = r^2
$$
我们对上式两边进行平方可得：
$$
(m^2 - n^2)^2 + (2mn)^2 = (m^2 + n^2)^2 = (r^2)^2
$$
令 $$a = m^2 - n^2$$, $$b = 2mn$$, $$c = m^2 + n^2$$. 容易得到：
$$
a^2 + b^2 = c^2
$$
注意到上述推导可逆，那么也就是说只要我们找到正整数满足`m > n`就能找到所有可能的勾股数。且根据素勾股数的特性，`m`, `n` 为一奇一偶，不妨设其为`2k-1`, `2k`. 代入`c`中可知`c`为`4K + 1`. 即`c % 4 = 1`. 根据 [Tree of primitive Pythagorean triples](https://en.wikipedia.org/wiki/Tree_of_primitive_Pythagorean_triples) 中提到的方法，我们只需找出小于给定的`r`的素勾股数即可，然后判断是否能整除`r`.

### Java

```java
import java.io.*;
import java.util.*;
import java.util.Queue;

class Point {
    long x;
    long y;
    Point(long x, long y) {
        this.x = x;
        this.y = y;
    }
}

class Pythagorean {
    long x;
    long y;
    long z;
    Pythagorean(long x, long y, long z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        double xd = in.nextDouble(), yd = in.nextDouble(), rd = in.nextDouble();
        // convert double to long(accurate)
        long x0 = (long)(xd * 1000), y0 = (long)(yd * 1000), r0 = (long)(rd * 1000);
        Point result = solve(x0, y0, r0);
        System.out.println(result.x + " " + result.y);
    }

    private static Point solve(long x0, long y0, long r) {
        Point res = new Point(Long.MIN_VALUE, Long.MIN_VALUE);
        long x_max = Long.MIN_VALUE, y_max = Long.MIN_VALUE;
        // init
        Pythagorean pyth0 = new Pythagorean(3, 4, 5);
        Queue<Pythagorean> q = new LinkedList<Pythagorean>();
        q.offer(pyth0);
        boolean update = true;
        while (!q.isEmpty()) {
            int qSize = q.size();
            for (int i = 0; i < qSize; i++) {
                Pythagorean pyth = q.poll();
                if ((r % pyth.z) == 0) {
                    // System.out.println("x = " + pyth.x + ", y = " + pyth.y + ", r = " + pyth.z);
                    long k = r / pyth.z;
                    long kx = k * pyth.x;
                    long ky = k * pyth.y;
                    List<Point> points = new ArrayList<Point>();
                    points.add(new Point(x0 + kx, y0 + ky));
                    points.add(new Point(x0 - kx, y0 + ky));
                    points.add(new Point(x0 + kx, y0 - ky));
                    points.add(new Point(x0 - kx, y0 - ky));
                    if (kx != ky) {
                        points.add(new Point(y0 + ky, x0 + kx));
                        points.add(new Point(y0 - ky, x0 + kx));
                        points.add(new Point(y0 + ky, x0 - kx));
                        points.add(new Point(y0 - ky, x0 - kx));
                    }
                    for (Point point : points) {
                        updateAns(point, res);
                    }
                }
                // add next level Pythagorean
                for (Pythagorean p : nextPyths(pyth)) {
                    if (p.z > r) continue;
                    q.offer(p);
                }
            }
        }

        // axis point check
        List<Point> axis = new ArrayList<Point>();
        axis.add(new Point(x0 + r, y0));
        axis.add(new Point(x0 - r, y0));
        axis.add(new Point(x0, y0 + r));
        axis.add(new Point(x0, y0 - r));
        for (Point point : axis) {
            updateAns(point, res);
        }
        // divide by 1000
        res.x /= 1000;
        res.y /= 1000;

        return res;
    }

    public static List<Pythagorean> nextPyths(Pythagorean pyth) {
        List<Pythagorean> pyths = new ArrayList<Pythagorean>();
        // method 1
        Pythagorean pyth1 = new Pythagorean(0, 0, 0);
        pyth1.x = pyth.x - 2 * pyth.y + 2 * pyth.z;
        pyth1.y = 2 * pyth.x - 1 * pyth.y + 2 * pyth.z;
        pyth1.z = 2 * pyth.x - 2 * pyth.y + 3 * pyth.z;
        pyths.add(pyth1);
        // method 2
        Pythagorean pyth2 = new Pythagorean(0, 0, 0);
        pyth2.x = pyth.x + 2 * pyth.y + 2 * pyth.z;
        pyth2.y = 2 * pyth.x + 1 * pyth.y + 2 * pyth.z;
        pyth2.z = 2 * pyth.x + 2 * pyth.y + 3 * pyth.z;
        pyths.add(pyth2);
        // method 3
        Pythagorean pyth3 = new Pythagorean(0, 0, 0);
        pyth3.x = -1 * pyth.x + 2 * pyth.y + 2 * pyth.z;
        pyth3.y = -2 * pyth.x + pyth.y + 2 * pyth.z;
        pyth3.z = -2 * pyth.x + 2 * pyth.y + 3 * pyth.z;
        pyths.add(pyth3);

        return pyths;
    }

    public static void updateAns(Point p, Point res) {
        // point(x, y) in integer
        if ((p.x % 1000 == 0) && (p.y % 1000 == 0)) {
            if (p.x > res.x) {
                res.x = p.x;
                res.y = p.y;
            } else if (p.x == res.x && p.y > res.y) {
                res.y = p.y;
            }
        }
    }
}
```

### 源码分析

根据链接中提到的数据结构，使用队列按层次遍历较好，但是空间消耗较大，所以在入队时一定要剪枝。

### 复杂度分析

时间复杂度最坏情况下需要遍历所有可能素勾股数。空间复杂度消耗也比较客观...

## Reference

- [BZOJ 1041 [HAOI2008] 圆上的整点 题解与分析 - 初学者 - 博客频道 - CSDN.NET](http://blog.csdn.net/csyzcyj/article/details/10044629)
- [[BZOJ1041 [HAOI2008]圆上的整点]数论、勾股数相关定理 | edward_mj](http://edward-mj.com/archives/166)
- [勾股数 - 维基百科，自由的百科全书](https://zh.wikipedia.org/wiki/%E5%8B%BE%E8%82%A1%E6%95%B0)
- [hihoCoder](http://hihocoder.com/discuss/question/2619)
