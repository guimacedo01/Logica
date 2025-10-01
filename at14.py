temperatura = float(input("Digite a temperatura: "))
if temperatura < 18:
    print("Frio")
elif 18 <= temperatura <= 25:
    print("Agradável")
else:
    print("Quente")