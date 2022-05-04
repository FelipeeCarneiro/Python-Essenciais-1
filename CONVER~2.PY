#Conversor de temperatura
title = 'Conversor de temperatura'
div_title = '-'*len(title)
print(div_title,title,div_title,sep="\n")
celcius = 20
kelvin = 293.15
fahrenheit = 68.0

celcius_to_kelvin = kelvin + 273.15
celcius_to_fahrenheit = celcius*9/5 + 32

kelvin_to_celcius = celcius - 273.15
kelvin_to_fahrenheit = kelvin * 9/5 - 459.67

fahrenheit_to_celcius = (fahrenheit - 32) * 5/9
fahrenheit_to_kelvin = (fahrenheit + 459.67) * 5/9 

print(
    'Settings for room temperature\n(ºC):',celcius,div_title,
    'celcius_to_kelvin',round(celcius_to_kelvin,2),
    'celcius_to_fahrenheit',round(celcius_to_fahrenheit,2),
    'kelvin_to_celcius',round(kelvin_to_celcius,2),
    'kelvin_to_fahrenheit',round(kelvin_to_fahrenheit,2),
    'fahrenheit_to_celcius',round(fahrenheit_to_celcius,2),
    'fahrenheit_to_kelvin',round(fahrenheit_to_kelvin,2),div_title,sep="\n"
    )