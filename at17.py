num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num2 != 0:
    if num1 % num2 == 0:
        print(f"{num1} é divisível por {num2}")
    else:
        print(f"{num1} não é divisível por {num2}")
else:
    print("Divisão por zero não é permitida.")