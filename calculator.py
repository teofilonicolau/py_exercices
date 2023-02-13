#Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:

#Soma
#Subtração
#Multiplicação
#Divisão
#Caso seja inserido um número de operação que não exista,
#  o resultado deverá ser 0.

print('Digite um número: ')
numero1 =int(input())
print('Digite um outro número :')
numero2 = int(input())
print('Digite a operação :')
operacao = input()

if operacao == '+':
   resultado = numero1 + numero2
   print('A soma é ',resultado)
elif operacao == '-':
   resultado = numero1 - numero2
   print('A subtração é',resultado)
if operacao == '*':
   resultado = numero1 * numero2
   print('A multiplicação é',resultado)
if operacao == '/':
   resultado = numero1 / numero2
   print('A divisão é',resultado) 
else:
   print('Resultado  é:0')   



