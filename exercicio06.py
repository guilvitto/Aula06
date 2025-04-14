n1= float(input("Digite a nota da 1a: "))
while n1<0 or n1>10 :
    n1= float(input("Valor inválido. Digite a nota da 1a: "))

n2= float(input("Digite a nota da 2a: "))
while n2<0 or n2>10:
    n2 = float(input("Valor inválido. Digite a nota da 2a: "))

media = (n1+n2)/2
print(media)