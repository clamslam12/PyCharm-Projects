fName = input("Enter file: ")
wordsD = {"the": 0, "of": 0, "to": 0, "we": 0, "and": 0,
         "a": 0, "our": 0, "that": 0, "not": 0, "in": 0}

with open(fName, mode='r') as f:
    for line in f:
        words = line.split()
        for i in words:
            if i == "the":
                wordsD["the"] += 1
            elif i == "of":
                wordsD["of"] += 1
            elif i == "to":
                wordsD["to"] += 1
            elif i == "we":
                wordsD["we"] += 1
            elif i == "and":
                wordsD["and"] += 1
            elif i == "a":
                wordsD["a"] += 1
            elif i == "our":
                wordsD["our"] += 1
            elif i == "that":
                wordsD["that"] += 1
            elif i == "not":
                wordsD["not"] += 1
            elif i == "in":
                wordsD["in"] += 1
# sorted returns a list of tuples sorted by value
sorted_d = sorted((value, key) for (key,value) in wordsD.items()) # low to high
for items in sorted_d[::-1]: # reverse order(high to low)
    print(items[1], ":", items[0])


