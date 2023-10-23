def ler_arquivo ():
    
    nome = input("digite o nome ")
    idade=input("digite  a idade ")
    curso=input("digite o curso ")

    
    lista_aluno = {
         "nome": nome,
        "idade": idade,
        "curso": curso,
       
    }
    return lista_aluno
    
def criar_arquivo(lista_aluno):
    
    with open("dados_aluno.txt","w")as arquivo:
        for chave,valor in lista_aluno.items():
                linha = f'{chave}:{valor}\n'
                arquivo.write(linha)


if __name__=='__main__':
    lista_aluno = ler_arquivo()
    criar_arquivo(lista_aluno=lista_aluno)

