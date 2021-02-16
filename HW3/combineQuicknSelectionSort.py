import time

'''
This function calculates time taken to execute an input function
Input: a function
Output: prints start time, end time, and time taken 
'''
def quickNselectTimer(func):
    # (could not use time.time() or time.process_time() due to having the same start and end times)
    start = time.perf_counter()
    print(f'starts at: {start}')
    func
    end = time.perf_counter()
    print(f'ends at: {end}')
    print(f'time taken: {end - start}')
'''
This function imports a text file and converts all numbers into integers and stores them in a list
Input: A list to store the numbers and file name
Output: Returns a list of imported numbers
'''
def importFile(randL, fname):
    with open(fname, mode="r") as inFile:
        for line in inFile:
            l1 = line.strip('\n').split(" ") # strip \n at every line and split spaces to put in a list
            for i, val in enumerate(l1):
                if val == '\n':
                    l1.remove(val)
            randL.extend(l1)
    # filters out " in list
    randL = list(filter(None, randL))
    # converts str to int for every element in list
    for i, val in enumerate(randL):
        j = int(val)
        randL[i] = j
    return randL

rand1MList = []
rand1MList = importFile(rand1MList, "rand1000000.txt")

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
'''
This function returns the nth largest element in a list. It uses partition in quicksort to determine if the nth largest
is to the left or right of pivot, then recursively call itself with the left sublist or right sublist as input. If the 
pivot is the nth largest is the pivot, then it just returns the pivot itself
Input: A list and the nth largest one wants to find. If the first largest then n = 1
Output: Returns the nth largest element in a list
'''
def nthlargest(A, n):
    lb = 0 # lower bound
    ub = len(A) - 1 # upper bound
    pivIndx = partition(A, lb, ub) # returns pivot index
    if pivIndx == ub - n + 1: # pivIndx is the nth largest
        return A[pivIndx]
    elif pivIndx > ub - n + 1: # the nth largest is smaller than pivot
        return nthlargest(A[:pivIndx], n - (ub - pivIndx + 1))
    else: # the nth largest is greater than pivot
        return nthlargest(A[pivIndx + 1:ub + 1], n)
'''
The idea here is to find the nth largest with partition from quicksort through a loop that starts from 1 to the end of
a list. When the loop first start i = 1 = n. So it finds the 1st largest, then 2nd largest then so forth. For each time
it finds the nth largest, it will append it to a sorted list from decreasing order. One can easily reverse the list 
for increasing order. Since the running time of this increases with input size, the minimum time would be when K = 1.
'''

sortedList = []

def combineQS(sList):
    for i in range(1, len(rand1MList)):
        print(nthlargest(rand1MList, i), time.perf_counter())
        sList.append(nthlargest(rand1MList, i))
'''
Since the running time increases with input size, the fastest time would be when K = 1. So K = 6 . K - 5 = 1. K + 5 = 11
Input: None
Output: prints the running time for input size K, K - 5, K + 5
'''
def combineKrange():
    # K
    start = time.perf_counter()
    for i in range(1, 7):
        print(nthlargest(rand1MList, i))

    end = time.perf_counter()
    print("K:", end - start)

    # K - 5
    start = time.perf_counter()
    for i in range(1, 2):
        print(nthlargest(rand1MList, i))

    end = time.perf_counter()
    print("K - 5:", end - start)

    # K + 5
    start = time.perf_counter()
    for i in range(1, 12):
        print(nthlargest(rand1MList, i))

    end = time.perf_counter()
    print("K + 5:", end - start)


combineKrange()
quickNselectTimer(combineQS(sortedList))