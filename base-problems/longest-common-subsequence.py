# X: a b c d g h
# Y: a b e d f h r
#
# Write down a Recursive Solution
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
