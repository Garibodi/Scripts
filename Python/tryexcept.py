idade = input("Escreva tua idade:   ")
try:
    idade = int(idade)
except:
    idade = -1
if idade >0:
    print("Your age is", idade)
else:
    print("Não é um número, tente de novo")
