# 5) Escreva um programa que inverta os caracteres de um string.
# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;

ordem = []
inversa = []

for i in range(4):
    numeros = input('Digite um número: ')
    ordem.append(numeros)

print(ordem)

for e in ordem[::-1]:
    print('Ordem inversa:', e, end=' ')
    inversa.append(e)

print(inversa)