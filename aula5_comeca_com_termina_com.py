# Meta Caracteres:
# ^ - No inicio da expressão regular quer dizer COMEÇA COM dentro da lista NEGA o dado da lista.
# $ - TERMINA COM
# [^a-z] - LISTA NEGADA - qualquer coisa que não seja de a-z

import re

cpf = '147.852.963-12'

# Abaixo temos ? no mínimo 1 0-9 três posições com um ponto, esse grupo se repete duas vezes
# 0-9 três posições, 0-9 duas posições
print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))

# Expressão que começa com:
cpf2 = 'a 147.852.963-12 qualquer coisa'

# ?: dentro de um grupo estou dizendo para não salvar esse grupo na memória:
print(re.findall(r'^(?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2}?', cpf2))