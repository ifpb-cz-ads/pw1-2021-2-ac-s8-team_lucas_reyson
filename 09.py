import random
n=random.randint(1,10)
x=int(input("Escolha um número entre 1 e 10: "))
x1=0
x2=0
if x==n:
	print("Você acertou!")

elif x!=n:
    x1 = int(input('Você errou, tente novamente: '))
    if x1==n:
        print("Você acertou!")

    elif x1!=n:
        x2 = int(input('Você errou, tente novamente: '))
        if x2==n:
            print("Você acertou!")

else:
	print("Você errou.")
