import sys
#parametro generalizado para n-rainhas
n = int(sys.argv[1])

vetor = [-1]*n
pilha = []
fila = []

#desenha a linha do tabuleiro com a rainha
def desenha_linha(vet):
    linha = ""
    for i in range(n):
        if(vet[i] == 1):
            linha = (linha+"O")
        else:
            linha = (linha+"#")
    return linha

#desenha o tabuleiro com as rainhas
def desenha(mat):
    print("+"+("-"*n)+"+")
    for i in range(n):
        print("|"+desenha_linha(mat[i])+"|")
    print("+"+("-"*n)+"+")

#cria uma matriz com as rainhas no tabuleiro
def coloca_no_tabuleiro(vet):
    tabuleiro = []
    for i in range(n):
        tabu = [0]*n
        tabu[vet[i]] = 1
        tabuleiro.append(tabu)
    return tabuleiro

#procura se a rainha ja esta colocado na coluna
def procura(vet,j):
    for k in vet:
        if(k == j):
            return False
    return True

#busca o proximo campo vazio(-1) do vetor
def busca_vazio(vet):
    k = 0
    while vet[k]!= -1:
        k=k+1
    return k

#busca em profundidade onde o mesmo retorna o vetor estado solucao, utilizando uma pilha de vetor. a visita e realizada a mais a direita
def bf(p,i):
    i=0
    while(p != []):
        est = p[len(p)-1]
        p = p[:len(p)-1]
        for k in range(n):
            if(procura(est,k)):
                i = busca_vazio(est)
                if(i != 0):
                    if(abs(est[i-1]-k)>1):
                        if(i < n):
                            aux = est[:]
                            aux[i] = k
                            if(i == n-1):
                                return aux
                            p.append(aux)
                else:
                    if(i < n):
                        aux = est[:]
                        aux[i] = k
                        if(i == n-1):
                            return aux
                        p.append(aux)
    return []
#busca em largura  onde o mesmo retorna o vetor estado solucao, utilizando uma fila de vetor. a visita e realizada mais a esquerda
def bl(f,i):
    i=0
    while(f != []):
        est = f[0]
        f = f[1:]
        for k in range(n):
            if(procura(est,k)):
                i = busca_vazio(est)
                if(i != 0):
                    if(abs(est[i-1]-k)>1):
                        if(i < n):
                            aux = est[:]
                            aux[i] = k
                            if(i == n-1):
                                return aux
                            f.append(aux)
                else:
                    if(i < n):
                        aux = est[:]
                        aux[i] = k
                        if(i == n-1):
                            return aux
                        f.append(aux)
    return []

#coloca o estado inicial na pilha
pilha.append(vetor)

reso_bf = bf(pilha,0)
if(reso_bf == []):
    print("sem resolucao")
else:
    print("Busca em Profundidade")
    print("vetor solucao")
    print(reso_bf)
    print("tabuleiro com n-rainhas")
    desenha(coloca_no_tabuleiro(reso_bf))

#reseta o vetor
vetor = [-1]*n

#coloca o estado inicial na fila
fila.append(vetor)

reso_bl = bl(fila,0)
if(reso_bf == []):
    print("sem resolucao")
else:
    print("Busca em Largura")
    print("vetor solucao")
    print(reso_bl)
    print("tabuleiro com n-rainhas")
    desenha(coloca_no_tabuleiro(reso_bl))
