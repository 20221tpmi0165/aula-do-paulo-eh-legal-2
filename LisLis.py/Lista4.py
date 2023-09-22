ompra = []
resposta = "s"
while resposta == "s" :
    item = input("digite uma item para lista de compra,(para, ou digita ")
    resposta = str(input("quer continua "))

    for item in compra:
        if item.louwer == "para":
                break
        resposta = str(input("quer continua "))

    print(item)