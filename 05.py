def pesquise(lista, valor):
    for x, e in enumerate(lista):
        if e == valor:
            return x + 1
    return None

num = int(input('Informe o número que deseja buscar na lista: '))
busca = pesquise([7,39,8,17], num)
print(f'O número {num} está na posição {busca}')