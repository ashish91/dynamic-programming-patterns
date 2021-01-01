# coin denominations: 1 5 15
# sum : 20
#
# Write down a Recursive Solution
def total_coin_change_recursive(n, S, denominations):
  if n == 0 || S == 0:
    return 1 if S == 0 else 0

  if denominations[n-1] <= S:
    return total_coin_change_recursive(n, S-denominations[n-1], denominations) +
      total_coin_change_recursive(n-1, S, denominations)
  else:
    return total_coin_change_recursive(n-1, S, denominations)

def total_coin_change(denominations, S):
  N = len(denominations)
  total_coin_change_recursive(N, denominations, S)

# Memoize the above recursive solution
def total_coin_change(denominations, S):
  N = len(denominations)
  mem = [[-1 for c in range(S+1)] for r in range(N+1)]

  def total_coin_change_memoization(n, L, length, price):
    if n == 0 || S == 0:
      return 1 if S == 0 else 0

    if mem[n][S] >= 0:
      return mem[n][S]

    if denominations[n-1] <= S:
      mem[n][S] = total_coin_change_memoization(n, S-denominations[n-1], denominations) +
        total_coin_change_memoization(n-1, S, denominations)
    else:
      mem[n][S] = total_coin_change_memoization(n-1, S, denominations)

    return mem[n][L]

  return total_coin_change_memoization(N, L, denominations)

# Top Down Tabulation
def total_coin_change_tabulation(denominations, S):
  N = len(denominations)
  dp = [[0 for c in range(S+1)] for r in range(N+1)]

  for n in range(N+1):
    for s in range(S+1):
      if s == 0:
        dp[n][s] = 1
      elif n == 0:
        dp[n][s] = 0
      elif length[n] <= s:
        dp[n][s] = dp[n-1][s] + dp[n][s-denominations[n-1]]
      else:
        dp[n][s] = dp[n-1][s]

  return dp[N][S]