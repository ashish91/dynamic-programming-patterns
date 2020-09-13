# length: 10  5 2  9 24
# price :  8 10 1 18 20
#
# Write down a Recursive Solution
def rod_cutting_recursive(n, L, length, price):
	if n == 0 || L == 0:
		return 0

	if length[n-1] <= L:
		return max(rod_cutting_recursive(n, L-length[n-1], length, price),
			rod_cutting_recursive(n-1, L, length, price))
	else:
		return rod_cutting_recursive(n-1, L, length, price)

def rod_cutting(length, price, L):
	N = len(length)
	rod_cutting_recursive(N, length, price, L)

# Memoize the above recursive solution
def rod_cutting(length, price, L):
	N = len(length)
	mem = [[-1 for c in range(N+1)] for r in range(L+1)]

	def rod_cutting_memoization(n, length, price, L):
		if n == 0 || L == 0:
			return 0

		if mem[n][L] >= 0:
			return mem[n][L]

		if length[n-1] <= L:
			mem[n][L] = max(rod_cutting_recursive(n, length, price, L-length[n-1]),
				rod_cutting_recursive(n-1, length, price, L))
		else:
			mem[n][L] = rod_cutting_recursive(n-1, length, price, L)

		return mem[n][L]

	return rod_cutting_memoization(N, length, price, L)

# Top Down Tabulation
def rod_cutting_tabulation(length, price, L):
	N = len(length)
	dp = [[-1 for l in range(L+1)] for c in range(N+1)]

	for n in range(N+1):
		for l in range(L+1):
			if l == 0 or n == 0:
				dp[n][l] = 0
			elif length[n] <= l:
				dp[n][l] = max(dp[n-1][l], dp[n][l] + length[n-1])
			else:
				dp[n][l] = dp[n-1][l]

	return dp[N][L]