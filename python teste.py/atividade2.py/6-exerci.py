media=float(input("digite o valor da media do aluno: "))
faltas=float(input("digite o números de faltas do aluno: "))

if media>=7 and faltas <=32:
    print("aprovado")
elif media <=7 and faltas <=32:
    print ("Reprovado por media ")
elif media >=7 and faltas > 32:
    print ("Reprovado por faltas ")
else:
    pritint ("Reprovado por media e faltas")
