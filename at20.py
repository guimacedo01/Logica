valor_compra = float(input("Digite o valor da compra (em R$): "))
if valor_compra > 100:
    print("Você tem direito a um desconto!")
else:
    print("Não há desconto para compras de até R$ 100,00.")
