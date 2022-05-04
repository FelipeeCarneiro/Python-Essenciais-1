'''
2.6.1.5 Como falar com um computador
O programa pede duas vezes ao utilizador o comprimento de ambas 
as pernas, avalia a hipotenusa e imprime o resultado.
Execute-o e tente introduzir alguns valores negativos.

O programa - infelizmente - não reage a este erro óbvio.

Vamos ignorar esta fraqueza por agora. Voltaremos a este assunto em breve.
'''

# leg_a = float(input("Input first leg length: "))
# leg_b = float(input("Input second leg length: "))
# hypo = (leg_a**2 + leg_b**2) ** .5
# print("Hypotenuse length is", hypo)

'''
# Note que no programa que pode ver no editor, a variável hypo é utilizada apenas para uma única finalidade - para guardar o valor calculado entre a execução da linha de código adjacente.

# Como a função print() aceita uma expressão como seu argumento, pode remover a variável do código.
# Tal como isto:
'''

leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is", (leg_a**2 + leg_b**2) ** .5)
