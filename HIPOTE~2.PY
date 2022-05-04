# O “triângulo de ângulo retângulo” novamente
# Aqui está o nosso programa “triângulo de ângulo retângulo” novamente:

leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is " + str((leg_a**2 + leg_b**2) ** .5))

'''Modificámo-lo um pouco para lhe mostrar como a função str() funciona.
Graças a isso, podemos passar todo o resultado para a função print() 
como uma string, esquecendo as vírgulas.'''