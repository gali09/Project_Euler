"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""

n = 999

result = []
for i in range(1,n):
    for j in range(1,n):
        num = i*j
        palin = [int(a) for a in str(num)] #rellenar lista con los digitos de num

        if len(str(num)) == 1:
            if palin[0] == palin[-1]:
                print(f"{num} = {i} x {j}")
                result.append(num)
        elif len(str(num)) == 2:
            if polin[0] == polin[-1] and polin[1] == polin[-2]:
                print(f"{num} = {i} x {j}")
                result.append(num)
        else:
            if polin[0] == polin[-1] and polin[1] == polin[-2] and polin[2] == polin[-3]:
                print(f"{num} = {i} x {j}")
                result.append(num)

print(max(result)) #buscar el valor maximo
"""
% isPalindromeNumber: returns true if the given number are a palindrome 
%                     otherwise false.
% assumes: the given number is positive
function ans = isPalindromeNumber(number)
  % precondition
  assert(number >= 0,'number must be positive')
  ans = false;
  strNumber = num2str(number); % num2str convierte un numero en string, es de la liberria math
  if (strNumber == flip(strNumber)) % flip traspone la posición de una lista, es de la libreria numpy
    ans = true;
  endif
endfunction
"""