def sort(array):
    return __merge_sort(array)


def __merge_sort(array):
    if len(array) < 2:
        return array

    mid = len(array) // 2
    left = __merge_sort(array[: mid])
    right = __merge_sort(array[mid:])
    return __merge_results(left, right)


def __merge_results(left_array, right_array):
    array = []
    while left_array and right_array:
        if left_array[0] <= right_array[0]:
            array.append(left_array.pop(0))
        else:
            array.append(right_array.pop(0))
    return [*array, *right_array, *left_array]


print(sort([3, 5, 7, 9, 2, 1]))
print(sort([-1, -5, 0, -9, 10]))
print(sort([]))
print(sort([-1, 3, -10]))
