#Aluno Aprovado ou Reprovado

nota = float(input("Digite a nota do aluno (0 a 10): "))
if 0 <= nota <= 10: 
    if nota >= 6:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
else:
    print("Nota inválida. Digite uma nota entre 0 e 10.")