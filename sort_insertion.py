# sort#
# insertion sort# Time-O(N*N);Space - O(1)
list = [64, 25, 12, 22, 11]
# i will start from the second ele
for i in range(1, len(list)):
    # make a record for list[i]
    j = i
    while j > 0 and list[j-1] > list[j]:
        list[j-1], list[j] = list[j], list[j-1]
        j -= 1

print(list)
