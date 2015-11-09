# Problem A. Dynamic Grid

## Source

- [Dashboard - Round D APAC Test 2016 - Problem A. Dynamic Grid](https://code.google.com/codejam/contest/11214486/dashboard#s=p0)

### Problem

We have a grid with **R** rows and **C** columns in which every entry is either 0 or 1. We are going to perform **N** operations on the grid, each of which is one of the following:

- Operation M: Change a number in one cell of the grid to 0 or 1
- Operation Q: Determine the number of different connected regions of 1s. A connected region of 1s is a subset of cells that are all 1, in which any cell in the region can be reached from any other cell in the region by traveling between cells along edges (**not** corners).

#### Input

The first line of the input gives the number of test cases, T. T test cases follow. Each test case starts with one line with two integers, R and C, which represent the number of rows and columns in the grid. Then, there are R lines of C characters each, in which every character is either 0 or 1. These lines represent the initial state of the grid.

The next line has one integer, N, the number of operations to perform on the grid. N more lines follow; each has one operation. All operation Ms will be of the form M x y z, meaning that the cell at row x and column y should be changed to the value z. All operation Qs will be of the form Q.

#### Output

For each test case, output one line containing "Case #x:", where x is the test case number (starting from 1). Then, for every operation Q in the test case, in order, output one line containing the number of connected regions of 1s.

#### Limits

```
1 ≤ T ≤ 10.
1 ≤ R, C ≤ 100.
0 ≤ x < R.
0 ≤ y < C.
0 ≤ z ≤ 1.
```

**Small dataset**

```
1 ≤ N ≤ 10.
```

**Large dataset**

```
1 ≤ N ≤ 1000.
```

#### Smaple

```
Input       Output

1           Case #1:
4 4         4
0101        2
0010        2
0100        2
1111
7
Q
M 0 2 1
Q
M 2 2 0
Q
M 2 1 0
Q
```

## 题解

简单题，DFS 即可解决。从矩阵中为1且未访问过的坐标开始 DFS，直至所有点均已遍历过，从矩阵中为1的坐标调用 DFS 的次数即为题中所求。具体实现可以使用布尔型矩阵标记访问过的坐标或者原地修改数组值。这里使用原地修改的方式，代码量略小一点。

### Java

```java
import java.util.*;

public class Solution {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int T = in.nextInt();
		// System.out.println("T = " + T);
		for (int t = 1; t <= T; t++) {
			int R = in.nextInt(), C = in.nextInt();
			int[][] grid = new int[R][C];
			// System.out.println("R = " + R + ", C = " + C);
			in.nextLine();
			for (int r = 0; r < R; r++) {
				String row = in.nextLine();
				// System.out.println(row);
				for (int c = 0; c < C; c++) {
					int z = Character.getNumericValue(row.charAt(c));
					grid[r][c] = z;
				}
			}
			int N = in.nextInt();
			in.nextLine();
			System.out.printf("Case #%d:\n", t);
			int[][] gridNew = new int[R][C];
			for (int i = 0; i < N; i++) {
				String[] tokens = in.nextLine().split(" ");
				if (tokens[0].equals("Q")) {
					for (int r = 0; r < R; r++) {
						for (int c = 0; c < C; c++) {
							gridNew[r][c] = grid[r][c];
						}
					}
					int ans = solve(gridNew);
					// System.out.printf("M = %d, N = %d\n", M, N);
					System.out.println(ans);
				} else {
					int tx = Integer.parseInt(tokens[1]);
					int ty = Integer.parseInt(tokens[2]);
					int tz = Integer.parseInt(tokens[3]);
					grid[tx][ty] = tz;
				}
			}
		}
	}

	public static int solve(int[][] grid) {
		if (grid == null || grid.length == 0) {
			return -1;
		}

		int R = grid.length, C = grid[0].length;
		int res = 0;
		for (int r = 0; r < R; r++) {
			for (int c = 0; c < C; c++) {
				if (grid[r][c] == 1) {
					dfs(grid, r, c);
					res++;
				}
			}
		}
		return res;
	}

	private static void dfs(int[][] grid, int x, int y) {
		int R = grid.length, C = grid[0].length;
		grid[x][y] = 0;
		for (int dx = -1; dx <= 1; dx++) {
			for (int dy = -1; dy <= 1; dy++) {
				int nx = x + dx, ny = y + dy;
				// up, down, left, right
				if (Math.abs(nx + ny - x - y) != 1) continue;
				if (0 <= nx && nx < R && 0 <= ny && ny < C) {
					if (grid[nx][ny] == 1) dfs(grid, nx, ny);
				}
			}
		}
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

对应每一个 Q，每个坐标点有四个方向，故单次求解时间复杂度 $$O(4RC)$$, 空间复杂度 $$O(RC)$$. 有 T 次测试数据及 N/2 次查询，故最终总的时间复杂度为 $$O(TNRC)$$, 代入 Large 数据集可知约为 $$O(10^8)$$, 几分钟内是可以解出来的。

## Reference

- 《挑战程序设计竞赛》穷竭搜索一章，POJ 八连通变形题
