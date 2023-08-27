km=float(input("digite o valor de kilometro rodados: "))
l=float(input("quantaos litro de gasolina gastou? "))
consumo = (km/l)
if consumo <8:
    print("venda o carro!")
elif consumo ==8 and consumo ==14:
    print("Econômico!")
elif consumo >12:
    print("Super Econômico")
    

