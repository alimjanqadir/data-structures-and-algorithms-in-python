def binary_search(input_array, value):
    input_length = len(input_array)
    if input_length == 0:
        return -1

    sorted_array = sorted(input_array)
    start = 0
    end = input_length - 1
    print(sorted_array)
    while start <= end:
        mid_point = (start + end) // 2
        value_in_middle = sorted_array[mid_point]

        if value < value_in_middle:
            end = mid_point - 1
        elif value > value_in_middle:
            start = mid_point + 1
        else:
            return mid_point
    return -1


test_list = [2, 5, 7, 9, 12]
test_val2 = 12
print(binary_search(test_list, test_val2))
