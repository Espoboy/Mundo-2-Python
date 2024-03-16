'''Aprendemos sobre os operadores condicionais de forma simples, mas,
dá pra colocar um operador detro do outro?

Sim, no nosso portugues, uma certa condição ficaria assim:'''

# SE numero == 5:
#    Faça algo
# SENÃO, SE numero == 3
#    Faça diferente
# OU ENTÃO, SE numero != 3
#    Desfaça
# SENÃO
#   Não faça

'''O se, nós conhecemos por if, o senão é o else, a mistura dos dois que é
o SENÃO, SE  e o OU ENTÃO, SE seria o else if, porém o próprio Python
encurta para elif, que pode nos dar mais opções de condições. 
Exemplo: '''

nome = str(input('\033[4;34mQual é seu nome?\033[m\n')).strip().upper()

if nome == 'JONG':
    print('\033[31mQue lindo nome varão!\033[m')
elif nome == 'EMILY':
    print('\033[35mQue nome lindo!!!\033[m \033[31m<3\033[m')
elif nome in 'Gael Israel Emanuel Jesus Paulo Pedro'.upper():
    print('Seu nome tem um significado \033[31mforte!\033[31m')
else:
    print('\033[32mSeu nome é bem normal!\033[m')
print('\033[33mTenha um ótimo dia,\033[m \033[4;31m{}!\033[m'.format(nome.capitalize()))

'''Estruturas com mais de um caminho, são estruturas aninhadas.'''

