def ler_busca():
    nome = input("digite o nome que esta a  procurar ")
    idade= input("digite a idade ")
    curso= input("digite o curso ")

    busca_aluno = {
        'Nome': nome,
        'Idade': idade,
        'Curso': curso,
    }
    return busca_aluno
def criar_arquivo(busca_aluno):

    with open('busca_aluno.txt','w')as arquivo:
        for chave, valor in busca_aluno.items():
                linha = f'{chave}:{valor}\n'
                arquivo.write(linha)
                
if __name__ == "__main__":
    busca_aluno = ler_busca()
    criar_arquivo(busca_aluno=busca_aluno)


