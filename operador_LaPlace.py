#!/usr/local/bin/python3


class cores:

    ERRO = '\033[1;91m'
    NORMAL = '\033[0;0m'
    CERTO = '\033[1;34m'
    PERG = '\033\033[32m'


def exclui_linha(matriz_det, lugar):

    nova_matriz = []
    for i in range(len(matriz_det)-1):
        linha = []
        for j in range(len(matriz_det)):
            if j != lugar:
                linha.append(matriz_det[i+1][j])
        nova_matriz.append(linha)
    return nova_matriz


def calcula_determinante(matriz_pronta):

    determinante = 0
    if len(matriz_pronta) == 2:
        determinante += (matriz_pronta[0][0]*matriz_pronta[1][1]) - \
                        (matriz_pronta[0][1]*matriz_pronta[1][0])

    else:
        for i in range(len(matriz_pronta)):
            fator = matriz_pronta[0][i]
            determinante += fator*((-1)**(i)) *\
                calcula_determinante(exclui_linha(matriz_pronta, i))

    return determinante


def criar_matrizes(num_linhas, num_colunas):

    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            linha.append(
                float(input("Qual é o valor do elemento da" + ' ' +
                            "linha % d e coluna % d " % (i, j))))
        matriz.append(linha)
    print(cores.CERTO+"A matriz é"+cores.PERG)
    for linha in matriz:
        print(linha)

    return matriz


if __name__ == '__main__':

    num_linha = int(input("Qual a ordem de sua matriz quadrada ?"))
    matriz_feita = criar_matrizes(num_linha, num_linha)
    print(cores.CERTO+"O valor do determinante é"+cores.ERRO,
          calcula_determinante(matriz_feita))
