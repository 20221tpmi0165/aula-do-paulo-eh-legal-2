import json


def carregar_contatos():
    try:
        with open("contatos.json", "r") as arquivo:
            contatos = json.load(arquivo)
    except FileNotFoundError:
        contatos = {}
    return contatos


def salvar_contatos(contatos):
    with open("contatos.json", "w") as arquivo:
        json.dump(contatos, arquivo)


def criar_contato(contatos):
    nome = input("Nome: ")
    endereco = input("Endereço: ")
    telefones = []
    while True:
        telefone = input("Telefone (ou deixe em branco para parar): ")
        if not telefone:
            break
        telefones.append(telefone)
    contatos[nome] = {"endereco": endereco, "telefones": telefones}
    print(f"Contato '{nome}' criado com sucesso!")


def listar_contatos(contatos):
    for nome, info in contatos.items():
        print(f"Nome: {nome}")
        print(f"Endereço: {info['endereco']}")
        print("Telefones:")
        for telefone in info["telefones"]:
            print(telefone)
        print()


def deletar_contato(contatos):
    nome = input("Digite o nome do contato a ser deletado: ")
    if nome in contatos:
        del contatos[nome]
        print(f"Contato '{nome}' deletado com sucesso!")
    else:
        print(f"Contato '{nome}' não encontrado.")


def editar_contato(contatos):
    nome = input("Digite o nome do contato a ser editado: ")
    if nome in contatos:
        endereco = input("Novo endereço: ")
        telefones = []
        while True:
            telefone = input("Novo telefone (ou deixe em branco para parar): ")
            if not telefone:
                break
            telefones.append(telefone)
        contatos[nome] = {"endereco": endereco, "telefones": telefones}
        print(f"Contato '{nome}' editado com sucesso!")
    else:
        print(f"Contato '{nome}' não encontrado.")

def main():
    contatos = carregar_contatos()

    while True:
        print("Menu:")
        print("1. Criar Contato")
        print("2. Listar Contatos")
        print("3. Deletar Contato")
        print("4. Editar Contato")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_contato(contatos)
        elif opcao == "2":
            listar_contatos(contatos)
        elif opcao == "3":
            deletar_contato(contatos)
        elif opcao == "4":
            editar_contato(contatos)
        elif opcao == "5":
            salvar_contatos(contatos)
            print("Contatos salvos. Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()