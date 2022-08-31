"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
n = 600851475143
prime = []
i = 1
while i <= n:
    if n % i == 0 and i not in prime:
        prime.append(i)
        n = n / i
        print(n)
        i += 1
    else:
        i += 1

print('NUMEROS PRIMOS:')
print(prime)

"""
from numbertools import is_prime

n = 600851475143
for i in range(3, n // 2 + 1, 2):
    if n % i == 0 and is_prime(n // i):
        print(n // i)
        break
"""