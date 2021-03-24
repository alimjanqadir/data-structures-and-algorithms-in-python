def quicksort(collection: list) -> list:
    copy = collection.copy()

    def quicksort_helper(low: int, high: int) -> list:
        if low >= high:
            return copy

        i = low
        j = high
        pivot = (low + high) // 2
        while i < j:
            while copy[i] > copy[pivot]:
                copy.insert(pivot, copy.pop(i))
                pivot -= 1
            else:
                i += 1

            while copy[j] < copy[pivot]:
                copy.insert(pivot, copy.pop(j))
                pivot += 1
            else:
                j -= 1

        quicksort_helper(0, pivot - 1)
        quicksort_helper(pivot + 1, high)

        return copy

    return quicksort_helper(0, len(collection) - 1)


print(quicksort([9, 7, 5, 3, 2, 1]))
print(quicksort([]))
print(quicksort([0, 0, 0, 0, 0]))
print(quicksort([2, 2, 0, 0, -1, -1]))
