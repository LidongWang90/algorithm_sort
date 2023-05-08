def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide the array in half and sort each half recursively
    else:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        left_half = merge_sort(left_half)
        right_half = merge_sort(right_half)

    # Merge the sorted halves back together
        return merge(left_half, right_half)


def merge(left_half, right_half):
    merged = []
    i = j = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            merged.append(left_half[i])
            i += 1
        else:
            merged.append(right_half[j])
            j += 1

    # Add any remaining elements from the left or right half
    merged += left_half[i:]
    merged += right_half[j:]

    return merged


arr = [5, 2, 1, 4, 8, 7, 6]
sorted_arr = merge_sort(arr)
print(sorted_arr)  # Output: [1, 2, 3, 4, 5]
