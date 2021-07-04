# Shorthands
# Letra minúscula PERMITIDO - Minúscula NEGADO
# \w -> [a-zA-Z0-9Á-ú_]
# \w -> [a-zA-Z0-9] -> re.A (pega somente a tabela ascci)
# \W -> [^a-zA-Z0-9Á-ú)] -> Retorna tudo menos palavras
# \d -> [0-9]
# \D -> [^0-9]
# \s -> [ \r\n\f\n\t] Qualquer tipo de espaço
# \S -> [^ \r\n\f\n\t] Negação de qualquer espaço.
# \r - recuo de carro
# \n - quebra de linha
# \t - tabulação
# \f -
# \v -

# \b - Encontra a borda (string vazia no começo ou no fim de cada palavra). Todas palavras que começa com flor
# \bflo\w+

# \B - não borda.

# Flags
# re.A -> ASCII
# re.I -> IGNORECASE
# re.I -> IGNORECASE
# re.M -> MULTILINE - ^ $
# re.S -> DOTALL

import re

# Selecionar todas as palavras de um texto

texto = """
João trouxe    flores para a sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.

Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso pão
de queijo.
Não canso de ouvir a Maria:
"Jooooooooãooooooooooooo, o café tá quentinho aqui. Veeeem Âeeeem"!

"""

print(re.findall(r'[a-z]+', texto))  # De a a z minuscula
print(re.findall(r'[a-zA-Z]+', texto))  # Encontra palavras
print(re.findall(r'[a-zA-Z0-9]+', texto)) # Texto e numero
print(re.findall(r'[a-zA-Z0-9Á-ú]+', texto))  # Palavras acentuadas, lower, upper e numeros
print(re.findall(r'\w+', texto, re.I))  # Palavras acentuadas, lower, upper e numeros
print(re.findall(r'\W+', texto, flags=re.I))
print(re.findall(r'\d+', texto))  # Somente digito
print(re.findall(r'\D+', texto, flags=re.I))  # Exceto digito
print(re.findall(r'\s+', texto, flags=re.I))  # Tudo que é espaço, caracter vazio e etc
print(re.findall(r'\S+', texto, flags=re.I))  # Tudo exceto espaços
print(re.findall(r'\bflo\w+', texto))   # Tudo que começa com flor
print(re.findall(r'flo\B', texto))   # Negação do começa com borda
print(re.findall(r'\w+e\b', texto))  # Tudo que termina com e
print(re.findall(r'\b\w{4}\b', texto))  # Palavras com 4 letras usando bordas

# =============================== FLAGS =======================

cpfs = '''
111.111.111-11  ABC
999.999.999-99  XRKI
555.555.555-55
'''
print(re.findall(r'(?:\d{3}\.){2}\d{3}-\d{2}', cpfs))
print(re.findall(r'^(?:\d{3}\.){2}\d{3}-\d{2}$', cpfs, flags=re.M))  # Usando a flag Multiline

texto2 = 'O João gosta de folia \ne adora ser amado'

print(re.findall(r'^o.*o$', texto2, flags=re.I))   # Pegando tudo DOTALL sem flag (dá erro por causa da quebra de linha
print(re.findall(r'^o.*o$', texto2, flags=re.I | re.S))  # Com duas flags
