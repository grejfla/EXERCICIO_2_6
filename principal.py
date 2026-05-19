import math
a = int(input("digite o valor de 'a': "))
b = int(input("digite o valor de 'b': "))
c = int(input("digite o valor de 'c': "))
delta = b ** 2 - 4 * a * c
print ("Delta é igual a: ", delta)
x1 = (- b + (math.sqrt(delta))) / 2 * a
x2 = (- b - (math.sqrt(delta))) / 2 * a
print ("x1 é igual a:  ", x1)
print ("x2 é igual a:  ", x2)
