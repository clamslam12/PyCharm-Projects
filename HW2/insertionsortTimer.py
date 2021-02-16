'''
calculates time taken for insertion sort for input size n such that n = 1000 and n = 1000000
'''

import time

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

def insertionSort(arr):
    # 1 to the end of arr
    for i in range(1, len(arr)):
        val = arr[i]
        h = i
        while h > 0 and arr[h - 1] > val:
            arr[h] = arr[h-1]
            h -= 1
        arr[h] = val

def insertionsortTimer(func):
    # (could not use time.time() or time.process_time() due to having the same start and end times)
    start = time.perf_counter()
    print(f'starts at: {start}')
    func
    end = time.perf_counter()
    print(f'ends at: {end}')
    print(f'time taken: {end - start}')

rand1000List= []
rand1MList = []

rand1000List = importFile(rand1000List, "rand1000.txt")
rand1MList = importFile(rand1MList, "rand1000000.txt")

print("Insertion sort with 1000 integers")
insertionsortTimer(insertionSort(rand1000List))
print("insertion sort with 1000000 integers")
insertionsortTimer(insertionSort(rand1MList))