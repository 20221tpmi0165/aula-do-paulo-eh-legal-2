





consumo = 0
valor_pagar =0
tipo = "i-industrial, c-comercail, r-residencial"

tipo=input("informe o tipo de consumo: ")
consumo=float(input("informe a quantidade de consumo de energia: "))

i = 0.68 * consumo + 34
c = 0.37 * consumo + 45
r = 0.77 * consumo - 22

if tipo == i:
    valor_pagar = 0.68 * consumo +34
    print("i é o:",valor_pagar )
elif tipo == c :
    valor_pagar * 0.37 * consumo + 45
    print(" c é o: ",valor_pagar)
elif tipo == r :
    valor_pagar = 0.77 * consumo - 22
    print("r é o: ",valor_pagar)
print("acabou ")







