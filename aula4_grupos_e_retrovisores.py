import re

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

# Grupos parecem com conjuntos (lista), porém quando usamos um grupo ele
# deixa de ser OU e passar ser E, busca exatamente aqueles caracteres.

# (Elias|Rodrigues)+
# Grupos são salvos na memória você acessa passando um número de referencia
# \1

texto = """
<p>Frase 1</p><p>Frase 2</p><p>Frase 3</p><div>Frase 4 </div> 

"""
# Comportamento Greedy (Guloso) Vai tentar o último match e retornar
# de uma vez só.
print(re.findall(r'<[pdiv]{1,3}>.*<\/[pdiv]{1,3}>', texto))


# Comportamento Non Greedy - Vai retornando sempre que encontrar.
print(re.findall(r'<[pdiv]{1,3}>.*?<\/[pdiv]{1,3}>', texto))

# Usando grupos no exemplo acima:
print(re.findall(r'<([pdiv]{1,3})>.*?<\/\1>', texto))
