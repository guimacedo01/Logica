pai = True
mae = True
colega = True
idade = 19
dinheiro = 1001

entrar = (idade <= 18 and dinheiro <= 100) or pai or mae or colega
print(entrar)