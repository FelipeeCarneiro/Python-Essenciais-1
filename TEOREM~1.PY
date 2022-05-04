'''
O teorema de Pitágoras:

O quadrado da hipotenusa é igual à soma dos 
quadrados dos catetos.

O código seguinte avalia o comprimento da 
hipotenusa (ou seja, o lado mais longo de um 
triângulo retângulo, o oposto ao ângulo reto) 
usando o teorema de Pitágoras:
'''
cateto_a = 3.0
cateto_b = 4.0
hipotenusa  = (cateto_a ** 2 + cateto_b ** 2) ** 0.5 # Usamos ** no lugar da raiz quadrada
print("Hipotenusa =", hipotenusa)


#Nota: precisamos de fazer uso do operador ** para avaliar a raiz quadrada como:
# √(x) = x(½)
# e
# c = √a2 + b2
