def is_year_leap(year):
    if (year %4 ==0) :          #
        if (year %100 ==0) :    # Your code from LAB 4.3.1.6.
            if (year %400 ==0) :#
                return True
        else:
            return True
    else:
        return False

def days_in_month(year, month):
	lst_month_31 = [1,3,5,7,8,10,12]
	lst_month_30 = [4,6,9,11]
	if month == 2: #sensível ao mes de fevereiro -- único que muda em ano bissexto
		if is_year_leap(year):
			days = 29
		else:
			days = 28
	#demais dias do ano
	else:
		if month in lst_month_31:
			days = 31
		elif month in lst_month_30:
			days = 30
		else:
			days = None
	return days

def tests():
	test_years = [1900, 2000, 2016, 1987]
	test_months = [2, 2, 1, 11]
	test_results = [28, 29, 31, 30]
	for i in range(len(test_years)):
		yr = test_years[i]
		mo = test_months[i]
		print(yr, mo, "->", end="")
		result = days_in_month(yr, mo)
		if result == test_results[i]:
			print("OK")
		else:
			print("Failed")

def void():
	rodar_test = input("Digite 'sim' e tecle enter para fazer os testes ou apenas tecle enter para continuar:")
	if rodar_test == "sim":
		tests()
		void()
	else:
		ano = int(input("Informe um ano:"))
		mes = int(input("Agora informe o mês:"))
		print('{}/{} tem {} dias.'.format(mes , ano, days_in_month(ano,mes)) )

void()
''' 4.3.1.7 LAB: Quantos dias: escrever e usar as suas próprias funções
LAB

Tempo estimado

15-20 minutos
Nível de dificuldade

Médio
Pré-requisitos

LAB 4.3.1.6
Objetivos

Familiarizar o aluno a:

    projetar e escrever funções parametrizadas;
    utilizar a return declaração;
    utilizar as próprias funções do aluno.

	Cenário

A sua tarefa é escrever e testar uma função que
toma dois argumentos (um ano e um mês) e devolve
o número de dias para o par mês/ano dado (enquanto
apenas fevereiro é sensível ao valor year , a sua
função deve ser universal).

A parte inicial da função está pronta.
Agora, convença a função a devolver None
se os seus argumentos não fizerem sentido.

É claro que pode (e deve) usar a função
previamente escrita e testada (LAB 4.3.1.6).
Pode ser muito útil. Encorajamo-lo a utilizar
uma lista preenchida com a duração dos meses.
Pode criá-la dentro da função - este truque
irá encurtar significativamente o código.

Preparámos um código de teste.
Expanda-o para incluir mais casos de teste.
-------------------------------------------
editor console:
def is_year_leap(year):
#
# Your code from LAB 4.3.1.6.
#

def days_in_month(year, month):
#
# Write your new code here.
#

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")

'''