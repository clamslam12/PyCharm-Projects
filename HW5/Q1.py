import time

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
    # converts to str for every element in list
    for i, val in enumerate(randL):
        j = str(val)
        randL[i] = j
    return randL


# A Naive recursive Python implementation of LCS problem
'''
This function finds the length of the LCS of two strings by naive recursive implementation
Input: two strings and their lengths
Output: returns the length of the LCS of the two input strings
'''
def lcs(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m - 1] == Y[n - 1]:
        return 1 + lcs(X, Y, m - 1, n - 1)
    else:
        return max(lcs(X, Y, m, n - 1), lcs(X, Y, m - 1, n))


# Dynamic Programming implementation of LCS problem
'''
This function finds the length of the LCS of two strings based on dynamic programming technique
Input: two strings
Output: returns the length of the LCS of the two input strings
'''
def DPlcs(X, Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)

    # declaring the array for storing the dp values
    L = [[None] * (n + 1) for i in range(m + 1)]

    """Following steps build L[m+1][n+1] in bottom up fashion 
    Note: L[i][j] contains length of LCS of X[0..i-1] 
    and Y[0..j-1]"""
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

                # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]


# end of function lcs

compStr = "0123456789"
randL = []
rand1M = importFile(randL,"rand1000000.txt")
# dynamic programming LCS test
'''
This function applies the DP LCS function to all integer strings in a list and compares each integer string with
compStr = "0123456789"
Input: a list of 1 million integer strings and the comparison string  "0123456789"
Output: returns the length of the LCS for each integer string in the list with the comparison string "0123456789"
'''
def dpTest(l,cStr):
    for i in l:
        DPlcs(i,cStr)
'''
This function applies the naive LCS function to all integer strings in a list and compares each integer string with
compStr = "0123456789"
Input: a list of 1 million integer strings and the comparison string  "0123456789"
Output: returns the length of the LCS for each integer string in the list with the comparison string "0123456789"
'''
def naiveRecursiveTest(l, cStr):
    for i in l:
        lcs(i,cStr, len(i), len(cStr))

'''
This function calculates the time efficiency(runtime) of DP LCS and naive recursive LCS
Input: a list of 1 million integer strings and the comparison string  "0123456789"
Output: prints the start time, end time, and time taken for DP LCS and naive recursive LCS
'''
def timeEff(l, cStr):
    print("Testing dynamic programming LCS")
    start = time.perf_counter()
    print("starts at:", start)
    dpTest(l,cStr)
    end = time.perf_counter()
    print("ends at:", end)
    print("time taken:", end - start)
    # testing naive recursive LCS
    print("Testing naive recursive LCS")
    start = time.perf_counter()
    print("starts at:", start)
    naiveRecursiveTest(l, cStr)
    end = time.perf_counter()
    print("ends at:", end)
    print("time taken:", end - start)

timeEff(rand1M, compStr)
#Results:
# Testing dynamic programming LCS
# starts at: 0.6233879
# ends at: 34.1140615
# time taken: 33.4906736
# Testing naive recursive LCS
# starts at: 34.114102
# ends at: 1444.9658196
# time taken 1410.8517176