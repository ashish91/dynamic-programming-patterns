# You have d dice, and each die has f faces numbered 1, 2, ..., f.
# Return the number of possible ways (out of fd total ways) modulo 10^9 + 7
# to roll the dice so the sum of the face up numbers equals target.

# Example 1:

# Input: d = 1, f = 6, target = 3
# Output: 1
# Explanation:
# You throw one die with 6 faces.  There is only one way to get a sum of 3.
# Example 2:

# Input: d = 2, f = 6, target = 7
# Output: 6
# Explanation:
# You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
# 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
# Example 3:

# Input: d = 2, f = 5, target = 10
# Output: 1
# Explanation:
# You throw two dice, each with 5 faces.  There is only one way to get a sum of 10: 5+5.
# Example 4:

# Input: d = 1, f = 2, target = 3
# Output: 0
# Explanation:
# You throw one die with 2 faces.  There is no way to get a sum of 3.
# Example 5:

# Input: d = 30, f = 30, target = 500
# Output: 222616187
# Explanation:
# The answer must be returned modulo 10^9 + 7.


# Constraints:

# 1 <= d, f <= 30
# 1 <= target <= 1000

# Basic Recursive Solution
# ========================
class Solution:
  def recursive(self, d, f, target):
    if d == 0 or target <= 0:
      return 1 if (d == 0 and target == 0) else 0

    ways = 0
    for i in range(1, f+1):
      ways = (ways + self.recursive(d-1, f, target - i)) % 1000000007

    return ways

  def numRollsToTarget(self, d: int, f: int, target: int) -> int:
    return self.recursive(d, f, target)

# Time Complexity: O(f^d). We're checking all permutations and returning the
# number of valid dice moves which results in the sum.
#
# Space Complexity: O(d). We create a f-ary tree with height as d. So the
# call stack size will be d.

# Top Down DP Solution
# ====================

class Solution:
  def __init__(self):
    self.dp = [[None for i in range(1001)] for j in range(31)]

  def topDown(self, d, f, target):
    if d == 0 or target <= 0:
      return 1 if (d == 0 and target == 0) else 0

    if self.dp[d][target] is not None:
      return self.dp[d][target]

    ways = 0
    for i in range(1, f+1):
      ways = (ways + self.topDown(d-1, f, target - i)) % 1000000007
    self.dp[d][target] = ways

    return ways

  def numRollsToTarget(self, d: int, f: int, target: int) -> int:
    return self.topDown(d, f, target)

# Time Complexity: O(f*d*target). We're checking all possible combinations only once.
#
# Space Complexity: O(d*target). We create a f-ary tree with height as d. So the
# call stack size will be d.


# Bottom Up DP Solution
# ====================

class Solution:

  def bottomUp(self, d, f, target):
    dp = [[0 for c in range(target+1)] for r in range(d+1) ]
    dp[0][0] = 1

    for i in range(1, d+1):
      for j in range(1, f+1):
        for k in range(j, target+1):
          dp[i][k] = (dp[i][k] + dp[i-1][k-j]) % 1000000007

    return dp[d][target]

  def numRollsToTarget(self, d: int, f: int, target: int) -> int:
    return self.bottomUp(d, f, target)

# Time Complexity: O(f*d*target). We're checking all possible combinations only once.
#
# Space Complexity: O(d*target). We create a f-ary tree with height as d. So the
# call stack size will be d.

# Bottom Up Push DP Solution
# ==========================

class Solution:

  def pushBottomUp(self, d, f, target):
    dp = [ 0 for i in range(target+1) ]
    dp[target+1] = 1

    i = j = k = 0
    for i in range(1, d+1):
      k = target
      while (i == d and k >= target) or (i != d and k >= 0):
        j = k - 1
        dp[k] = 0
        while j >= max(0, k - f):
          dp[k] = (dp[k] + dp[j]) % 1000000007;
          j -= 1
        k -= 1

    return dp[d][target]

  def numRollsToTarget(self, d: int, f: int, target: int) -> int:
    return self.pushBottomUp(d, f, target)

# Time Complexity: O(f*d*target). We're checking all possible combinations only once.
#
# Space Complexity: O(d*target). We create a f-ary tree with height as d. So the
# call stack size will be d.
