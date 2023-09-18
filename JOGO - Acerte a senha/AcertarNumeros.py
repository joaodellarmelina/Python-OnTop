import numpy
import math

def sortear(MIN = 1, MAX = 100, SIZE = 1):
  sorte = numpy.random.randint(MIN, MAX, SIZE)[0]
  return sorte

def tentativas(MIN = 1, MAX = 100):
  return math.ceil(math.log2(MAX - MIN))

def VamosComecar():
      print("-------------------------")
      print("O GAME IRÁ COMEÇAR!!!")
      print("Definindo valor...")

      tentativa = tentativas()
      random = sortear()
      
      print("SENHA DEFINIDA.")
      print("-------------------------")
      guess = 0

      while guess != random:
          
          if (tentativa == 0):
            print("-------------------------")
            print(f'{tentativa} restantes...')
            print("Voce perdeu :(")
            print(f"A senha era {random}.")
            print("-------------------------")
            break
          else:
            guess = int(input(f"Voce tem {tentativa} tentativas restantes... Qual a senha correta? "))
            if (guess > random):
              print("-------------------------")
              print("NÃO NÃO! A SENHA É MENOR.")
              print("-------------------------")
              tentativa -= 1
            elif (guess < random):
              print("-------------------------")
              print("NÃO NÃO! A SENHA É MAIOR.")
              print("-------------------------")
              tentativa -= 1

            elif(guess == random):
              print("-------------------------")
              print("PARABENS VOCE ACERTOU!!!")
              print(f"Faltavam só {tentativa} tentativa.")
              print(f"De fato a senha era {random}.")
              print("-------------------------")
              break

try:
    print("ACERTE A SENHA")
    print("Pressione (2) para ver como o jogo funciona, (1) para começar e (0) para cancelar")
    start = int(input("= "))

    while (start != 1 and start != 0 and start != 2):
      print("Essa não é uma opção valida.")
      print("Pressione (2) para ver como o jogo funciona, (1) para começar e (0) para cancelar")
      start = int(input("= "))

    if (start == 0):
      print("Bye Bye!")
    
    elif (start == 1):
       VamosComecar()
    
    elif (start == 2):
      print("REGRAS: O sistema irá gerar um número aleatorio de 1-100 e você terá 7 tentativas para acertar, a cada tentativa o sistema irá te avisar se o seu proximo chute precisa ser maior ou menor. ")
      print("Clique (1) para começar e (0) para cancelar")
      start2 = int(input("= "))
      if (start2 == 1):
        VamosComecar()
      elif (start2 == 0):
        print("Bye Bye!")

      while start2 != 1 and start2 != 0:
        print("Essa não é uma opção valida.")
        print("Clique (1) para começar e (0) para cancelar")
        start2 = int(input("= "))
        if (start2 == 1):
          VamosComecar()
        elif (start2 == 0):
          print("Bye Bye!")

except Exception: 
   print("Você não foi legal... :(")
   print("Digíte um número inteiro, poxa!")