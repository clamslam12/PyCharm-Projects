from operator import add
from plotly import graph_objects as go
from plotly import offline
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

def process(a, b):
    return a[0] if a[0] > b[0] else b[0], a[1] + b[1]

# A Naive recursive Python implementation of LCS problem
# X/Y are strings and m = len(X) and n = len(Y)
def lcs(X, Y, m, n):
    if m == 0 or n == 0:
        return 0, 1
    elif X[m - 1] == Y[n - 1]:
        result = lcs(X, Y, m - 1, n - 1)
        return tuple(map(add, result, (1, 1))) if (result[1] <= 6000 and result[1]>0) else tuple(0,0)
    else:
        resultA = lcs(X, Y, m, n - 1)
        if(resultA[1] > 6000 or resultA[1]==0):
            return(0,0)
        resultB = lcs(X, Y, m-1, n)
        if(resultB[1] > 6000 or resultB[1]==0 or resultA[1]+resultB[1]>6000):
            return(0,0)
        return tuple(map(add, process(resultA, resultB), (0, 1)))

def hash_func(str):
    return abs(hash(str))

class hash_table:
    def __init__(self, size):
        self.table = [0] * size
        self.size = size
        self.collisions = [0] * size

    def insert(self, hash_value, value):
        index = hash_value % self.size
        if self.table[index] != 0:
            self.collisions[index] += 1
        else:
            self.table[index] = value

def do_analysis():
    compStr = "0123456789"
    random_list = []
    random_list = importFile(random_list,"rand1000000.txt")
    table = hash_table(10000)
    for num in random_list:
        key = lcs(num,compStr,len(num),10)
        if(key[1]==0):
            table.insert(hash_func(num), num)
        else:
            table.insert(key[1],num)
    
    offline.plot([go.Scatter(y=table.collisions)])

do_analysis()