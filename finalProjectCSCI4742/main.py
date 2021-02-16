# stores permutations of user input string
results = []
# function takes a string, start index, and ending index
def bruteForce(iarray, start, end):
    #if left and right index are the same; only 1 letter
    if start == end:
        # eliminate duplicate results given duplicate inputs
        if ''.join(iarray) not in results:
            results.append(''.join(iarray))

    else:
        for i in range(start, end + 1):
            iarray[start], iarray[i] = iarray[i], iarray[start]
            bruteForce(iarray, start + 1, end)
            #backtrack
            iarray[start], iarray[i] = iarray[i], iarray[start]

# function takes a string, custom string , start index, and ending index; concatenate custom string to the front of each permutation
def bruteForce2(iarray, start, end, customString):
    # if left and right index are the same; only 1 letter
    if start == end:
        # eliminate duplicate results given duplicate inputs
        if customString+''.join(iarray) not in results:
            results.append(customString+''.join(iarray))

    else:
        for i in range(start, end + 1):
            iarray[start], iarray[i] = iarray[i], iarray[start]
            bruteForce2(iarray, start + 1, end, customString)
            # backtrack
            iarray[start], iarray[i] = iarray[i], iarray[start]

# function takes a string, custom string , start index, and ending index; concatenate custom string to the end of each permutation
def bruteForce3(iarray, start, end, customString):
    # if left and right index are the same; only 1 letter
    if start == end:
        # eliminate duplicate results given duplicate inputs
        if ''.join(iarray)+customString not in results:
            results.append(''.join(iarray)+customString)

    else:
        for i in range(start, end + 1):
            iarray[start], iarray[i] = iarray[i], iarray[start]
            bruteForce3(iarray, start + 1, end, customString)
            # backtrack
            iarray[start], iarray[i] = iarray[i], iarray[start]



def help():
    print('Normal Brute Force- user will enter a string and the program will find all possible permutations of it. If string inputs contain'
          ' duplicate characters, the program will dynamically delete any duplicate results ')
    print('Custom Brute Force- user will enter a string, a custom string, and placement of custom string and the program will find all possible permutations of it.\n A custom string can be placed in front or back of a permutation string. If string inputs contain '
          'duplicate characters, the program will dynamically delete any duplicate results.')


while(True):

    print('********* Brute Force for Wordlists/Passwords **********')
    print('1. Help')
    print('2. Normal Brute Force w/ output to file')
    print('3. Custom Brute Force w/ output to file')
    print('4. Exit')
    option = int(input('Enter an option: '))
    fileOut = open('outFile.txt', 'w+')
    if option == 1:
        help()
        its = 'string'
        me = 'hello'

    elif option == 2:
        inputString = input('Enter your string: ')
        lengthInputString = len(inputString)
        # take each character from input and store in an array
        inputArray = list(inputString)
        #apply brute force
        bruteForce(inputArray, 0, lengthInputString - 1)
        #print all permutations
        for i in results:
            print(i)
            fileOut.write(i+'\n')
        #clear the array for other user inputs
        results.clear()
        fileOut.close()
    elif option == 3:
        inputString2 = input('Enter your string: ')
        customString2 = input('Enter your custom string: ')
        placement = input('Enter your custom string placement (f for front, b for back): ')
        lengthInputString2 = len(inputString2)
        # take each character from input and store in an array
        inputArray2 = list(inputString2)
        # apply brute force front
        if placement == 'f':
            bruteForce2(inputArray2, 0, lengthInputString2 - 1, customString2)
            for i in results:
                print(i)
                fileOut.write(i+'\n')
            # clear array for other inputs
            results.clear()
            fileOut.close()
        # apply brute force back
        else:
            bruteForce3(inputArray2, 0, lengthInputString2 - 1, customString2)
            for i in results:
                print(i)
                fileOut.write(i+'\n')
            # clear array for other inputs
            results.clear()
            fileOut.close()
    else:
        break
