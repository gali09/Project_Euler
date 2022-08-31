"""

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""

from sympy import isprime

# prime = [isprime(a) for a in range(99)]
# print(prime)
prime = []
condicion = False

for i in range(9999999):
    if isprime(i):
        prime.append(i)
        if len(prime) > 10000:
            break
print(prime)
print(len(prime))
print(prime[10000])

