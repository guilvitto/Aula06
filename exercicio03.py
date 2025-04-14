alunos = int(input("Digite o num de alunos: "))
i=1
soma=0
media=0
while i <= alunos:

    notas= int(input("Digite as notas: "))

    soma=soma+notas

    i=i+1

media=soma/alunos
print(media)
