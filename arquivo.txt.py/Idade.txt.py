def calcular_idade():
    idades = [55, 25, 60]
    return idades

def calcular_media(idades):
    
    soma = sum(idades)
    media = soma / len(idades)
    return media

def cria_arquivo(media):
    with open("calcular_media.txt", "w") as arquivo:
        arquivo.write(f'Média: {media}\n')

if __name__ == "__main__":
    idades = calcular_idade()
    media_idades = calcular_media(idades)
    cria_arquivo(media_idades)

    idades = calcular_idade()
    media_idades = calcular_media
    
    