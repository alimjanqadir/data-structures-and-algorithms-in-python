def sort(array):
    return _bubble_sort(array)


def _bubble_sort(array):
    copy = list(array)
    unsorted_element_count = len(copy)
    while unsorted_element_count > 0:
        i = 0
        j = i + 1
        for _ in range(unsorted_element_count - 1):
            if copy[i] > copy[j]:
                _swap(copy, j, i)
            i += 1
            j += 1
        unsorted_element_count -= 1
    return copy


def _swap(array, a, b):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp


print(sort([3, 4, 2, 3, 1, 0]))
