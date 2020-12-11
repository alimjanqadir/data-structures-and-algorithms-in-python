"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


def quicksort1(start, end, array, ):
    array_length = len(array)

    # Return empty array when array is empty
    if array_length == 0:
        return []

    # Finish the recursion when both pointers in one position
    if start == end:
        return

    # Finish the recursion when iteration is outof boundry
    if start == end or start < 0 or end < 0 or \
            start > array_length - 1 or end > array_length - 1:
        return

    # The last element selected as pivot by default
    pivot = end
    left = start

    while left < pivot:
        if array[left] > array[pivot]:
            temp = array[left]
            array.insert(pivot + 1, temp)
            array.pop(left)
            pivot -= 1
        else:
            left += 1

    quicksort1(start, pivot - 1, array)
    quicksort1(pivot + 1, array_length - 1, array)

    return array


def quicksort(array):
    return quicksort1(0, len(array) - 1, array)


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
test1 = [22, 11, 3, 6, 25, 32, 31, 71, 88, 1]
print(quicksort(test))
print(quicksort(test1))
