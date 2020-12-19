
def lps_tabulation(s):
	M = len(s)
	N = M

	x = s
  y = s[::-1]

	dp = [[0 for c in range(N+1)] for r in range(M+1)]

	for i in range(M+1):
		for j in range(N+1):
			if i == 0 or j == 0:
				dp[i][j] = 0
			elif M[i] == M[j]:
				dp[i][j] = 1 + dp[i-1][j-1]
			else:
				dp[i][j] = max(dp[i-1][j], dp[i][j-1])

	return dp[M][N]


#   @ a g b c b a
# @
# a
# b
# c
# b
# g
# a
