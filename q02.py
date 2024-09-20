# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
# IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

fibonacci = [0, 1]
indice = 1
numero = int(input('Digite um numero: '))

while(numero >= fibonacci[indice]):
    fibonacci.append(fibonacci[indice] + fibonacci[indice-1])
    indice += 1
    if(numero in fibonacci):
        print('O número', numero, 'pertence a sequência de Fibonacci.')
        break

if(fibonacci[indice] > numero):
    print('O número', numero, 'NÃO pertence a sequência de Fibonacci.')
