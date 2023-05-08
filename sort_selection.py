# sort#
# selection sort# Time-O(N*N); Space-O(N)
list = [64, 25, 12, 22, 11]
for i in range(len(list)):
    # At first, pretend the first element is the minimum one,
    # so the min_idx is i(from 0 to len(list)-1).
    min_idx = i
    # compare the first ele with the following ele on by one
    # to find the minimum ele and its index
    # For example, when i=0,j=1, 64>25, 25 is small, so min_idx=j=1;
    # when i=0,j=2, 25>12,12 is small, so min_idx=j=2;
    # when i=0,j=3, 12<22, min_idx still equal 2, which means we don't move it,
    # and then j=4, 12>11, min_ind=j=4. Now, we find the smallest ele's index, whcih is 4
    for j in range(i+1, len(list)):
        if list[min_idx] > list[j]:
            min_idx = j
        # we swap the list[i] and smallest ele:
    list[i], list[min_idx] = list[min_idx], list[i]
for i in range(len(list)):
    print(list[i], end=" ")
