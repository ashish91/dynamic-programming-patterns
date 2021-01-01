# X: a b c d g h
# Y: a b e d f h r
#
# Recursive Solution
def lcs_recursive(x, y, r, c):
  if r == 0 || c == 0:
    return 0

  if x[r-1] == y[c-1]:
    return 1 + lcs_recursive(x, y, r-1, c-1)
  else:
    return max(lcs_recursive(x, y, r-1, c), lcs_recursive(x, y, r, c-1))

def lcs(x, y):
  R = len(x)
  C = len(y)
  return lcs_recursive(x, y, R, C)

# Memoize recursive Solution
def lcs(x, y):
  R = len(x)
  C = len(y)
  mem = [[-1 for c in range(C+1)] for r in range(R+1)]

  def lcs_memoized(x, y, r, c):
    nonlocal mem
    if r == 0 || c == 0:
      return 0
    if mem[r][c] != -1:
      return mem[r][c]

    if x[r-1] == y[c-1]:
      mem[r][c] = 1 + lcs_memoized(x, y, r-1, c-1)
    else:
      mem[r][c] = max(lcs_memoized(x, y, r-1, c), lcs_memoized(x, y, r, c-1))

  return lcs_memoized(x, y, R, C)

# X: a b c d g h
# Y: a b e d f h r
# Top Down Tabulation
def lcs_tabulation(x, y):
  M = len(x)
  N = len(y)

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

# dp[i][j] = 1+dp[i-1][j-1] if x[i] == y[i]
#          = max(dp[i-1][j], dp[i][j-1]) if x[i] != y[i]
#
#   @ a b c d g h
# @ 0 0 0 0 0 0 0
# a 0 1 1 1 1 1 1
# b 0 1 2 2 2 2 2
# e 0 1 2 2 2 2 2
# d 0 1 2 2 3 3 3
# f 0 1 2 2 3 3 3
# h 0 1 2 2 3 3 4
# r 0 1 2 2 3 3 4

