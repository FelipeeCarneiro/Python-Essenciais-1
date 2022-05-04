def is_year_leap(year):
  if year % 4 == 0 :#1³ etapa
    if(year%100==0):#2
      if(year%400==0):return True#3 #4
      else:return False#4
    else:return True#4
  else:return False #5 - 365 dias não é bissexto
'''Como determinar se um ano é bissexto
1-Se o ano for uniformemente divisível por 4, vá para a etapa 2. Caso contrário, vá para a etapa 5.
2-Se o ano for uniformemente divisível por 100, vá para a etapa 3. Caso contrário, vá para a etapa 4.
3-Se o ano for uniformemente divisível por 400, vá para a etapa 4. Caso contrário, vá para a etapa 5.
4-O ano é bissexto (tem 366 dias).
5-O ano não é um ano bissexto (tem 365 dias).'''

def void():
 y = int(input ('Entre com o ano escolhido '))
 print(y,'É um ano bissexto?',is_year_leap(y))

def tests():
  test_data = [1900,2000,2016,1987]
  test_res = [False,True,True,False]
  for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,'-> ',end='')
    result = is_year_leap(yr)
    if (result == test_res[i]) :
      print('Ok')
    else:
      print('Falhou')

tests()
void()