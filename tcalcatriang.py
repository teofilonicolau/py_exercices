#Exercício Python 017: Faça um programa que leia o comprimento
#  do cateto oposto e do cateto adjacente de um triângulo retângulo
# . Calcule e mostre o comprimento da hipotenusa.

x = float(input('Comprimento do cateto adjacente : '))
y = float(input('Comprimento do cateto oposto :'))
h = (x ** 2 + y **2) ** (1/2)
print('A hipotenusa vai medir: {}'.format(h))