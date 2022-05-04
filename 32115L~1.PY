def checar_numero_real() :
    num_natural = 1
    while num_natural < 2 :
        num_natural = int(input("Insira um número natural:") )
    return num_natural
    
def se_for_par(num) :
    if (num % 2) == 0 :
        return True
    else:
        return False

def par_calculo(num_par) : 
    new_par = num_par // 2
    return new_par

def impar_calculo(num_impar) :
    new_impar = 3 * num_impar + 1
    return new_impar

def calculo_hipotese_intrigante(num_c0) :
    index = 0
    while num_c0 != 1 :
        if se_for_par(num_c0): 
            num_c0 = par_calculo(num_c0)
            print(num_c0)
            index += 1          #se for par, avalie um novo c0 como c0 ÷ 2;
        else:            
            num_c0 = impar_calculo(num_c0)
            pr:int(num_c0)
            index += 1
    return [index, num_c0]
#             [0]      [1]

def collatz():
    c0 = checar_numero_real()          #tomar qualquer número inteiro não-negativo e não-nulo e nomeá-lo c0
    steps = calculo_hipotese_intrigante(c0)[0]
    print("steps =",steps)
    # num_final = hipotese_intrigante[1]    
    # return [num_final, steps]
    #              [0]               [1]
'''-----------------+
|quero fazer testes |
| infinitos mas não |
|    tive tempo     |
+-----------------''' 
def test_collatz():    
    num_natural = 3**68 #tomar qualquer número inteiro não-negativo e não-nulo e nomeá-lo c0
    c0_test = 1
    while c0_test == 1:
        if c0_test == 1:        
            c0_test = calculo_hipotese_intrigante(num_natural)[1]
            steps_test = calculo_hipotese_intrigante(num_natural)[0]
            print(num_natural)
            num_natural += 1
        if c0_test != 1:
            break
        
    print("c0 diferente de 1!")
    print("steps test =",steps_test,"c0 test =", c0_test)

# collatz() #funciona
test_collatz()

''' 3.2.1.15 LAB: A hipótese de Collatz
LAB

Tempo estimado
20 minutos

Nível de dificuldade
Médio

Objetivos
Familiarizar o aluno a:

a utilização do loop while ;
a conversão de loops definidos verbalmente em código Python real.
Cenário
Em 1937, um matemático alemão chamado Lothar Collatz formulou uma hipótese intrigante (ainda não provada) que pode ser descrita da seguinte forma:

tomar qualquer número inteiro não-negativo e não-nulo e nomeá-lo c0;
se for par, avalie um novo c0 como c0 ÷ 2;
caso contrário, se for ímpar, avalie um novo c0 como 3 × c0 + 1;
Se c0 ≠ 1, saltar para o ponto 2.
A hipótese diz que, independentemente do valor inicial de c0, irá sempre para 1.

É claro que é uma tarefa extremamente complexa utilizar um computador para provar a hipótese de qualquer número natural (pode até requerer inteligência artificial), mas pode usar o Python para verificar alguns números individuais. Talvez até encontre o que possa refutar a hipótese.


Escreva um programa que leia um número natural e execute os passos acima indicados, desde que c0 permaneça diferente de 1. Também queremos que conte os passos necessários para alcançar o objetivo. O seu código deve fazer output de todos os valores intermédios de c0, também.

Dica: a parte mais importante do problema é como transformar a ideia de Collatz num loop while - esta é a chave para o sucesso.

Teste o seu código utilizando os dados por nós fornecidos.

Dados de teste

Input de amostra: 15

Output esperado:

46
23
70
35
106
53
160
80
40
20
10
5
16
8
4
2
1
steps = 17
Input de amostra: 16

Output esperado:

8
4
2
1
steps = 4
Input de amostra: 1023

Output esperado:

3070
1535
4606
2303
6910
3455
10366
5183
15550
7775
23326
11663
34990
17495
52486
26243
78730
39365
118096
59048
29524
14762
7381
22144
11072
5536
2768
1384
692
346
173
520
260
130
65
196
98
49
148
74
37
112
56
28
14
7
22
11
34
17
52
26
13
40
20
10
5
16
8
4
2
1
steps = 62

'''