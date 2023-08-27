desconto = 0
quantidade  = 0
valor_totalHaste = 0
totalPagar = 0
hasteaco = float(input(" digite a quantidade de  haste de aço vendida: "))
hastecobre = float(input("digite a quantidede de conbre vendidas: "))
hastealu = float(input("digite a quantidade de haste de auminio vendida: "))

valortotal_hastes = hasteaco * 2.50 + hastecobre * 4.00 + hastealu * 5.00

quantidadetotal_hastes = hasteaco + hastecobre + hastealu


if quantidadetotal_hastes < 6:
    print("Não tem desconto ")
elif 7 <= quantidade <= 15:
    desconto = (quantidadetotal_hastes * 10)/100
    print("O desconto é: ", desconto)
elif 16 <= quantidade <= 20:
    desconto = (quantidadetotal_hastes * 15)/100
    print("o desconto é: ", desconto)
elif 20 > quantidade:
    desconto = (quantidadetotal_hastes * 20)/100
    print("a quantidade vendida é: ",quantidadetotal_hastes)
    print("o desconto é: ",desconto)
    print(" o valor a pargar é: ",valortotal_hastes)

    