# x: h e a p
# y: e a p
#
# Top Down Tabulation
def insert_delete_lcs(x, y):
  M = len(x)
  N = len(y)

  dp = [[0 for c in range(N+1)] for r in range(M+1)]

  for r in range(M+1):
    for c in range(N+1):
      if r == 0 or c == 0:
        dp[r][c] = max(r, c)
      elif x[r-1] == y[c-1]:
        dp[r][c] = dp[r-1][c-1]
      else:
        dp[r][c] = min(dp[r-1][c], dp[r][c-1]) + 1

  return dp[M][N]

#   @ h e a p
# @ 0 1 2 3 4
# e 1 2 1 2 3
# a 2 3 2 1 3
# p 3 4 3 3 1
#
#   @ h e a p
# @ 0 1 2 3 4
# p 1 2 3 4 3
# e 2 3 2 3 4
# a 3 4 3 2 3