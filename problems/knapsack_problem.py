class KnapsackProblemSolver(object):
    def __init__(self, items, weight_limit):
        self.items = items
        self.weight_limit = weight_limit
        self.permutation_count = 0

    def naive_iteratively(self):
        nth_item = 0
        knapsack = [0 for x in range(len(self.items))]
        stack = [nth_item]
        max_value = 0
        while stack:
            index = stack.pop()
            if index >= len(self.items):
                continue

            # Include current item
            item = self.items[index]
            knapsack[index] = item
            # Calculate included knapsack and update the max value
            knapsack_value, knapsack_weight = self.__calculate_knapsack_weight_and_value(knapsack)
            if knapsack_weight <= self.weight_limit and knapsack_value > max_value:
                max_value = knapsack_value

            # Clean up knapsack for next iteration
            # Todo(Clean knapsack has problems)
            knapsack = self.__clean_knapsack(index, knapsack, stack)

            # Add subsequent calculations to the stack
            stack, nth_item = self.__append_subsequent_calculations_to_stack(index, nth_item, stack)

        return max_value

    def __append_subsequent_calculations_to_stack(self, index, nth_item, stack):
        stack_copy = list(stack)
        nth_item_copy = nth_item
        if index < 0:
            raise ValueError('incorrect index')

        if 0 < index:
            for x in reversed(range(index)):
                stack_copy.append(x)
        else:
            if not stack:
                nth_item_copy += 1
                stack_copy.append(nth_item_copy)
        return stack_copy, nth_item_copy

    def __clean_knapsack(self, index, knapsack, stack):
        if index == 0:
            if stack:
                knapsack = self.__partial_cleanup(knapsack, stack)
            else:
                knapsack = self.__full_cleanup()
        return knapsack

    def __partial_cleanup(self, knapsack, stack):
        copy = list(knapsack)
        top = stack[-1]
        for x in range(top):
            copy[x] = 0
        return copy

    def __full_cleanup(self):
        return [0 for x in range(len(self.items))]

    def __calculate_knapsack_weight_and_value(self, knapsack):
        copy = list(knapsack)
        knapsack_weight, knapsack_value = 0, 0
        for item in copy:
            if isinstance(item, int):
                continue
            item_weight, item_value = item
            knapsack_weight += item_weight
            knapsack_value += item_value
        return knapsack_value, knapsack_weight

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
            dp = [[0 for _ in range(weight_limit)] for _ in range(len(self.items))]

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


array = [(1, 3), (3, 5), (5, 7), (4, 12), (2, 10), (4, 12), (2, 10), (4, 12), (2, 10), (4, 12)]
knapsack_problem = KnapsackProblemSolver(array, 10)
print(knapsack_problem.naive_iteratively())
print(knapsack_problem.naive_recursively())
print(knapsack_problem.dynamic_recursively())
