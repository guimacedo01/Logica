nota = float(input("digite a nota do aluno(0 a 10): "))
if nota < 0 or nota > 10:
    print("Nota inválida no sistema, nota deve ser entre 0 e 10")
elif nota >= 7:
    print("Aluno aprovado")
else:
    print("Aluno reprovado")