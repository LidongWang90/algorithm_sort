# sort#
# insertion sort# Time-O(N*N);Space - O(1)
list = [64, 25, 12, 22, 11]
# i will start from the second ele
for i in range(1, len(list)):
    # make a record for list[i]
    key = list[i]
    # compare key and left ele, if left one is bigger than key,
    # make list[j+1] be the bigger one. But, key is not changed.
    # Then, cursor move to left to compare to make a partial sorted.
    # Need to draw pic to show the process
    j = i - 1
    while j >= 0 and list[j] > key:
        list[j+1] = list[j]
        j -= 1
    list[j+1] = key
for i in range(len(list)):
    print(list[i], end=" ")
