sexo=input("diga o sexo da pessoa: ")
peso=float(input("digite o valor do peso: "))
altura=float(input("Quantos metro de altura? "))
idade=float(input("digite a  idade: "))
if sexo=="M":
    Homem = 66 + (13.7*peso) + 5.0*altura-6.8*idade
    print(Homem)
else:
    Mulher = 663 + (9.6*peso) + 1.8 * altura-4.7*idade
    print("calorDiaria",Mulher)

