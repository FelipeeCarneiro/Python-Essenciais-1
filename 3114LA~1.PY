'''
3.1.1.4 LAB: Perguntas e respostas
LAB

Tempo estimado
5-10 minutos

Nível de dificuldade
Muito fácil

Objetivos
familiarizar-se com a função input() ;
familiarizar-se com os operadores de comparação em Python.
Cenário
Usando um dos operadores de comparação em Python, escreva um programa simples de duas linhas que toma o parâmetro n como input, que é um inteiro, e imprime False Se n for menor que 100, e True Se n for maior ou igual que 100.

Não crie blocos if nenhuns (vamos falar deles muito em breve). Teste o seu código utilizando os dados que lhe fornecemos.

Dados de teste

Input de amostra: 55

Output esperado: False

Input de amostra: 99

Output esperado: False

Input de amostra: 100

Output esperado: True

Input de amostra: 101

Output esperado: True

Input de amostra: -5

Output esperado: False

Input de amostra: +123

Output esperado: True
'''
#-------------------------------outra solução-------------------------------

# def programa(n):
#     i = 0
#     while i < len(n):
#         print(n[i] >= 100)
#         i += 1
# l = [55,99,100,101,-5,+123] #dados de teste

# programa(l)

#-------------------------------outra solução-------------------------------
# x = 0
# while x != None:
#     x = int(input("Informe um número ou Enter para sair: "))
#     print(x >= 100)

#-------------------------------outra solução-------------------------------
#solução pedida no exercício
x = int(input(""))
print(x >= 100)