myloop1.py
for x in range(11):
    print (x)


myloop2.py
for x in range (101):
    print(x)


myloop3.py
numero = int(input("digite um numero para ver a tabuada: "))

#imprima a tabuada do numero fornecido
print(f"Tabuado do{numero}: ")

for i in range (1,11):
    resultado = numero + i
    print(f"{numero} + {i} = {resultado}")


myloop4.py
soma = 0
cont = 0 
for c in range (1, 10):
    num = int(input("digite o {} numero: ".format(c)))
    if num % 2 ==0:
        soma+=num
        cont+=1
print( "o total de  par são",soma)


myaloop5.py
listaNum = []
maior = 0
menor = 0
for c in range(0,5):
    listaNum.append(int(input("digite um valor para posição (c)")))
    if c == 0:
        maior = menor = listaNum[c]
    else:
        if listaNum[c]>maior:
            maior = listaNum[c]
        if listaNum[c]<menor:
            menor = listaNum[c]

print ("-" *30)
print(f"Você digitou o valor {listaNum} ")
print(f"O maior valor digitado foi {maior}")
print(f"O menor vaor digitado for {menor}")


myloop6.py
n = int(input("digite a qte "))
print(n)
# 0, 1, 1, 2, 3, 5, 8, 13
# n = 3
# 0, 1,1  
# n = 5
n1=0
n2=1
resposta = 1 + 2 

for x in range (1,2):
    resposta = n1 + n2
    print(resposta)
    n1 = n2
    n2=resposta
valor_anterior = 0
cont  = 0
for i in range (1,n-1):
    if cont == 0:
        print(valor_anterior)
    else:
        print(resposta)


myloop7.py
n=int(input("digite a qtd "))
i = n
while (i>1):
    i = 1 -1
    n = n*1
print("fatorial é {} numero é {},".format(i,n))


myloop8.py
or num in range(2, 51):
    is_prime = True
    
    
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    
    
    if is_prime:
        print(num)



        
    

        


