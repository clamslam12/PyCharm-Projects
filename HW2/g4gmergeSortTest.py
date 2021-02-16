randlist1000 = []
randlist1M = []

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


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = []
    R = []

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L.append(arr[l + i])

    for j in range(0, n2):
        R.append(arr[m + 1 + j])

        # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


# l is for left index and r is right index of the
# sub-array of arr to be sorted

def mergeSort(arr, l, r):
    if l < r:
        # Same as (l+r)/2, but avoids overflow for
        # large l and h
        m = (l + r) // 2

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


randlist1000 = importFile(randlist1000, "rand1000.txt")
randlist1M = importFile(randlist1M, "rand1000000.txt")

mergeSort(randlist1000, 0, len(randlist1000) - 1)
for num in randlist1000:
    print(num)