# X: a b c d e
# Y: a b f c e
#
# Top down tabulation

def print_lcs(x, y):
	M = len(x)
	N = len(y)

	dp = [[0 for c in range(N+1)] for r in range(M+1)]

	# Time Complexity: O(MN)
	for r in range(M+1):
		for c in range(N+1):
			if r == 0 or c == 0:
				dp[r][c] = 0
			elif x[r] == y[c]:
				dp[r][c] = 1+dp[r-1][c-1]
			else:
				dp[r][c] = max(dp[r-1][c], dp[r][c-1])

	r = M
	c = N
	lcs = ''
	# Time Complexity: O(M+N)
	while r > 0 and c > 0:
		if x[r-1] == y[c-1]:
			lcs = x[r-1]+lcs
			r -= 1
			c -= 1
		elif dp[r-1][c] > dp[r][c-1]:
			r -= 1
		else:
			c -= 1

	return lcs
