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
