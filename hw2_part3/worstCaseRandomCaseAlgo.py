import random
from random import choice

#exclude100 = [0,1,2,3,4,5,6,7,8]
#compGuess100 = random.choice([i for i in range(0,10) if i not in exclude100])
#print(compGuess100)

def dWorstCase():

    highestGInTry = 0
    numTries = 0
    totalG = 0
    correctTries = 0  # correct guess for all 3 numbers
    lowestTries = 0
    for x in range(1, 10001):
        numTries += 1
        # generate 3 random numbers
        rand1 = random.randint(0, 9)
        rand2 = random.randint(0, 9)
        rand3 = random.randint(0, 9)
        # store in a tuple
        randT = (rand1, rand2, rand3)

        # guess the 3 numbers
        # For this try
        numGuess = 0
        # list of tuples that contains numbers that are already guessed
        exclude = []
        while numGuess <= 1000:  # max guess
            # computer guess
            compG1 = random.randint(0, 9)
            compG2 = random.randint(0, 9)
            compG3 = random.randint(0, 9)
            compT = (compG1, compG2, compG3)
            if compT == randT and compT not in exclude:  # correct guess
                totalG += 1  # increment total number of guess for all tries
                correctTries += 1  # increment number of correct tries
                lowestTries += 1
                numGuess += 1
                #highestGInTry = numGuess
                break
            elif compT != randT and compT not in exclude:  # wrong guess
                totalG += 1  # increment total number of guess for all tries
                numGuess += 1  # increment number of guess for a try
                exclude.append(compT)
            else:
                continue
        if numGuess >= highestGInTry:
            highestGInTry = numGuess
        if numGuess >= highestGInTry and numGuess == 1001:
            highestGInTry = numGuess - 1
        if correctTries >= 1:
            lowestTries = 1
        else:
            lowestTries = 0

    print("Deterministic worst case algorithm\n")
    print("Number of tries:", numTries)
    print("Highest number of guess in a try:", highestGInTry)
    print("Lowest Tries:", lowestTries)
    print("Number of Correct Tries:", correctTries)
    print("Average number of Tries:", totalG, "/", numTries, ": ",totalG/numTries )

def cRandAlgo():

    highestGInTry = 0
    numTries = 0
    totalG = 0
    correctTries = 0  # correct guess for all 3 numbers
    lowestTries = 0
    for x in range(1, 10001):
        numTries += 1
        # generate 3 random numbers
        rand1 = random.randint(0, 9)
        rand2 = random.randint(0, 9)
        rand3 = random.randint(0, 9)
        # store in a tuple
        randT = (rand1, rand2, rand3)

        # guess the 3 numbers
        # For this try
        numGuess = 0

        while numGuess <= 10000:  # max guess
            # computer guess
            compG1 = random.randint(0, 9)
            compG2 = random.randint(0, 9)
            compG3 = random.randint(0, 9)
            compT = (compG1, compG2, compG3)
            if compT == randT:  # correct guess
                totalG += 1  # increment total number of guess for all tries
                correctTries += 1  # increment number of correct tries
                lowestTries += 1
                numGuess += 1
                break
            else:  # wrong guess
                totalG += 1  # increment total number of guess for all tries
                numGuess += 1  # increment number of guess for a try

        if numGuess >= highestGInTry:
            highestGInTry = numGuess
        if numGuess >= highestGInTry and numGuess == 10001:
            highestGInTry = numGuess - 1
        if correctTries >= 1:
            lowestTries = 1
        else:
            lowestTries = 0

    print("Complete random algorithm\n")
    print("Number of tries:", numTries)
    print("Highest number of guess in a try:", highestGInTry)
    print("Lowest Tries:", lowestTries)
    print("Number of Correct Tries:", correctTries)
    print("Average number of Tries:", totalG, "/", numTries, ": ", totalG / numTries)

dWorstCase()
print()
cRandAlgo()











