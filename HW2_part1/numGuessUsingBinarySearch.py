# declare and initialize array 1-1000
nArr = [i for i in range(1, 1001)]


def binarySearchCustom(arr, l, r, x):

    counter = 0
    while l <= r:

        mid = int(l + (r - l) / 2)
        print("computer says: ", nArr[mid])
        result = input("Type 'l' if larger, 's' if smaller, 'c' if correct: ")

        # if x is at mid
        if result == 'c':
            counter += 1
            print("Done, Your number is {}. Guessed in {} times".format(arr[mid], counter))
            return 1

        # if x is greater, ignore left half of array
        elif result == 'l':
            counter += 1
            l = mid + 1

        # If x is smaller, ignore right half of array
        else:
            counter += 1
            r = mid - 1

        # If we reach here, then the element
        # was not present
    return -1


x = int(input("Enter a number between 1 and 1000? "))
binarySearchCustom(nArr, 0, len(nArr)-1, x)



