# weights: 10  5 2  9 24
# values :  8 10 1 18 20
#
# Write down a Recursive Solution
def knapsack_recursive(n, w, weights, values):
	if (n == 0 or w == 0):
		return 0

	if weights[n-1] <= w:
		return max(values[n-1] + knapsack_recursive(n-1, w-weights[n-1], weights, values),
								knapsack_recursive(n-1, w, weights, values))
	else:
		return knapsack_recursive(n-1, w, weights, values)

def knapsack(weights, values, C):
	return knapsack_recursive(len(weights), C, weights, values)

# Memoize the above recursive solution
def knapsack(weights, values, C):
	mem = [[-1 for c in range(len(weights)+1)] for r in range(C+1)]
	def knapsack_memoized(n, w, weights, values):
		nonlocal mem
		if (n == 0 or w == 0):
			return 0

		if mem[n][w] >= 0:
			return mem[n][w]

		if weights[n-1] <= capacity:
			mem[n][w] = max(values[n-1] + knapsack_memoized(n-1, w-weights[n-1], weights, values),
									knapsack_memoized(n-1, w, weights, values))
		else:
			mem[n][w] = knapsack_memoized(n-1, w, weights, values)

		return mem[n][w]

	knapsack_memoized(len(weights), C, weights, values)

# Top Down Tabulation
def knapsack_tabulation(weights, values, capacity):
	W = capacity
	N = len(values)

	dp = [[0 for w in range(W+1)] for n in range(N+1)]

	for n in range(N+1):
		for w in range(W+1):
			if n == 0 || w == 0:
				dp[i][j] = 0
			elif weights[n] <= w:
				dp[n][w] = max(dp[n-1][w], dp[n-1][w-weights[n]] + values[n-1])
			else:
				dp[n][w] = dp[n-1][w]

	return dp[N][W]
