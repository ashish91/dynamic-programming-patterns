# x: A G G T A B
# y: G X T X A Y B
#
# Top Down Tabulation

def shortest_common_supersequence(x, y):
  M = len(x)
  N = len(y)

  dp = [[0 for c in range(N+1)] for r in range(M+1)]

  for r in range(M+1):
    for c in range(N+1):
      if r == 0 or c == 0:
        dp[r][c] = max(r, c)
      elif x[r] == y[c]:
        dp[r][c] = 1+dp[r-1][c-1]
      else:
        dp[r][c] = 1+min(dp[r-1][c], dp[r][c-1])

  return dp[M][N]

#  @ G X T X A Y B
#@ 0 1 2 3 4 5 6 7
#A 1 2 3 4 5 5 6 7
#G 2 2 3 4 5 6 7 8
#G 3 3 4 5 6 7 8 9
#T 4 4 5 5 6 7 8 9
#A 5 5 6 6 7 7 8 9
#B 6 6 7 7 8 8 9 9

