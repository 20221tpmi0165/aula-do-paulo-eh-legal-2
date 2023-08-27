

sexo=input("digo o sexo da  pessoa ")
idade=float(input("diga a idade da pessoa: "))
sexo = "M"
sexo = "F"

if sexo == "M":
    if idade >21:
        print("\n a pessoa é masculino e maior de idade")
    else:
        print("\n a pessoa é masculino e menor de idade")
if sexo =="F":
    if idade > 18:
        print("\n a pessoa e feminino e é maior de idade ")
    else:
        print("\n a pesso é feminina e menor de idade ")
