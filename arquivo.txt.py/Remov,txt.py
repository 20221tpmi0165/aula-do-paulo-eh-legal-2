def remover_dados():
    nome = input("digite o nome ")
    idade = input("digite a idade ")
    ver_dados={
        "nome": nome,
        "idade": idade,
        }
    return ver_dados
def cria_arquivo(ver_dados):
    with open("ver_dados.txt", "w") as arquivo:
        for chave, valor in ver_dados.items():
            linha = (f"{chave}: {valor}\n")
            arquivo.write(linha)
            

if __name__=='__main__':
    ver_dados = remover_dados()
    cria_arquivo(ver_dados=ver_dados)


