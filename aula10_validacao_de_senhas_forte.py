# validando senhas forte
import re

senha_forte_regexp = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*).{12,}$', flags=re.M)

senhas = """
VÁLIDAS
OVg_5d5)}4jZ
K`~hz68YW]f3
l|4fy}AT"0V7
|al|53IlPC4+
Udw3^1vMX%,0

SEM MINÚSCULAS
13Q&Q^3!NU6^
4(M7^W={8LW4
9>`;OK54L~M3
"8~W$GUY7=00
=>U2 X67T3#W

SEM MINÚSCULAS E NÚMEROS
=/UM&SJ<T;]R
R`&??G_IEZ<S
F}V:MB("E=&W
`]R~GIUSZ>_=
${LP[;P:BHO?

SEM NÚMEROS CARACTERES E MINÚSCULAS
XFPLKOEQORYW
CFCOIKNWVQMP
NKQQALZPMWZQ
NQXNMPTADTUP
JZZNPBKKCCFJ

QUANTIDADE INVÁLIDA
LGYSIQ
CYWMUZ
HIVDZR
DOMIAH
ZOESLU
"""
print(senha_forte_regexp.findall(senhas))
