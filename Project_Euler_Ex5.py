"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""

# list=[2,3,5,7,11,13,17,19]
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print(list)
number = 0
cont = 0
for i in range(196197952, 1000000000,19):
    for a in list:
        if i % a == 0:
            cont += 1
        else:
            cont = 0

    print(i)
    if cont == 20:
        print(f'ESTE ES EL NUMERO {i}')
        break


"""
check_list = [11, 13, 14, 16, 17, 18, 19, 20]

def find_solution(step):
    for num in range(step, 999999999, step):
        if all(num % n == 0 for n in check_list):
            return num
    return None

solution = find_solution(20)
if solution is None:
    print("No answer found")
else:
    print("found an answer:", solution)

"""