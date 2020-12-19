# X: a b c d e
# Y: a b f c e
#
# Top Down Tabulation
def lcss_tabulation(x, y):
	M = len(x)
	N = len(y)

	dp = [[0 for c in range(N+1)] for r in range(M+1)]

	for i in range(M+1):
		for j in range(N+1):
			if i == 0 or j == 0:
				dp[i][j] = 0
			elif x[i] == y[i]:
				dp[i][j] = 1+dp[i-1][j-1]
			else:
				dp[i][j] = 0

	return dp[M][N]

