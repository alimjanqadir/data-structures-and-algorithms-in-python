import sys
class KnapsackProblem(object):

    def __init__(self, items):
        self.items = items

    def brute_force(self, weight_limit):
        knapsack = {}
        sum_weight = sys.maxsize
        sum_value = 0

        for i in xrange(0, len(self.items)):
            current_item = self.items[i]
            current_item_value = current_item[0]
            current_item_weight = current_item[1]

            if current_item_weight <= weight_limit and \
                    current_item_value >= sum_value:
                knapsack = {}
                knapsack[i] = current_item
                sum_value = current_item_value
                sum_weight = current_item_weight

            for j in xrange(i + 1, len(self.items)):
                compared_item = self.items[j]
                compared_item_value = compared_item[0]
                compared_item_weight = compared_item[1]

                if current_item_weight > weight_limit or \
                        compared_item_weight > weight_limit:
                    continue

                calculated_weight = current_item_weight + compared_item_weight
                calculated_value = current_item_value + compared_item_value
                if calculated_weight > weight_limit:
                    continue

                test_value = knapsack.get(i, (0, 0))[1]

                if (calculated_weight + sum_weight) - test_value \
                        <= weight_limit:
                    knapsack[j] = compared_item
                    sum_weight += compared_item_weight
                    sum_value += compared_item_value
                else:
                    if calculated_weight <= weight_limit and \
                            calculated_value > sum_value:
                        sum_weight = calculated_weight
                        sum_value = calculated_value
                        knapsack = {}
                        knapsack[i] = current_item
                        knapsack[j] = compared_item
        return knapsack


knapsack_problem = KnapsackProblem(
    [(12, 8), (4, 4), (2, 3), (13, 13), (2, 4)])

print knapsack_problem.brute_force(15)
