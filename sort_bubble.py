# sort#
# bubble sort# Time-O(N*N);
list = [64, 25, 12, 22, 11]
for i in range(len(list)):
    # compare two ele from the first ele. if left ele
    # is smaller than the next one, swap, to put the biggest
    # one into the left end. In next round, continue to compare
    # except for the left end ele.
    for j in range(len(list)-i-1):
        if list[j] > list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]

for i in range(len(list)):
    print(list[i], end=" ")
