import sys


class KnapsackProblem(object):
    def __init__(self, items):
        self.items = items

    def naive_recursive_solution(self, weight_limit):
        return self._naive_recursive_helper(
            weight_limit,
            len(self.items))

    def _naive_recursive_helper(self, weight_limit, n, knapsack=None, dp=None):
        # Initialize default value
        if knapsack is None:
            knapsack = {'value': 0, 'items': []}
        # Base case
        if n == 0 or weight_limit == 0:
            return knapsack

        # Nth item value and weight
        nth_item = self.items[n - 1]
        nth_item_value = nth_item[0]
        nth_item_weight = nth_item[1]

        # Skip if nth item weight is higher than weight_limit
        if nth_item_weight > weight_limit:
            return self._naive_recursive_helper(
                weight_limit,
                n - 1,
                knapsack)
        else:
            # If weight is not higher than the limit,
            # use nth item in to subset.

            # Find the subset that don't include nth item
            result_nth_item_not_included = self._naive_recursive_helper(
                weight_limit,
                n - 1,
                # Pass knapsack that doesn't include nth item
                knapsack)

            # Find the subset that include nth item
            # Copy the list and create a new instance to avoid side effects
            knapsack_items_nth_item_included = list(knapsack["items"])
            knapsack_items_nth_item_included.append(self.items[n - 1])
            knapsack_items_nth_item_value_included = \
                knapsack["value"] + nth_item_value

            result_nth_item_included = self._naive_recursive_helper(
                # Remove nth item weight
                weight_limit - nth_item_weight,
                n - 1,
                # Pass knapsack that include nth item
                {
                    'value': knapsack_items_nth_item_value_included,
                    'items': knapsack_items_nth_item_included
                })
            # Get the result in two different subsets and return the subset
            # with higher value
            value_nth_item_included = result_nth_item_included
            value_nth_item_not_included = result_nth_item_not_included

            if value_nth_item_included >= value_nth_item_not_included:
                result = result_nth_item_included
            else:
                result = result_nth_item_not_included
            return result

    def dynamic_solution(self, weight_limit):

        return


array = [(3, 1), (5, 3), (7, 5), (9, 7)]
knapsack_problem = KnapsackProblem(array)
print knapsack_problem.naive_recursive_solution(7)
