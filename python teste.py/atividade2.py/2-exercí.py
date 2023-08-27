from re import T


carro1 = float(input("informe a distância percorrida: " ))
carro1 = float(input("informe o tempo que levou na percorrida: "))
carro2= float(input("informe a distância percorrida: "))
carro2 = float(input("informe o tempo que levou na percorrida: "))
distancia=carro1
tempo=carro1
distancia=carro2
tempo=carro2

velo_media = distancia/tempo
if velo_media > carro1:
    print("o vencedor é o carro1")
else:
    print("o vencedor é o carro2")
print("acabou ")



