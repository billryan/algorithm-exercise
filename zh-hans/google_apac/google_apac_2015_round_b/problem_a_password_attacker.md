# Problem A. Password Attacker

## Source

- [Dashboard - Round B APAC Test - Problem A. Password Attacker](https://code.google.com/codejam/contest/4214486/dashboard#s=p0)

### Problem

Passwords are widely used in our lives: for ATMs, online forum logins, mobile device unlock and door access. Everyone cares about password security. However, attackers always find ways to steal our passwords. Here is one possible situation:

Assume that Eve, the attacker, wants to steal a password from the victim Alice. Eve cleans up the keyboard beforehand. After Alice types the password and leaves, Eve collects the fingerprints on the keyboard. Now she knows which keys are used in the password. However, Eve won't know how many times each key has been pressed or the order of the keystroke sequence.

To simplify the problem, let's assume that Eve finds Alice's fingerprints only occurs on M keys. And she knows, by another method, that Alice's password contains N characters. Furthermore, every keystroke on the keyboard only generates a single, unique character. Also, Alice won't press other irrelevant keys like 'left', 'home', 'backspace' and etc.

Here's an example. Assume that Eve finds Alice's fingerprints on M=3 key '3', '7' and '5', and she knows that Alice's password is N=4-digit in length. So all the following passwords are possible: 3577, 3557, 7353 and 5735. (And, in fact, there are 32 more possible passwords.)

However, these passwords are not possible:

```
1357  // There is no fingerprint on key '1'
3355  // There is fingerprint on key '7',
         so '7' must occur at least once.
357   // Eve knows the password must be a 4-digit number.
```

With the information, please count that how many possible passwords satisfy the statements above. Since the result could be large, please output the answer modulo 1000000007(109+7).

#### Input

The first line of the input gives the number of test cases, T.
For the next T lines, each contains two space-separated numbers M and N, indicating a test case.

#### Output

For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1) and y is the total number of possible passwords modulo 1000000007(109+7).

#### Limits

**Small dataset**

T = 15.
1 ≤ M ≤ N ≤ 7.

**Large dataset**

T = 100.
1 ≤ M ≤ N ≤ 100.

#### Smaple

```
Input    Output

4
1 1      Case #1: 1
3 4      Case #2: 36
5 5      Case #3: 120
15 15    Case #4: 674358851
```

## 题解

题目看似很长，其实简单来讲就是用 M 个 不同的字符组成长度为 N 的字符串，问有多少种不同的排列。这里 M 小于 N，要是大于的话就是纯排列了。这道题我最开始想用纯数学方法推导公式一步到位，实践下来发现这种想法真是太天真了，这不是数学竞赛... 即使用推导也应该是推导类似动态规划的状态转移方程。

这里的动态规划不太明显，我们以状态`dp[m][n]`表示用 m 个不同的字符能组成长度为 n 的不同字符串的个数。这里需要注意的是最后长度为 n 的字符串中必须包含 m 个不同的字符，不多也不少。接下来就是寻找状态转移方程了，之前可能的状态为`dp[m - 1][n -1], dp[m - 1][n], dp[m][n - 1]`. 现在问题来了，怎么解释这些状态以寻找状态转移方程？常规方法为正向分析，即分析`m ==> n`, 但很快我们可以发现`dp[m - 1][n]`这个状态很难处理。既然正向分析比较麻烦，我们不妨试试反向从`n ==> m`分析，可以发现字符串个数由 n 变为 n-1，这减少的字符可以分为两种情况，一种是这个减少的字符就在前 n - 1个字符中，另一种则不在，如此一来便做到了不重不漏。相应的状态转移方程为：

```
dp[i][j] = dp[m][n-1] * m + dp[m - 1][n - 1] * m
```

第一种和第二种情况下字符串的第 n 位均可由 m 个字符中的一个填充。初始化分两种情况，第一种为索引为0时，其值显然为0；第二种则是 m 为1时，容易知道相应的排列为1。最后返回 `dp[M][N]`.

### Java

```java
import java.util.*;

public class Solution {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int T = in.nextInt();
		// System.out.println("T = " + T);
		for (int t = 1; t <= T; t++) {
			int M = in.nextInt(), N = in.nextInt();
			long ans = solve(M, N);
			// System.out.printf("M = %d, N = %d\n", M, N);
			System.out.printf("Case #%d: %d\n", t, ans);
		}
	}

	public static long solve(int M, int N) {
		long[][] dp = new long[1 + M][1 + N];
		long mod = 1000000007;
		for (int j = 1; j <= N; j++) {
			dp[1][j] = 1;
		}
		for (int i = 2; i <= M; i++) {
			for (int j = i; j <= N; j++) {
				dp[i][j] = i * (dp[i][j - 1] + dp[i - 1][j - 1]);
				dp[i][j] %= mod;
			}
		}

		return dp[M][N];
	}
}
```

### 源码分析

Google Code Jam 上都是自己下载输入文件，上传结果，这里我们使用输入输出重定向的方法解决这个问题。举个例子，将这段代码保存为`Solution.java`, 将标准输入重定向至输入文件，标准输出重定向至输出文件。编译好之后以如下方式运行：

```
java Solution < A-large-practice.in > A-large-practice.out
```

这种方式处理各种不同 OJ 平台的输入输出较为方便。

### 复杂度分析

时间复杂度 $$O(mn)$$, 空间复杂度 $$O(mn)$$.

## Reference

- [Google-APAC2015-"Password Attacker" - dmsehuang的专栏](http://blog.csdn.net/dmsehuang/article/details/40807799)
