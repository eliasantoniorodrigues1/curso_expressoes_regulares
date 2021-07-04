# Encontrando números válidos a través de expressão regular
# https://regex101.com/r/WiUATu/1
import re

string = '''
Válidos
0.0
00.00
000.000
+0.0
-00.00
+000.000
10
50
8.5
-8.5
+10.5005412136
1231345458.54654564
-133215646589.6543215648978977
+1.11123123
-0.154987
1.121654987
10.123
10.1
-1.1
Inválidos
10..2
++1213
--1235050
.124546
-.1231324
10.
.1
.10
10.
+10.
-10.
5a
b5
'''


# is_float = re.compile(r'^[+-]?\d+(?:\.)?\d+?$')
# is_int = re.compile(r'^[+-]?\d+?')


def is_float(string):
    return bool(re.search(r'^[+-]?\d+(?:\.)?\d+?$', string))


def is_int(string):
    return bool(re.search(r'^[+-]?\d+?$', string))


print(is_float('10'))
print(is_float('10..55'))
print(is_int('55'))

while True:
    numero = input('Digite um número: ')

    if is_int(numero):
        numero = int(numero)
        print(f'O número {numero} foi convertido para int.')
        continue
    if is_float(numero):
        numero = float(numero)
        print(f'O número {numero} foi convertido para float.')
        continue
