# Given a set and a sum, find number subset whose sum of elements equals sum
#
#
# Recursive Solution
def count_subset_sum_recursive(n, arr, sum):
	if sum == 0 or n == 0:
		return 1 if sum == 0 else 0

	if arr[n-1] >= sum:
		return count_subset_sum_recursive(n-1, arr, sum-arr[n-1]) + count_subset_sum_recursive(n-1, arr, sum)
	else:
		return count_subset_sum_recursive(n-1, arr, sum)

def count_subset_sum(arr, sum):
	N = len(arr)
	return count_subset_sum_recursive(N, arr, sum)

# Memoize recursive solution
def count_subset_sum(arr, sum):
	N = len(arr)
	mem = [[-1 for c in range(sum+1)] for r in range(N+1)]
	def count_subset_sum_memoized(n, arr, sum):
		if sum == 0 or n == 0:
			return 1 if sum == 0 else 0

		if mem[n][sum] >= 0:
			return mem[n][sum]

		if arr[n-1] >= sum:
			return count_subset_sum_recursive(n-1, arr, sum-arr[n-1]) + count_subset_sum_recursive(n-1, arr, sum)
		else:
			return count_subset_sum_recursive(n-1, arr, sum)

	count_subset_sum_memoized(N, arr, sum)
	return mem[N][sum]

# Memoize recursive solution
def count_subset_sum_tabulation(arr, sum):
	N = len(arr)
	dp = [[-1 for c in range(sum+1)] for r in range(N+1)]

	for r in range(N+1):
		for c in range(sum+1):
			if c == 0:
				dp[r][c] = 1
			elif r == 0:
				dp[r][c] = 0
			elif arr[r] >= c:
				dp[r][c] = dp[r-1][c-arr[r]] + dp[r-1][c]
			else:
				dp[r][c] = dp[r-1][c]

	return dp[N][sum]