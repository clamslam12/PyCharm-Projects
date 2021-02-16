import math
import numpy as np
'''
this program calculates input size n for each function and their time and writes it in an html file
'''

# time = time in microseconds
SEC = int(1e6)
MINS = int(6e7)
HR = int(3.6e9)
DAY = int(8.64e10)
MONTH = int(2.628e12)
YEAR = int(3.154e13)
CENT = int(3.154e15)
# tried to format to scientific notation but overflow occurred
def logn(t):
    return f'2^{format(t, "e")}'

lognSec = logn(SEC)
lognMin = logn(MINS)
lognHr = logn(HR)
lognDay = logn(DAY)
lognMon = logn(MONTH)
lognYr = logn(YEAR)
lognCent = logn(CENT)

print(lognSec, lognMin, lognHr, lognDay, lognMon, lognYr, lognCent)

def sqrtN(t):
    return format(t**2, "e")

sqrtSec = sqrtN(SEC)
sqrtMin = sqrtN(MINS)
sqrtHr = sqrtN(HR)
sqrtDay = (sqrtN(DAY))
sqrtMon = sqrtN(MONTH)
sqrtYr = sqrtN(YEAR)
sqrtCent = sqrtN(CENT)

def N(t):
    return format(t, "e")

Nsec = N(SEC)
Nmin = N(MINS)
Nhr = N(HR)
Nday = N(DAY)
Nmon = N(MONTH)
Nyr = N(YEAR)
Ncent = N(CENT)

# Dont know how to solve without using Lambert W function, so had to use Wolfram alpha

nlgnSec = 62746
nlgnMin = format(int(2.8e6), "e")
nlgnHr = format(int(1.3e8), "e")
nlgnDay = format(int(2.7e9), "e")
nlgnMon = format(int(7.1e10), "e")
nlgnYr = format(int(7.9e11), "e")
nlgnCent = format(int(6.8e13), "e")

def nSqr(t):
    return format(math.sqrt(t), "e")

nsqrSec = nSqr(SEC)
nsqrMin = nSqr(MINS)
nsqrHr = nSqr(HR)
nsqrDay = nSqr(DAY)
nsqrMon = nSqr(MONTH)
nsqrYr = nSqr(YEAR)
nsqrCent = nSqr(CENT)

def nCubed(t):
    return format(math.pow(t, 1/3), "e")

ncubedSec = nCubed(SEC)
ncubedMin = nCubed(MINS)
ncubedHr = nCubed(HR)
ncubedDay = nCubed(DAY)
ncubedMon = nCubed(MONTH)
ncubedYr = nCubed(YEAR)
ncubedCent = nCubed(CENT)

def twoPowN(t):
    return format(math.log(t)/math.log(2), "e")

twoPowSec = twoPowN(SEC)
twoPowMin = twoPowN(MINS)
twoPowHr = twoPowN(HR)
twoPowDay = twoPowN(DAY)
twoPowMon = twoPowN(MONTH)
twoPowYr = twoPowN(YEAR)
twoPowCent = twoPowN(CENT)

# Factorial - using wolfram alpha
nFactSec = 9
nFactMin = 11
nFactHr = 12
nFactDay = 13
nFactMon = 15
nFactYr = 16
nFactCent = 17

def writeHtml():
    with open("table1.html", mode ="w") as f:
        f.write(f'<table border="1">\n'
                f'<tr>\n'
                f'<th></th>\n'
                f'<td>1 Second</td>\n'
                f'<td>1 Minute</td>\n'
                f'<td>1 Hour</td>\n'
                f'<td>1 Day</td>\n'
                f'<td>1 Month</td>\n'
                f'<td>1 Year</td>\n'
                f'<td>1 Century</td>\n'
                f'</tr>\n'
                f'<tr>\n'
                f'<td>lg n</td>\n'
                f'<td>{lognSec}</td>\n'
                f'<td>{lognMin}</td>\n'
                f'<td>{lognHr}</td>\n'
                f'<td>{lognDay}</td>\n'
                f'<td>{lognMon}</td>\n'
                f'<td>{lognYr}</td>\n'
                f'<td>{lognCent}</td>\n'
                f'</tr>\n'
                f'<tr>\n'
                f'<td>&#8730 n</td>\n'
                f'<td>{sqrtSec}</td>\n'
                f'<td>{sqrtMin}</td>\n'
                f'<td>{sqrtHr}</td>\n'
                f'<td>{sqrtDay}</td>\n'
                f'<td>{sqrtMon}</td>\n'
                f'<td>{sqrtYr}</td>\n'
                f'<td>{sqrtCent}</td>\n'
                f'</tr>\n'
                f'<tr>\n'
                f'<td>n</td>\n'
                f'<td>{Nsec}</td>\n'
                f'<td>{Nmin}</td>\n'
                f'<td>{Nhr}</td>\n'
                f'<td>{Nday}</td>\n'
                f'<td>{Nmon}</td>\n'
                f'<td>{Nyr}</td>\n'
                f'<td>{Ncent}</td>\n'
                f'</tr>\n'
                f'<tr>\n'
                f'<td>n lg n</td>\n'
                f'<td>{nlgnSec}</td>\n'
                f'<td>{nlgnMin}</td>\n'
                f'<td>{nlgnHr}</td>\n'
                f'<td>{nlgnDay}</td>\n'
                f'<td>{nlgnMon}</td>\n'
                f'<td>{nlgnYr}</td>\n'
                f'<td>{nlgnCent}</td>\n'
                f'</tr>\n'
                f'<tr>\n'
                f'<td>n<sup>2</sup></td>\n'
                f'<td>{nsqrSec}</td>\n'
                f'<td>{nsqrMin}</td>\n'
                f'<td>{nsqrHr}</td>\n'
                f'<td>{nsqrDay}</td>\n'
                f'<td>{nsqrMon}</td>\n'
                f'<td>{nsqrYr}</td>\n'
                f'<td>{nsqrCent}</td>\n'
                f'</tr>\n'
                f'<tr>\n'
                f'<td>n<sup>3</sup></td>\n'
                f'<td>{ncubedSec}</td>\n'
                f'<td>{ncubedMin}</td>\n'
                f'<td>{ncubedHr}</td>\n'
                f'<td>{ncubedDay}</td>\n'
                f'<td>{ncubedMon}</td>\n'
                f'<td>{ncubedYr}</td>\n'
                f'<td>{ncubedCent}</td>\n'
                f'</tr>\n'
                f'<tr>\n'
                f'<td>2<sup>n</sup></td>\n'
                f'<td>{twoPowSec}</td>\n'
                f'<td>{twoPowMin}</td>\n'
                f'<td>{twoPowHr}</td>\n'
                f'<td>{twoPowDay}</td>\n'
                f'<td>{twoPowMon}</td>\n'
                f'<td>{twoPowYr}</td>\n'
                f'<td>{twoPowCent}</td>\n'
                f'</tr>\n'
                f'<tr>\n'
                f'<td>n!</td>\n'
                f'<td>{nFactSec}</td>\n'
                f'<td>{nFactMin}</td>\n'
                f'<td>{nFactHr}</td>\n'
                f'<td>{nFactDay}</td>\n'
                f'<td>{nFactMon}</td>\n'
                f'<td>{nFactYr}</td>\n'
                f'<td>{nFactCent}</td>\n'
                f'</tr>\n'
                f'</table>')


writeHtml()
