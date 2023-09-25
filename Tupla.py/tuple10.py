palavras = ("gato", "cachorro", "paralelepipede")
comprimentos = tuple(len(palavra)
for palavra in palavras)

for comprimento in comprimentos:
    print(comprimento)