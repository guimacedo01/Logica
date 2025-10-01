letra = input("Digite 'M' para Masculino ou 'F' para Feminino: ").strip().upper()

if letra == "M":
    print("Masculino")
elif letra == "F":
    print("Feminino")
else:
    print("Opção inválida")