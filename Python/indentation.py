x = float(input("Escreva um número de 0 a 100:"))
if x >= 0 and x < 100:
    print(x , "Está dentro do alcance")
    if x >= 20 and x <=80 :
        print(x,"está apertado")
        if x > 30 and x <= 50:
            print(x , "está justo")
else :
    print(x, "é fora de escala")
print("Boa")
