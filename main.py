# 1 - imports / bibliotecas

# 2 - Classes

# 3 - Métodos e Funções
# def = definition = definição
def calcular_area_do_retangulo(largura, comprimento):
    return largura * comprimento


def calcular_area_do_quadrado(lado):
    return lado ** 2


def calcular_area_do_triangulo(largura, comprimento):
    return largura * comprimento // 2


def contagem_progressiva(inicio, fim):
    for numero in range(inicio, fim):  # range é uma lista de valores, ex: range(10) = [0,1,2,3,4,5,6,7,8,9]
        print(numero)


# range possui essa característica: range(fim) (começa no 0) / range(inicio, fim) ex: range(2,4) = [2,3]
# range(inicio, fim, quantos números pula) - ex: range(2,10,3) = [2,5,8]
# também pode ser inverso, ex: range(10,2,-2) = [10,8,6,4] / entretanto range(10,2) será vazio.


def apoiar_candidado(nome, vezes):
    for numero in range(vezes):
        # contador = numero + 1
        # print(f'{nome} - {contador}')
        # print(nome, ' - ', str(numero + 1).zfill(2))  # preenche uma string com 0 a esquerda
        print(nome, ' - ', format(numero + 1, '02d'))   # aplica a formatação de 0 a esquerda em decimal (int)


def brincar_de_plim(fim):
    for numero in range(1, fim + 1):
        if numero % 4 == 0:
            print('PLIM!')
        else:
            print(format(numero, '02d'))
            # print('{:0>2}'.format(numero))


# estrutura de identificação / execução do script

# chamar a função de cálculo da área do retângulo
if __name__ == '__main__':
    resultado = calcular_area_do_retangulo(3, 4)
    print(f'A área do retâgulo é de {resultado} m²')

    # chamar função de cálculo da área do quadrado
    resultado = calcular_area_do_quadrado(5)
    print(f'A área do quadrado é de {resultado} m²')

    # chamar função de cálculo da área do triângulo
    resultado = calcular_area_do_triangulo(4, 3)
    print(f'A área do triângulo é de {resultado} m²')

    # executar uma contagem progressiva
    contagem_progressiva(1, 10)

    # exibir um nome várias vezes
    apoiar_candidado('batata', 5)

    # brincar de Plim do Silvio Santos (resto da divisão por 4 igual a 0)
    brincar_de_plim(16)
