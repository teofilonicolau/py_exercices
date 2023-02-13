# Faça um programa que leia um ângulo qualquer
#  e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
ang = float(input('Digite o ângulo que voçê deseja : '))
sen = math.sin(math.radians(ang))
print('O ângulo de {} tem o SENO de  : {:.2f} :'.format(ang, sen))
cos = math.cos(math.radians(ang))
print('O ãngulo de {} tem o COSSENO de :{:.2f} :'.format(ang, cos))
tang = math.tan(math.radians(ang))
print('O ângulo de {} tem a tangente de {:.2f} :'.format(ang, tang))