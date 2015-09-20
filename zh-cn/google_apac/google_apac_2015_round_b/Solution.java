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
