fibo_a = 1
fibo_b = 2
list = [fibo_a, fibo_b]
suma = 0
while fibo_a + fibo_b < 4000000:
    sum = fibo_a + fibo_b
    list.append(sum)
    fibo_a = fibo_b
    fibo_b = sum

for i in list:
    if i % 2 == 0:
        suma += i

print(suma)
