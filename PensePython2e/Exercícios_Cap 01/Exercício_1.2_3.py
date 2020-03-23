Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Se você correr 10 quilômetros em 42 minutos e 42 segundos, qual é o seu passo médio (tempo por milha em minutos e segundos)? Qual é a sua velocidade média em milhas por hora?
>>> 
>>> tempo_s = 42 * 60 + 42
>>> milha = 10 / 1.61
>>> passo_médio = (tempo_s / milha) / 60
>>> vel_média = tempo_s / (60 * 60)
>>> 
>>> print(f'O passo médio será de {passo_médio:.2f} e velocidade média será {vel_média:.2f}.')
O passo médio será de 6.87 e velocidade média será 0.71.
>>> 