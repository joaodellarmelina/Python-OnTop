try:
  #! ENTRADA
  print("Dígite três valores reais quaisquer e distindos:")
  valor1 = float(input("Primeiro valor: "))
  valor2 = float(input("Segundo valor: "))
  valor3 = float(input("Terceiro valor: "))

  #! ULA & SAÍDA
  if (valor1 == valor2 or valor1 == valor3 or valor2 == valor3):
    print("Digite valores distindos, os valor são iguais")
  elif (valor1 > valor2 or valor1 > valor3):
      if (valor2 < valor3):
        print(f'o maior valor é {valor1} e {valor3}')
      else:
        print(f'o maior valor é {valor1} e {valor2}')
  else:
    print(f'o maior valor é {valor2} e {valor3}')


except Exception as ERRO:
  print("Digite uma valor valído")