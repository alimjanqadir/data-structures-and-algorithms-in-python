def binary_search(input_array, value):
    """Your code goes here."""
    input_length = len(input_array)
    if input_length == 0:
        return -1

    left = 0
    right = input_length - 1
    while left <= right:
        mid_point = (left + right) / 2
        value_in_middle = input_array[mid_point]

        if value_in_middle == value:
            return mid_point

        if value_in_middle < value:
            left = mid_point + 1
        elif value_in_middle > value:
            right = mid_point - 1
        else:
            return mid_point
    return -1


test_list = [-4, 1, 3, 9, 11, 15, 19, 29, 43, 55, 234, 34234, 144444]
test_val1 = -4
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)
