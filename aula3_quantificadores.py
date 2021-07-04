# Meta caracteres: . ^ $ * + ? { } [ ] \ | ( )
# | Ou
# . Qualquer caracter com exceção da quebra de linha
# [] conjunto de caracteres - Lista
# * 0 ou n
# + 1 ou n
# ? 0 ou 1
# {n}
# {min, max} {1, } uma ou mais {, 10} De zero até 10
# {10} Especificamente 10
# {5, 10} De 5 até 10
# Aplicando em conjuntos () +, [a-zA-Z0-9]+ basta adicionar no final

import re

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
# O quantificador é aplicado ao caracter a esquerda.
print(re.findall(r'jo+ão+', texto, flags=re.IGNORECASE))  
print(re.sub(r'jo+ão+', 'Felipe', texto, flags=re.I))
print(re.sub(r'jo{1, }ão{1, }', 'Felipe', texto, flags=re.I))
print(re.search(r'[a-zA-Z]e{4}[a-zA-Z]', texto, flags=re.IGNORECASE))
# Como usar o POSIX no python
print(re.findall(r'[:alpha:]e{1, 4}[:alpha:]', texto))

texto2 = 'João ama ser amado'
print(re.findall(r'ama[do]{,2}', texto2))  # Prefiro essa forma de uso.
print(re.findall(r'ama[do]*', texto))
