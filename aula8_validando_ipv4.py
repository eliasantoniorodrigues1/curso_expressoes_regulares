# Validando CPF e IP
# 0.0.0.0 a 255.255.255.255
# CPF não é número
# 025.258.963-10
# Validações diferentes ip é um range de 0 a 255
# CPF você pode validar por blocos
import re

cpf = '025.258.963-10'
cpf_reg_exp = re.compile(r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$')
# print(cpf_reg_exp.search(cpf))

# Validando ip
ip_reg_exp = re.compile(r'''
    ^
    (?:
        25[0-5]|  # 250-255
        2[0-4][0-9]|  # 200-249
        1[0-9]{2}|  # 100-199
        [1-9][0-9]|  # 10-99
        [0-9]  # 0-9
    )
    \.
    (?:
        25[0-5]|  # 250-255
        2[0-4][0-9]|  # 200-249
        1[0-9]{2}|  # 100-199
        [1-9][0-9]|  # 10-99
        [0-9]  # 0-9
    )
    \.
    (?:
        25[0-5]|  # 250-255
        2[0-4][0-9]|  # 200-249
        1[0-9]{2}|  # 100-199
        [1-9][0-9]|  # 10-99
        [0-9]  # 0-9
    )
    \.
    (?:
        25[0-5]|  # 250-255
        2[0-4][0-9]|  # 200-249
        1[0-9]{2}|  # 100-199
        [1-9][0-9]|  # 10-99
        [0-9]  # 0-9
    )
    $            
''', flags=re.VERBOSE)

# Mesma porém compacta
ip_reg_exp2 = re.compile(r'''
    ^
    (?:
    (?:
        25[0-5]|  # 250-255
        2[0-4][0-9]|  # 200-249
        1[0-9]{2}|  # 100-199
        [1-9][0-9]|  # 10-99
        [0-9]  # 0-9
    )
    \.?
    ){4}
    \b
    $
''', flags=re.X)


# Loop para criar 300 ips
for i in range(301):
    ip = f'{i}.{i}.{i}.{i}'
    print(f'{ip}, {ip_reg_exp2.findall(ip)}')
