res=0
num1= int(input("Digite o 1°número: "))
num2 = int(input("Digite o 2°número: "))
while num2==0 :
    num2 = int(input("Digite o 2°número DIFERENTE DE ZERO: "))
res = num1/num2
print(res)