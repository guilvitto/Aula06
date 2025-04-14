pin=123456
tentativas=1
resposta="Senha bloqueada!!"
while tentativas<=3:
    senha = int(input("Digite seu pin de 6 números: "))
    if senha==pin:
        resposta="login efetuado com sucesso!"
        break
    tentativas = tentativas + 1
print(resposta)