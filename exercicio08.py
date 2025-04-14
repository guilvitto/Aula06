n= int(input("Digite um valor que vai se repetir: "))
for x in range (1,n+1):
    print(x,end=" ")
    for y in range(1,x):
        print(x,end=" ")
    print()

