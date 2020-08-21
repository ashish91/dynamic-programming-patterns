# weights: 10  5 2  9 24
# values :  8 10 1 18 20
#
# Recursive Solution
def knapsack_recursive(weights, values, capacity, index):
	if (capacity == 0 or index == 0):
		return 0

	if (weights[index] > capacity):
		return knapsack_recursive(weights, values, capacity, index - 1)
	else:
		return max(values[index] + knapsack_recursive(weights, values, capacity - weights[index], index - 1),
								knapsack_recursive(weights, values, capacity - weights[index], index - 1))

def knapsack(weights, values, N):
	return knapsack_recursive(weights, values, N, len(weights) - 1)

# Memoization
