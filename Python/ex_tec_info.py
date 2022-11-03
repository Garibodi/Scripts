
def raio(): #calcule o volume de uma esfera
    #faça um algoritmo para calcular o volume de umma esfera de raio R, em que R é um dado fornecido pelo usuário
    Raio = float(input("Digite o valor do raio:\n"))
    Volume = 4/3 * 3.14 * (Raio**3)
    print(Volume)
#raio()

def peso_ideal(): #imprima o peso ideal se masculino ou feminino
    #tendo como entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu peso ideal
    #para homens, (72.7 * h) - 58
    #para mulheres, (62.1*h) - 44.7
    sexo = str(input("Digite o sexo:\n"))
    altura = float(input("Digite a altura:\n"))
    p_masc = (72.7 * altura) - 58
    p_fem = (62.1 * altura) - 44.7

    if sexo.lower() == "masculino": 
        print(p_masc)
    elif sexo.lower() == "feminino":
        print(p_fem)
    else:
        (print("Digitou errado algum valor"))
#peso_ideal()

def imc():  #Imprima o IMC de acordo com peso e altura informado
    #Crie um algoritmo que:
    # 1. leia o peso e altura
    # 2. calcule o IMC pela fórmula IMC = peso /(altura**2)
    # 3. Mostre a condição
    #Abaixo de 18.5 == Abaixo do Peso
    #Entre 18.5 e 25 == Peso Normal
    #Entre 25 e 30 == Acima do Peso
    #Acima de 30 == Obeso

    peso = float(input("Qual teu peso?\n"))
    altura = float(input("Qual tua altura?\n"))
    imc = peso/(altura**2)
    print("Seu IMC calculado é: ", imc)
    if imc < 18.5:
        print("Abaixo do peso")
    elif imc >= 18.5 and imc < 25:
        print("Peso Normal")
    elif imc >= 25 and imc < 30:
        print("Acima do peso")
    elif imc >= 30:
        print("Obeso")
#imc()

def raiz(): # número inteiro que mais se aproxima da raiz quadrada de um número fornecido
    num = float(input("Escreva um número: \n"))
    raiz = num**(1/2)
    red = round(raiz,0)
    print("A raiz é: ", raiz)
    print("O número inteiro mais próximo é :", red)
#raiz()

def numeros(): #Encontre o maior e o menor número
    começo = float('-inf')
    final = float('inf')
    for num in [1, 200, 50, 30, 5000, 700, 800]:
        if num > começo:
            começo = num
    print("maior número é:\n", começo)
    for n in [1, 200, 50, 30, 5000, 700, 800]:
        if n < final:
            final = n
    print("menor número é:\n", final)
#numeros()
