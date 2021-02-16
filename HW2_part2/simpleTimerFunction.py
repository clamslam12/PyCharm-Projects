import timeit

def timeEfficiency(func):
    start = timeit.default_timer()
    print(f'starts at: {start}')
    sumOf = func
    end = timeit.default_timer()
    print(f'ends at: {end}')
    print(f'sum is {sumOf}')
    print("time taken to execute the function: %.7f" % float(end - start))


def sumUp(n):
    s = 0
    for x in range(0, n + 1):
        s += x
    return s

num = int(input("enter your num for 0..."))
timeEfficiency(sumUp(num))