'''
calculates the time taken for merge sort of input size n such that n = 1000 and n = 1000000
'''
import time
def mergeSort(nlist):

    if len(nlist)>1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k]=lefthalf[i]
                i=i+1
            else:
                nlist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            nlist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            nlist[k]=righthalf[j]
            j=j+1
            k=k+1


rand1000List = []  # list to hold numbers
def mergesortTimer(func):
    # (could not use time.time() or time.process_time() due to having the same start and end times)
    start = time.perf_counter()
    print(f'starts at: {start}')
    func
    end = time.perf_counter()
    print(f'ends at: {end}')
    print(f'time taken: {end - start}')

rand1000List= []
rand1MList = []
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

rand1000List = importFile(rand1000List, "rand1000.txt")
rand1MList = importFile(rand1MList, "rand1000000.txt")

print("merge sort with 1000 integers")
mergesortTimer(mergeSort(rand1000List))
print("merge sort with 1000000 integers")
mergesortTimer(mergeSort(rand1MList))




