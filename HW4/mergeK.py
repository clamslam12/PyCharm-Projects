import math
import heapq
from collections import deque

'''
This function use min heap to sort merge all elements from the sorted sublists to a single sorted list. For each element
in each sublist, it will add to heap and then heapify to find the smallest. Then it will remove the smallest and add to 
result[]. Then it will add the next element in the array in which the smallest resides. It will continue adding and removing
from heap until all elements from each sublists are added.
Input: a list with k sorted sublists of length n = 10000
Output: a list with k*n elements in sorted order
'''
def k_merge(lists):
    queues = [queue for queue in map(deque, lists)]

    heap = []
    for i, lst in enumerate(queues):
        heap.append((lst.popleft(), i))

    heapq.heapify(heap)

    result = []
    while heap:
        value, index = heapq.heappop(heap)
        result.append(value)

        if queues[index]:
            heapq.heappush(heap, (queues[index].popleft(), index))

    return result



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

'''
This function splits a list into k sublists with n elements each
Input: a list and n = # elements in each sublist
Output: a list containing k sublists with n elements in each
'''

def chunks(l, n):
    # For item i in a range that is a length of l,
    for i in range(0, len(l), n):
        # Create an index range for l of n items:
        yield l[i:i+n]


'''
This function applies counting sort to sort a list
Input: a list and exponent to find correct place of digit
Output: nothing but original list will be sorted
'''
def countingSort(arr, exp1):
    n = len(arr)

    # The output array elements that will have sorted arr
    output = [0] * (n)

    # initialize count array as 0
    count = [0] * (10)

    # Store count of occurrences in count[]
    for i in range(0, n):
        index = int((arr[i] / exp1))
        count[(index) % 10] += 1

    # Change count[i] so that count[i] now contains actual
    #  position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]

        # Build the output array
    i = n - 1
    while i >= 0:
        index = int((arr[i] / exp1))
        output[count[(index) % 10] - 1] = arr[i]
        count[(index) % 10] -= 1 # decrement the element in count for next iteration of same index
        i -= 1

    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]


'''
This function applies radix sort to sort a list with counting sort as the underlying sorting algorithm
Input: a list
Output: nothing but original list is sorted
'''
def radixSort(arr):
    # Find the maximum number to know number of digits
    max1 = max(arr)

    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 / exp > 0:
        countingSort(arr, exp)
        exp *= 10


DEFAULT_BUCKET_SIZE = 5
'''
This function applies bucket sort to sort a list
Input: a list and default bucket size
Output: a list that is sorted
'''
def bucketSort(array, bucketSize=DEFAULT_BUCKET_SIZE):
  if len(array) == 0:
    return array

  # Determine minimum and maximum values
  minValue = array[0]
  maxValue = array[0]
  for i in range(1, len(array)):
    if array[i] < minValue:
      minValue = array[i]
    elif array[i] > maxValue:
      maxValue = array[i]

  # Initialize buckets
  bucketCount = math.floor((maxValue - minValue) / bucketSize) + 1
  buckets = []
  for i in range(0, bucketCount):
    buckets.append([])

  # Distribute input array values into buckets
  for i in range(0, len(array)):
    buckets[math.floor((array[i] - minValue) / bucketSize)].append(array[i])

  # Sort buckets and place back into input array
  array = []
  for i in range(0, len(buckets)):
    buckets[i] = sorted(buckets[i])
    for j in range(0, len(buckets[i])):
      array.append(buckets[i][j])

  return array


rand1MList = [] # initialize a list to store 1000000 elements
rand1MList = importFile(rand1MList, "rand1000000.txt") # store the 1000000 elements
rand10000 = [] # initialize a list to store 100 sublists with 10000 in each
rand10000 = list(chunks(rand1MList,10000)) # store 100 sublists with 10000 in each
fHalf = rand10000[0:50] # split the first half sublists (50 sublists)
sHalf = rand10000[50:] # split the second half sublists (50 sublists)
print("this may take some time...")
# bucketsort the second half and append to list
newBsRs = [] # list to store all the sorted sublist from radix sort and bucket sort
for i in range(0,50):
    newL = bucketSort(sHalf[i])
    newBsRs.append(newL)

#radix sort for first half
for i in range(0,50):
    radixSort(fHalf[i])
# append the sorted sublist to new list
for i in range(0,50):
    newBsRs.append(fHalf[i])

# apply merge to 100 sorted sublists
print("Merging all sorted sublists into a single list and print...")
mL = k_merge(newBsRs) # mL stores all sorted elements from both sublist
for x in mL:
    print(x)
print("length of list:", len(mL)) # equals to 1,000,000 , so all alements are sorted