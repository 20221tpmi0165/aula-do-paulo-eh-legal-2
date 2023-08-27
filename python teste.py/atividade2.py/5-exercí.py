nome_aluno = input("digite o nome do aluno: ")
nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
media = (nota1 + nota2)/2
if (media < 5):
    print("aluno reprovado")
else:
    if(media >5) or (media <=7):
        print("o aluno esta de recuperação ")
    else:
        if(media > 7) or (media <=10):
            print("o aluno está aprovado ")
    






