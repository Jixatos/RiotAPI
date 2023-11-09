import requests

def inputBar():
    camp = input("Search: ").strip().lower().capitalize()
    return camp

def GET(nomeCampeao):
    try:
        url = f"https://ddragon.leagueoflegends.com/cdn/13.22.1/data/pt_BR/champion/{nomeCampeao}.json"
        requisicao = requests.get(url)
        dic = requisicao.json()
        data = dic['data']
        return data
    except Exception as e:
        print("Erro no GETCampeao: ",e)

def GETCampeoes():
    try:
        url = "https://ddragon.leagueoflegends.com/cdn/13.22.1/data/pt_BR/champion.json"
        requisicao = requests.get(url)
        dic = requisicao.json()
        data = dic['data']
        campeoes = [campeao for campeao in data.keys()]
        return campeoes
    except Exception as e:
        print("Erro no GETCampeoes: ",e)

def arrayCampeao(data, nomeCampeao):
    campeao = {}
    data = data[nomeCampeao]
    campeao['nome'] = data['id']
    campeao['lore'] = data['lore']
    return campeao

def imprimirLista():
    conf = True
    while conf:
        conf = input("Você quer imprimir a lista?\nResponda com Sim ou Não: ").upper()
        match conf:
            case 'SIM' | 'S':
                print("Aqui é uma lista de campeões para você pesquisar:")
                print(', '.join(campeoes))
                conf = False
            case 'NÃO' | 'NAO' | 'N':
                conf = False
            case _:
                print("Por favor, responda apenas com Sim ou Não.")

def saudacoes():
    print("Pesquise um campeão do League of Legends e conheça um pouco sobre sua história.")
    print("Caso queira a LISTA de campeões, digite no campo abaixo 'lista'.")
    print("Caso queira SAIR, digite no campo abaixo 'sair'.")
    print('Digite na barra de pesquisa o nome do campeão.')

#Teste
test = True
while test:
    campeoes = GETCampeoes()
    saudacoes()
    search = inputBar()
    if search in campeoes:
        data = GET(search)
        campeao = arrayCampeao(data, search)
        print(f"Nome do campeão: {campeao['nome']}\nHistória: {campeao['lore']}")
    elif search == 'Lista':
        imprimirLista()
    elif search == 'Sair':
        print('Obrigado, tchau tchau!')
        test = False
    else:
        print("Este campeão não existe ou foi digitado errado.")