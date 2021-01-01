# Given a set and a sum, find if there exists a subset whose sum of elements equals sum
#
# arr = {3, 34, 4, 12, 5, 2}, sum = 9
# ans = True
#
# Recursive Solution
def subset_sum_recursive(n, arr, sum):
  if n == 0:
    return True

  if arr[n-1] <= sum:
    return (subset_sum_recursive(n-1, arr, sum-arr[n-1]) or
      subset_sum_recursive(n-1, arr, sum))
  else:
    return subset_sum_recursive(n-1, arr, sum)

def subset_sum(arr, sum):
  return subset_sum_recursive(len(arr), arr, sum)

# Memoize recursive solution
def subset_sum(arr, sum):
  N = len(arr)
  mem = [[None for c in range(sum+1)] for r in range(N+1)]

  def subset_sum_memoized(n, arr, sum):
    if n == 0:
      return True

    if not mem[n][sum] is None:
      return mem[n][sum]

    if arr[n-1] <= sum:
      mem[n][sum] = (subset_sum_memoized(n-1, arr, sum-arr[n-1]) or
        subset_sum_memoized(n-1, arr, sum))
    else:
      mem[n][sum] = subset_sum_memoized(n-1, arr, sum)

    return mem[n][sum]

  return subset_sum_memoized(len(arr), arr, sum)

# Memoize recursive solution
# Top Down Tabulation
def subset_sum_tabulation(arr, sum):
  N = len(arr)
  dp = [[None for c in range(sum+1)] for r in range(N+1)]

  for i in range(N+1):
    for j in range(sum+1):
      # Empty Subset will give 0 sum
      if j == 0:
        dp[i][j] = True
      elif i == 0:
        dp[i][j] = False
      # ith element can be chosen
      elif arr[i] <= j:
        dp[i][j] = dp[i-1][j-arr[i]] || dp[i-1][j]
      # ith element cannot be chosen so check if
      # solution possible from previous set
      else:
        dp[i][j] = dp[i-1][j]

  return dp[N][sum]