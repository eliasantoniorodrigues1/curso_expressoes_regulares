# Meta caracteres: . ^ $ * + ? { } [ ] \ | ( )
# | Ou
# . Qualquer caracter com exceção da quebra de linha
# [] conjunto de caracteres - Lista

import re

texto = """
João trouxe    flores para a sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.

Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso pão
de queijo.
Não canso de ouvir a Maria:
"Joãooooooooooooo, o café tá printnho aqui. Veeeem"!

"""
print(re.findall(r'João|Maria', texto, re.IGNORECASE))
