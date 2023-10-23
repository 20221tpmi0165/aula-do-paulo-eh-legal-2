def carrega_contato():

    qtd = int(input("quantidade de contatos "))
    telefone = input("digite numero telefone ")
    e_mail = input("digidte seu e-mail ")



    
    
    contato={
       
        "numero": "telefone",
        "endereço":"imail",
        
    }
    return contato

def cria_arquivo(contato):
     with open("contato.txt", "w") as arquivo:
        for chave, valor in contato.items():
            linha = (f"{chave}: {valor}\n")
            arquivo.write(linha)

if __name__=='__main__':
    contato = carrega_contato()
    cria_arquivo(contato=contato)
