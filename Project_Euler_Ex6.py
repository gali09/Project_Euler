"""
The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is

.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

"""

from math import *
a = 0
b = 0
for i in range(1,101):
    a += i**2

for i in range(1,101):
    b += i

b = b**2
dif = b - a
print(a)
print(b)
print(dif)
