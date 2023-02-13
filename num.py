def mostrar_numero():
  numero_valido = True
  while(numero_valido):
    print('Coloque o número menor que 100')
    try:
      num = int(input())
      if(num < 100) and (num > 0):
        print('Beleza voce inseriu um numero ', num)
        numero_valido = False
      else:
        print('Voce precisa colocar o numero menor que  100')
    except:
      print('Presta atençao abestado')