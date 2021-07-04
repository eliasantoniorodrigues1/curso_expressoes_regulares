# Look around - lookahead - lookbehind
# Verifica o que está a frente/atrás existe para depois retornar a expressão.
# Exemplo verificar se existe Rodrigues e retornar Elias
import re
from pprint import pprint

texto = '''
ONLINE  192.168.0.1 GHIJK active
OFFLINE  192.168.0.2 GHIJK inactive
OFFLINE  192.168.0.3 GHIJK active
ONLINE  192.168.0.4 GHIJK active
ONLINE  192.168.0.5 GHIJK inactive
OFFLINE  192.168.0.6 GHIJK active
'''

# Positive lookahead
# pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(\w+)', texto))
# print(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?=active)', texto))

# Negative lookbahead
# print(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?!active)', texto))

# Pegando a frase inteira
# pprint(re.findall(r'(?=.*[^in]active).+', texto))

# Positive Lookbehind (Verifica se existe uma palavra antes do que eu estou checando.
pprint(re.findall(r'\w+(?<=ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto))

# Negative Lookbehind (Verifica se existe uma palavra antes do que eu estou checando.
pprint(re.findall(r'\w+(?<!ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto))



