//
// Inputs:
//    A : an input array
//    l : the index of the leftmost value (the pivot)
//    r : the index of the rightmost value
// Note: the indices l,r (inclusive) define a subarray of A
//
// Outputs:
//    1 : the index of the pivot after partitioning
//    2 : the number of comparisons that were performed
// Note: if you want to calculate the number of comparisons using a
//       global variable then you only need the first output.
//
PARTITION(A, left_index, right_index)
    pivot = A[left_index]
    i = left_index + 1
    for j = left_index + 1 to right_index
        if A[j] < pivot
            swap A[j] and A[i]
            increment i
    swap A[left_index] and A[i-1]
    return i-1, right_index-left_index
'''
prompt > ./main.py
Please enter a filename:
ordered-10.txt
Please enter a Quicksort variant:
first
45

prompt > ./main.py
Please enter a filename:
ordered-10.txt
Please enter a Quicksort variant:
median3
19

prompt > ./main.py
Please enter a filename:
ordered-10.txt
Please enter a Quicksort variant:
random
25
'''
