# 1 - imports / bibliotecas


# 2 - Classes

# 3 - Métodos e Funções
# def = definition = definição
# chamar a função de cálculo da área do retângulo
def calcular_area_do_retangulo(largura, comprimento):
    resultado = largura * comprimento
    print(f'A área do retâgulo é de {resultado} m²')
    return resultado


# chamar função de cálculo da área do quadrado
def calcular_area_do_quadrado(lado):
    resultado = lado ** 2
    print(f'A área do quadrado é de {resultado} m²')
    return resultado


# chamar função de cálculo da área do triângulo
def calcular_area_do_triangulo(largura, comprimento):
    resultado = largura * comprimento // 2
    print(f'A área do triângulo é de {resultado} m²')
    return resultado


# executar uma contagem progressiva
def contagem_progressiva(inicio, fim):
    for numero in range(inicio, fim):  # range é uma lista de valores, ex: range(10) = [0,1,2,3,4,5,6,7,8,9]
        print(numero)


# range possui essa característica: range(fim) (começa no 0) / range(inicio, fim) ex: range(2,4) = [2,3]
# range(inicio, fim, quantos números pula) - ex: range(2,10,3) = [2,5,8]
# também pode ser inverso, ex: range(10,2,-2) = [10,8,6,4] / entretanto range(10,2) será vazio.


# exibir um nome várias vezes
def apoiar_candidado(nome, vezes):
    for numero in range(vezes):
        # contador = numero + 1
        # print(f'{nome} - {contador}')
        # print(nome, ' - ', str(numero + 1).zfill(2))  # preenche uma string com 0 a esquerda
        print(nome, ' - ', format(numero + 1, '02d'))  # aplica a formatação de 0 a esquerda em decimal (int)


# brincar de Plim do Silvio Santos (resto da divisão por 4 igual a 0)
def brincar_de_plim(fim):
    for numero in range(1, fim + 1):
        if numero % 4 == 0:
            print('PLIM!')
        else:
            print(format(numero, '02d'))
            # print('{:0>2}'.format(numero))


def sair():
    print('Obrigado e volte sempre!')


# def calcular_menu(argumento):
#     return {
#         1: calcular_area_do_retangulo(3, 4),
#         2: calcular_area_do_quadrado(5),
#         3: calcular_area_do_triangulo(4, 3),
#         4: contagem_progressiva(1, 10),
#         5: apoiar_candidado('batata', 5),
#         6: brincar_de_plim(16),
#         'Z': sair()
#
#     }.get(argumento, 'Opção Inválida')
def calcular_menu(argumento):
    if argumento == '1':
        calcular_area_do_retangulo(3, 4)
    elif argumento == '2':
        calcular_area_do_quadrado(5)
    elif argumento == '3':
        calcular_area_do_triangulo(4, 3)
    elif argumento == '4':
        contagem_progressiva(1, 10)
    elif argumento == '5':
        apoiar_candidado('batata', 5)
    elif argumento == '6':
        brincar_de_plim(16)


# estrutura de identificação / execução do script
if __name__ == '__main__':
    continua = 'a'

    while continua.upper() != 'Z':
        print('#' * 20,
              '\n#                                  #',
              '\n#          MENU DE OPÇÕES          #',
              '\n#      1 - Área do Retângulo       #',
              '\n#      2 - Área do Quadrado        #',
              '\n#      3 - Área do Triângulo       #',
              '\n#      4 - Contagem Progressiva    #',
              '\n#      5 - Apoiar Candidado        #',
              '\n#      6 - Brincar de PLIM         #',
              '\n#                                  #',
              '\n#      Z - Sair                    #',
              '\n#                                  #',
              '\n', '#' * 20)
        resposta = input('Escolha sua Opção:\n')

        if resposta.upper() != 'Z':
            if resposta.isdigit() and 6 >= int(resposta) >= 1:
                calcular_menu(resposta)
            else:
                sair()
                break
        else:
            sair()
            break
