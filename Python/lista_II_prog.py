# leia 30 números e gere outro valor:
# pares: dobro
# ímpares: triplo

def ex1():
    list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    for n in list:
        if n%2==0:
            par = 2*n
            print("Estes são os pares:\n")
            print(par)
    for y in list:
        if y%2!=0:
            impar = 3*y
            print("Estes são os ímpares:\n")
            print(impar)
ex1()

#leia 50 números
#calcule quantos são 10% acima e quantos são 10% abaixo da média
def ex4():
    list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    média = list/50
    for n in list:
        if n >= média*1.1:
            maior = n[1:51]
            print(maior)
        if n <= média*0.9:
            menor = n[1:51]
            print(menor)
#ex4

#leia um conjunto, preencha matriz 10x10 e gere:
#lista dos menores valores para cada coluna
#lista dos maiores valores de cada linha
def ex11():
    matriz = [1,...,100]
    coluna1 = matriz [:11]
    coluna2 = matriz [10: 21]
    coluna3 = matriz [20: 21]
    for n in coluna1:
        print("x")
#ex11 (não faço ideia)
        








