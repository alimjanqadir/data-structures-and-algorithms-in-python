class KnapsackProblemSolver(object):
    def __init__(self, items, weight_limit):
        self.items = items
        self.weight_limit = weight_limit
        self.permutation_count = 0

    def naive_iteratively(self):
        knapsack = []
        knapsack_weight = 0
        knapsack_value = 0
        max_value = 0
        self.permutation_count += 1
        print("knapsack value: " + str(knapsack))
        for x in range(len(self.items)):
            # Current item properties.
            nth_item = self.items[x]
            nth_item_weight = nth_item[0]
            nth_item_value = nth_item[1]
            # Knapsack properties.
            knapsack = [nth_item]
            knapsack_weight = nth_item_weight
            knapsack_value = nth_item_value
            if knapsack_weight <= self.weight_limit and max_value < knapsack_value:
                max_value = knapsack_value
            self.permutation_count += 1
            print("knapsack value: " + str(knapsack))
            for y in range(x):
                knapsack = [nth_item]
                knapsack_weight = nth_item_weight
                knapsack_value = nth_item_value

                item_y = self.items[y]
                item_y_weight = item_y[0]
                item_y_value = item_y[1]

                knapsack.append(item_y)
                knapsack_weight += item_y_weight
                knapsack_value += item_y_value

                if knapsack_weight <= self.weight_limit and max_value < knapsack_value:
                    max_value = knapsack_value

                self.permutation_count += 1
                print("knapsack value: " + str(knapsack))
                previous_subset = list(knapsack)
                previous_subset_weight = knapsack_weight
                previous_subset_value = knapsack_value
                for z in range(y):
                    knapsack = list(previous_subset)
                    knapsack_weight = previous_subset_weight
                    knapsack_value = previous_subset_value
                    item_z = self.items[z]
                    item_z_weight = item_z[0]
                    item_z_value = item_z[1]
                    knapsack.append(item_z)
                    knapsack_weight += item_z_weight
                    knapsack_value += item_z_value

                    if knapsack_weight <= self.weight_limit and max_value < knapsack_value:
                        max_value = knapsack_value

                    self.permutation_count += 1
                    print("knapsack value: " + str(knapsack))
                    previous_subset = list(knapsack)
                    previous_subset_weight = knapsack_weight
                    previous_subset_value = knapsack_value
                    for a in range(z):
                        knapsack = list(previous_subset)
                        knapsack_weight = previous_subset_weight
                        knapsack_value = previous_subset_value
                        item_a = self.items[a]
                        item_a_weight = item_a[0]
                        item_a_value = item_a[1]

                        knapsack.append(item_a)
                        knapsack_weight += item_a_weight
                        knapsack_value += item_a_value

                        if knapsack_weight <= self.weight_limit and max_value < knapsack_value:
                            max_value = knapsack_value
                        self.permutation_count += 1
                        print("knapsack value: " + str(knapsack))
        return max_value

    def naive_recursively(self):
        return self._naive_recursive_helper(self.weight_limit, len(self.items))

    def _naive_recursive_helper(self, weight_limit, n):
        if weight_limit <= 0 or n <= 0:
            return 0

        self.permutation_count += 1
        # Nth item value and weight
        nth_item = self.items[n - 1]
        nth_item_weight = nth_item[0]
        nth_item_value = nth_item[1]

        # Skip if nth item weight is higher than weight_limit
        if nth_item_weight > weight_limit:
            return self._naive_recursive_helper(
                weight_limit,
                n - 1)
        else:
            # If weight is smaller than the limit,
            # use nth item in to subset.

            # Find the subset that don't include nth item
            result_nth_item_not_included = self._naive_recursive_helper(
                weight_limit,
                n - 1)

            result_nth_item_included = nth_item_value + self._naive_recursive_helper(
                # Remove nth item weight
                weight_limit - nth_item_weight,
                n - 1)

            if result_nth_item_included >= result_nth_item_not_included:
                result = result_nth_item_included
            else:
                result = result_nth_item_not_included
        return result

    def dynamic_recursively(self):
        return self._recursive_solution_dynamic_helper(self.weight_limit, len(self.items))

    def _recursive_solution_dynamic_helper(self, weight_limit, n, dp=None):
        # Initialize default parameter
        if dp is None:
            dp = [[0 for x in range(weight_limit)] for x in range(len(self.items))]

        # Base case
        if n <= 0 or weight_limit <= 0:
            return 0

        if dp[n - 1][weight_limit - 1] != 0:
            return dp[n - 1][weight_limit - 1]

        # Nth item value and weight
        nth_item = self.items[n - 1]
        nth_item_weight = nth_item[0]
        nth_item_value = nth_item[1]

        # Skip if nth item weight is higher than weight_limit
        if nth_item_weight > weight_limit:
            return self._recursive_solution_dynamic_helper(
                weight_limit,
                n - 1, dp)
        else:
            # If weight is not higher than the limit,
            # use nth item in to subset.

            # Find the subset that don't include nth item
            result_nth_item_not_included = self._recursive_solution_dynamic_helper(weight_limit, n - 1, dp)
            # Find the subset that include nth item
            result_nth_item_included = nth_item_value + self._recursive_solution_dynamic_helper(
                weight_limit - nth_item_weight, n - 1, dp)

            max_value = max(result_nth_item_not_included, result_nth_item_included)
            dp[n - 1][weight_limit - 1] = max_value
            return max_value


# array = [(1, 3), (3, 5), (5, 7), (7, 9), (2, 10), (4, 12)]
# knapsack_problem = KnapsackProblemSolver(array, 19)
array = [(1, 3), (3, 5), (5, 7), (7, 9), (2, 10), (2, 12), ]
knapsack_problem = KnapsackProblemSolver(array, 1000000000)
print(knapsack_problem.naive_iteratively())
print(knapsack_problem.permutation_count)
knapsack_problem.permutation_count = 0
print(knapsack_problem.naive_recursively())
print(knapsack_problem.permutation_count)
# print(knapsack_problem.dynamic_recursively())
# print(knapsack_problem.permutation_count)
