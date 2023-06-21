import random
import os

numero1=int(input('Digite seu primeiro número: '))
numero2=int(input('Digite seu segundo número: '))
numero3=int(input('Digite seu terceiro número: '))
numero4=int(input('Digite seu quarto número: '))
numero5=int(input('Digite seu quinto número: '))
numero6=int(input('Digite seu sexto número: '))
numeros=[numero1,numero2,numero3,numero4,numero5,numero6]
intervaloNum=range(61)
soma=int(0)


while True:
    soma=soma+1
    listaAtual=random.sample(intervaloNum, 6)
    print(numeros)
    print(listaAtual)
    print(soma)

    if listaAtual != numeros:
        print("NO")
        os.system("cls")
        continue        
    else:
        print("You won!")
        break
