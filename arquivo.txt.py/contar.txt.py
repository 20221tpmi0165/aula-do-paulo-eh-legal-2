import pprint
import json

def contar_estudante():
    curso_A = input("Digite quantos estudantes: ")
    curso_B = input("Digite quantos estudantes: ")


    quant_estudante={
       "curso_A": curso_A,
       "curso_B": curso_B,
    }

    return quant_estudante

def criar_arquivo(quant_estudante):
    data = quant_estudante
    with open("quant_estudante.txt","w")as arquivo:
       json.dump(data, arquivo, indent=4)


if __name__ == "__main__":
    quant_estudante = contar_estudante()
    print(quant_estudante)
    criar_arquivo(quant_estudante)