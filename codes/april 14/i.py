def custo_consumo(a):
    consumo = {2: 0, 3: 0, 5: 0, 7: 0}
    aux = a
    if aux > 200:
        consumo[2] = 100
        aux -= 200
        if aux > 30000:
            consumo[3] = 10000
            aux -= 30000
            if aux > 5000000:
                consumo[5] = 1000000
                aux -= 5000000
                if aux:
                    consumo[7] = aux / 7
            else:
                consumo[5] = aux / 5
        else:
            consumo[3] = aux / 3
    else:
        consumo[2] = aux / 2
    return consumo

def consumo_custo(d):
    return 2 * d[2] + 3 * d[3] + 5 * d[5] + 7 * d[7]

while True:
    linha = input()
    if linha == '0 0':
        break
    a, b = map(int, linha.split())
    consumo = custo_consumo(a)
    # if consumo[7]:
    #     meu = {2: 200, 3: 30000, 5: 5000000, 7: consumo[7] / 2}
    #     vizinho = {2: 200, 3: 30000, 5: 5000000, 7: consumo[7] / 2}
    # elif consumo[5]:
    #     meu = {2: 200, 3: 30000, 5: consumo[5] / 2, 7: 0}
    #     vizinho = {2: 200, 3: 30000, 5: consumo[5] / 2, 7: 0}
    # elif consumo[3]:
    #     meu = {2: 200, 3: consumo[3], 5: 0, 7: 0}
    #     vizinho = {2: 200, 3: consumo[3], 5: 0, 7: 0}
    # else:
    #     meu = {2: consumo[2] / 2, 3: 0, 5: 0, 7: 0}
    #     vizinho = {2: consumo[2] / 2, 3: 0, 5: 0, 7: 0}
    # cmeu = consumo_custo(meu)
    # novo_meu = custo_consumo(cmeu - b / 2)
    print(consumo_custo(consumo - b / 2))