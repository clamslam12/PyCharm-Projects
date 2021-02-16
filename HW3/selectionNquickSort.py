import random
'''
This function applies selection sort to sort an list A in increasing order
Input: a list A
Output: None, but the list A will be sorted in increasing order
'''

def selectionSort(A):
    for i in range(len(A) - 1): # for each element minus the last because it is trivially sorted
        min = i # set minimum value to first index
        for j in range(i + 1, len(A)): # for each element starting from i+1 to end of list
            if A[j] < A[min]:
                min = j
        if(min != i): # if the minimum value is not located at index i, else it is in the right place
            A[i], A[min] = A[min], A[i]


'''
This function generates 20 random numbers between 1-50
Input: None
Output: returns a list of 20 random numbers between 1-50
'''
def randlist():
    l = []
    for x in range(20):
        l.append(random.randint(1,50))
    return l

'''
This function will choose the first element in the list as pivot and partition values that are <= pivot to 
the left and values > pivot to the right.
Input: a list, lower bound index, upper bound index
Output: the index of the pivot after partitioning
'''
def partition(A, lb, ub):
    pivot = A[lb]
    start = lb
    end = ub
    while start < end:
        while A[start] <= pivot and start < end:
            start += 1
        while A[end] > pivot:
            end -= 1
        if start < end: # check again to see if start < end after incrementing start
            A[start], A[end] = A[end], A[start] # swap value at index start with value at index end
    A[lb], A[end] = A[end], A[lb] # swap the value at index end with value at index lb; value at index end = pivot
    return end  # returns the index of pivot

"""
This function applies the partition function to find the index of the pivot and recursively calls itself to partition
until the lower bound is > upper bound
Input: a list A, lower bound index, upper bound index
Output: None but the list A will be sorted in increasing order
"""
def quickSort(A, lb, ub):
    if lb < ub:
        pivIndx = partition(A, lb, ub)
        quickSort(A, lb, pivIndx - 1) # partition the left half of pivot
        quickSort(A, pivIndx + 1, ub) # partition the right half of pivot


randNum = randlist()
selectionSort(randNum)
print("applying selection sort...")
for x in randNum:
    print(x)

randNum2 = randlist()
quickSort(randNum2, 0, len(randNum2) - 1)
print("applying quick sort...")
for x in randNum2:
    print(x)