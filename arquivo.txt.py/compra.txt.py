def produtos():
    nome = input("digite o nome do produtos ")
    preco= input("digite o preçoa ")
    produtos = (nome,preco)


    ler_Items={
        "item_1": "preço",
        "item_2": "preço",
        "item_3": "preço",
        "item_4": "preço"
        }
    return ler_Items
def cria_arquivo(ler_items):

    with open("ler_items.txt","w")as arquivos:
        for linha in ler_items.items():
            for chave, valor in produtos:
                linha = f'{chave}:{valor}\n'
                arquivos.write(linha)


if __name__=='__main__':
    ler_items=produtos
    cria_arquivo(ler_items=ler_items)


  