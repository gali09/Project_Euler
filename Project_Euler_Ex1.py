n = 0
suma_3 = 0
suma_5 = 0

for i in range(1000):
    if i % 3 == 0:
        suma_3 += i
    elif i % 5 == 0:
        suma_5 += i
sum = suma_3 + suma_5
print(sum)