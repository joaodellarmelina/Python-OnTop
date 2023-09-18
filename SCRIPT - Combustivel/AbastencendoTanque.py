
print("------------------------------------------------")
print("Todas informações que precisa antes de abastecer seu carro.")
print("------------------------------------------------")

try:
    print("Vamos descobrir o tamanho do seu tanque:")
    print("- Para isso, favor fornecer o valor da Largura, Altura e Profundidade (em metros):")
    print("ps.: No manual você também acha essas informações")
    Largura = float(input("Largura (Em metros): "))
    Altura = float(input("Altura (Em metros): "))
    Profundidade = float(input("Profundidade (Em metros): "))

    print("-----------------------------------------------")
    print("- Qual valor do Alcool e da Gasolina por litro no posto que abastece?")
    Alcool = float(input("Preço do alcool por litro: R$ "))
    Gasolina = float(input("Preço da gasolina por litro: R$ "))

    print("-----------------------------------------------")
    print("- Qual a proporção de cada ingrediente que quer colocar?")
    PA = float(input("Propoção de alcool (%): "))
    PG = float(input("Proporção de gasolina (%): "))

    print("-----------------------------------------------")
    medidaTanqueLAP = float(Largura * Altura * Profundidade)
    print(f"A medida do seu tanque é {medidaTanqueLAP: .2f} metros³")
    medidaTanqueLitro = medidaTanqueLAP * 1000
    print(f"Seu tanque cabe {medidaTanqueLitro: .2f} litros")

    PrecoLitroG = float(Gasolina * medidaTanqueLitro)
    PrecoLitroA = float(Alcool * medidaTanqueLitro)

    print(
        f'> O preço a ser pago para encher o seu Taque de combustivel com Gasolina é: R$ {PrecoLitroG: .1f}')
    print(
        f'> O preço a ser pago para encher o seu Taque de combustivel com Alcool é: R$ {PrecoLitroA: .1f}')

    print("-----------------------------------------------")

    if (PA + PG == 100):
        PA /= 100
        PG /= 100

        PA *= medidaTanqueLitro
        PG *= medidaTanqueLitro

        PA *= Alcool
        PG *= Gasolina

        print(f'O preço a ser pago com sua Proporção de Alcool é {PA: .1f}')
        print(f'O preço a ser pago com sua Proporção de Gasolina é {PG: .1f}')

    elif (PA + PG != 100):
        print("Favor fornecer um valor de PA e PG com as proporções corretas")


except Exception:
    print("Favor preencher um valor válido")


def TestaPorcetagem():
    if (PA + PG != 100):
        print("A soma de PA% (Proporção de Alcool) e a PG% (Proporção de Gasolina) precisa dar 100%")
