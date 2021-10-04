import json

dados = {'cliente': []}  # {} indica a criação de um dictionary/dicionário /
# [] indica a criação de um vector/matriz/lista/array

dados['cliente'].append({
    'nome': 'Juca',
    'telefone': '11999999999',
    'email': 'juca@iterasys.com.br'
})
dados['cliente'].append({
    'nome': 'Ana',
    'telefone': '21988888888',
    'email': 'ana@iterasys.com.br'
})


def criar_json():
    with open('clientes.json', 'w') as outfile:
        json.dump(dados, outfile, indent=2)


def ler_json():
    with open('clientes2.json') as outfile:  # se quiser ler o arquivo, sem bloqueá-lo, pode deixar sem o 'r'
        conteudo = json.load(outfile)
        print(json.dumps(conteudo, indent=2))  # -> pra ler o conteúdo do arquivo
        # for registro in conteudo['cliente']:
        #     print('nome: ', registro['nome']) # -> Pra ler linha por linha
        #     print('telefone: ', registro['telefone'])
        #     print('email: ', registro['email'])
        #     print(json.dumps(registro, indent=2)) # -> pra ler tudo no registro)


def ler_json_adicionar_lista():
    with open('clientes2.json') as outfile:  # se quiser ler o arquivo, sem bloqueá-lo, pode deixar sem o 'r'
        conteudo = json.load(outfile)
    # print(conteudo['cliente'])
    for registro in conteudo['cliente']:
        dados['cliente'].append(registro)
    with open('clientes.json', 'w') as outfile:
        json.dump(dados, outfile, indent=2)


def testar_criar_json():
    criar_json()
    print(json.dumps(dados, indent=2))


def testar_ler_json():
    print('Leitura do JSON por linha / campo:')
    ler_json()


def testar_ler_json_adicionar_lista():
    ler_json_adicionar_lista()
    print(json.dumps(dados, indent=2))
