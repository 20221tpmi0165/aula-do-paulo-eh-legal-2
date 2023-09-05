

esp = "s"
while (resp == "s"):
    nota = float(input("digite a nota: "))
    if nota >=7 and 10:
        print("media")
    else:
        print("essa não é media")
    resp = str(input("você quer continuar[s/n]".upper()))   

    
resp = "s"
resp = "s"
while (resp == "s"):
    valor =  int(input("digite o menor valor : "))
    if valor < 5:
        print(valor)
    else:
        print("pula esse")
    resp = str(input("você quer continuar[s/n]".upper()))   


rom random import randint
conputador = randint(1,100)
print("sou seu computador... acabei de pensar em um numero entre 1 a 100. ")
print("será que você consegui advinhar o qual foi? ")
acertou = False
while not acertou:
    jogador = int(input("qual o seu palpite? "))
    if jogador == conputador:
        acertou = True
    print(" acertou ! ")
print("acertou ")