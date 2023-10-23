dicionario ={}

quat = int(input("informe a quantidade de estudante "))
lista_alunos = []

for index in range (0, quat):
    nome = input("digite o nome dos estudante ")
    idade = input("digite a idade dos estudantes ")
    curso = input("digite o curso dos estudantes ")


    dicionario_estudante = {
        'nome':nome,'idade':idade, 'curso': curso }
    
    lista_alunos.append (dicionario_estudante)

with open('lista_alunos.txt', 'w') as arquivo:
    for estudante in lista_alunos:
        for chave, value in estudante.items():
            linha=f'{chave}:{value}\n'
            arquivo.write(linha)

print(f'o dicionario foi escrito no aquivo"(lista_aluno)".')