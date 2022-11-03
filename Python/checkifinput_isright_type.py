seq = "abcd"
n1 = "20"
n2 = "49"

def teste():
    dadosinput = [seq, n1, n2]
    for x in dadosinput:
        if type(x) == str:
            print("string ok")
            return True
        else:
            print("not string")
            return False

if teste() ==True:
    print("deu bom")
else:
    print("Uma das paradas tá errada")