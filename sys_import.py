#escreva o nome do programa e mais 3 coisas

import sys
print(sys.argv)
sys.argv[1] = sys.argv[1] + "awdwa"
print(sys.argv[1], "hello")

#or

import sys
print(sys.argv)
trecho = sys.argv[1]
n1 = sys.argv[2]
n2 = sys.argv[3]
lenght = len(trecho[0 : ])
print(lenght)