import re
# Github da seção https://github.com/luizomf/regexp-python
# findall - Encontra todas as ocorrências do padrão
# search  - Encontra a primeria ocorrência e retorna o índice
# (retorna um objeto match)
# sub  - Substitui
# compile - Compilar expressões regulares
# r antes da expressão evita que seja necessa´rio digitar muitas barras para escapar 
# o caracter


string = 'Este é um teste de expressões teste regulares.'
print(re.search(r'teste', string))  # Para na primeira ocorrência
print(re.findall(r'teste', string)) # Retorna uma lista contendo os matchs
print(re.sub(r'teste', 'ABCD', string, count=1))  # Substitui os matchs, o count
# faz com que subistitua somente a primeira incidência. poderiamos usar flags também.

# Compila uma vez a expressão regular para ser utilizada em outras seções do
# código. Da forma abaixo você compila apenas uma vez a expressão regular.
regexp = re.compile(r'teste')
print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub('DEEF', string))
