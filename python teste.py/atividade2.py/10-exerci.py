salBruto=float(input("digite o salario bruto "))
imposto=0
sliquido=salBruto-imposto
if salBruto<=1903.98:
    print("Isento")
elif salBruto>=1903.99 and salBruto<=2826.65:
    imposto=(salBruto*7.5)/100
    print(imposto)
elif salBruto>=2826.66 and salBruto<=3751.05:
    imposto=salBruto*0.15-548.82
    print(imposto)
elif salBruto>=3751.06 and salBruto<= 4664.68:
    imposto=salBruto*0.225-636.13
    print(imposto)
else: 
    imposto=salBruto*0.275-869.36
print(imposto)

