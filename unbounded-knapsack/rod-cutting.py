# length: 10  5 2  9 24
# price :  8 10 1 18 20
# L : 10
#
# Write down a Recursive Solution
def rod_cutting_recursive(n, L, length, price):
  if n == 0 || L == 0:
    return 0

  if length[n-1] <= L:
    return max(length[n-1] + rod_cutting_recursive(n, L-length[n-1], length, price),
      rod_cutting_recursive(n-1, L, length, price))
  else:
    return rod_cutting_recursive(n-1, L, length, price)

def rod_cutting(length, price, L):
  N = len(length)
  rod_cutting_recursive(N, L, length, price)

# Memoize the above recursive solution
def rod_cutting(length, price, L):
  N = len(length)
  mem = [[-1 for c in range(L+1)] for r in range(N+1)]

  def rod_cutting_memoization(n, L, length, price):
    if n == 0 || L == 0:
      return 0

    if mem[n][L] >= 0:
      return mem[n][L]

    if length[n-1] <= L:
      mem[n][L] = max(length[n-1] + rod_cutting_recursive(n, L-length[n-1], length, price),
        rod_cutting_recursive(n-1, L, length, price))
    else:
      mem[n][L] = rod_cutting_recursive(n-1, L, length, price)

    return mem[n][L]

  return rod_cutting_memoization(N, L, length, price)

# Top Down Tabulation
def rod_cutting_tabulation(length, price, L):
  N = len(length)
  dp = [[-1 for c in range(L+1)] for r in range(N+1)]

  for n in range(N+1):
    for l in range(L+1):
      if l == 0 or n == 0:
        dp[n][l] = 0
      elif length[n] <= l:
        dp[n][l] = max(dp[n-1][l], length[n-1] + dp[n][l-length[n-1]])
      else:
        dp[n][l] = dp[n-1][l]

  return dp[N][L]