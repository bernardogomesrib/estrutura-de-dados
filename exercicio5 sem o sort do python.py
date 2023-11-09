def reorganizar(lista):
    topo = len(lista)
    inicio = 0

    for k in range(int(len(lista)//2)):
        menor = lista[inicio]
        maior = lista[inicio]
        localmenor = inicio
        localmaior = inicio
        for i in range(inicio,topo):
            if menor > lista[i]:
                menor = lista[i]
                localmenor = i
            if maior < lista[i]:
                maior = lista[i]
                localmaior = i

        if localmenor != inicio:
            lista[localmenor], lista[inicio] = lista[inicio], lista[localmenor]

        if localmaior == inicio:
            localmaior = localmenor

        if localmaior != topo - 1:
            lista[localmaior], lista[topo - 1] = lista[topo - 1], lista[localmaior]

        topo -= 1
        inicio += 1
    return lista


l2d=[list(map(int,input().split())) for i in range(2)]
l2d = l2d[0]+l2d[1]
l2d = reorganizar(l2d)
print(l2d)