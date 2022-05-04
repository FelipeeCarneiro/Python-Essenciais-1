'''
Depois de concluir o lab, 
abra a Sandbox e experimente mais. 
Tente escrever conversores diferentes, 

por exemplo, um conversor de USD para EUR, 
um conversor de temperatura, etc.

- deixe que a sua imaginação voe! 
Tente fazer output dos resultados combinando 
strings e variáveis. Tente usar e experimentar 
com a round() função para arredondar os seus 
resultados a uma, duas ou três casas decimais. 
Verifique o que acontece se não fornecer qualquer 
número de dígitos. Lembre-se de testar os seus programas.

Experimente, tire conclusões, e aprenda. Seja curioso.
'''
title = 'Conversor de USD para EUR (EUR/USD = US$1.1294 at 11/28/2021)'
div = '-'*len(title)
#titulo
print( div, title, div, sep="\n" )

#current
# choice = input ('What is your choice? 1- USD TO EUR or 2- EUR TO USD [1/2]:')
usd = 5.61
eur = 6.35

#convert
usd_to_eur = usd * 1.1294
eur_to_usd = eur / 1.1294

#result
print(usd, "Dollars is", round(usd_to_eur, 2), "Euro")
print(eur, "Euro is", round(eur_to_usd, 2), "Dolars")
