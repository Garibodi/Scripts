# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want {} pieces of item {} for {} dollars."
# print(myorder.format(quantity, itemno, price))


# quantity = input("Escreva quantos items \n")
# itemno = 567
# price = 49.95
# myorder = "I want to \"pay\" \n {2} dollars for \n {0} pieces of item \n {1}."
# print(myorder.format(quantity, itemno, price)) 


texto = "1Escreva"

def check():
    if texto.startswith("Esc"):
        return bool(check)

if check() == True:
    print("safe")
else:
    print("not true")

if texto.isdigit() == True:
    print("Only digits")

if texto.isalpha() == True:
    print("Only letters")
else:
    print("Letras e Texto")