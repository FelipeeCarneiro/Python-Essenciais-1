'''Cenário
A sua tarefa é completar o código a fim de avaliar os resultados de quatro operações aritméticas básicas.

Os resultados têm de ser impressos para a consola.

Poderá não conseguir proteger o código de um utilizador que queira dividir por zero. Tudo bem, não se preocupe com isso por agora.

Teste o seu código - produz os resultados que espera?

Não lhe mostraremos quaisquer dados de teste - isso seria demasiado simples.
# input a float value for variable a here
# input a float value for variable b here

# output the result of addition here
# output the result of subtraction here
# output the result of multiplication here
# output the result of division here

print("\nThat's all, folks!")'''
# input a float value for variable a here
# input a float value for variable b here

# output the result of addition here
# output the result of subtraction here
# output the result of multiplication here
# output the result of division here

# print("\nThat's all, folks!")
#===================================================================================
#começo da minha resolução do exercício


pvalor = float(input("\n\nfirst value here: "))# input a float value for variable a here

svalor = float(input("second value here: "))# input a float value for variable b here
print(
    "\n\nThe results of:\n","Addition",float(pvalor + svalor),  # output the result of addition here
    "subtraction",float(pvalor-svalor),     # output the result of subtraction here
    "multiplication",float(pvalor*svalor),  # output the result of multiplication here
    "division",float(pvalor/svalor)         # output the result of division here
    ,sep="\n"
    )
print("\nThat's all, folks!")
