# Validando telefones
# Parão: (31) 9 9999-9999
import re
telefone = '''
(31) 9 9999-9999
3442-5595
34415665
31 3442-569
'''
# regex_exp = re.compile(r'(\(\d{2}\))?\s?\d?\s?\d{4}-\d{4}$')  # errada minha
# (\(\d{2}\))?\s?(\d)?\s?(\d{4})-?(\3)
regex_exp = re.compile(r'^(\(\d{2}\))\s(9\s?)(\d{4}-?\d{4})$', flags=re.MULTILINE)
print(regex_exp.findall(telefone))
