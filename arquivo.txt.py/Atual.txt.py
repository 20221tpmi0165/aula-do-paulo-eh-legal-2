def ler_informacoes():

    nome = input("digite o nome do estudante ")
    idade = input("digite a idade do estudate ")
    diciplina = input("digite a diciplina ")


    informacoes = {
        "nome":nome,"idade":idade, 
        "curso": 'curso', 
        }

    return informacoes

def cria_arquivo(informacoes_estudante):

    with open('informacoes_estudante.txt','w')as arquivo:
        for items_informcoes in informacoes_estudante:   
            for chave,value in informacoes_estudante.items():
                linha = f'{chave}:{value}\n'
                arquivo.write(linha)

if __name__=='__main__':
    informacoes_estudante = ler_informacoes()
    cria_arquivo(informacoes_estudante = informacoes_estudante)
