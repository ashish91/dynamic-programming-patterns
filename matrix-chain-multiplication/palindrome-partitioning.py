# Recursive Solution
def is_palindrome(s):
  return s == s[::-1]

def min_palindrom_partition_recursive(s, i, j):
  if i >= j:
    return 0

  if is_palindrome(s[i:j+1]):
    return 0

  min_cuts = float('inf')
  for k in range(i,j):
    min_cuts = min(min_cuts, min_palindrom_partition_recursive(i,k)+min_palindrom_partition_recursive(k+1,j)+1)

  return min_cuts

def min_palindrome_partition(s):
  N = len(s)
  min_palindrom_partition_recursive(s, 0, N-1)

# Memoized solution
def is_palindrome(s):
  return s == s[::-1]

def min_palindrome_partition(s):
  N = len(s)

  dp = [[-1 for r in range(N)] for c in range(N)]
  def min_palindrom_partition_memoized(s, i, j):
    nonlocal dp
    if i >= j:
      return 0

    if is_palindrome(s[i:j+1]):
      return 0

    if dp[i][j] >= 0:
      return dp[i][j]

    min_cuts = float('inf')
    for k in range(i,j):
      min_cuts = min(min_cuts, min_palindrom_partition_memoized(i,k)+min_palindrom_partition_memoized(k+1,j)+1)

    dp[i][j] = min_cuts
    return dp[i][j]
  min_palindrom_partition_memoized(s, 0, N-1)
