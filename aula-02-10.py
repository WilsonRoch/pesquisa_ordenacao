import random
import time

class Util:
    @staticmethod
    def popular_lista(lista, tamanho):
        for _ in range(tamanho):
            lista.append(random.randint(0, tamanho))

    @staticmethod
    def menor_numero_sequencial(lista): # O(n)
        menor = lista[0]
        for i in lista:
            # qtd_comparacoes += 1
            if i < menor:
                menor = i
        
        return menor
    
    @staticmethod
    def menor_numero_ordenado(lista): # O(log n)
        lista.sort()
        return lista[0]

    @staticmethod
    def esta_contido_sequencial(numero, lista): # index of
        qtd_comparacoes = 0
        for i in range(0, len(lista)):
            qtd_comparacoes += 1
            if (numero == lista[i]):
                return i
        return qtd_comparacoes, -1

    @staticmethod
    def esta_contido_binaria(numero, lista): # O (log n) -- Arvore
        lista.sort()
        #original [8, 9, 5, 1, 2, 3, 3, 7, 10, 5]
        #.         0, 1, 2, 3, 4, 5, 6, 7, 8, 9
        #ordenado [1, 2, 3, 3, 5, 5, 7, 8, 9, 10]
        ini = 0
        fim = len(lista)-1
        qtd_comparacoes = 0
        while (ini <= fim):
            meio = int((ini+fim)/2)
            if (numero == lista[meio]):
                return meio
            if (numero < lista[meio]):
                fim = meio - 1
            else:
                ini = meio + 1
        return qtd_comparacoes, -1
    

def main():
    lista = []
    tamanho = 20
    Util.popular_lista(lista, tamanho)
    print(lista)

    numero = 30
    #print(numero in lista)
    #print(Util.menor_numero_sequencial(lista))
    #print(Util.menor_numero_ordenado(lista))

    inicio = time.perf_counter()
    print('pesuisa sequencial...')
    qtd_comparacoes, posicao = Util.esta_contido_sequencial(numero, lista)
    fim = time.perf_counter()
    total = fim - inicio
    print('comparacoes: ',qtd_comparacoes, ' Posicao: ', posicao, ' Tempo:', total)

    inicio = time.perf_counter()
    print('pesquisa binaria...')
    qtd_comparacoes, posicao = Util.esta_contido_binaria(numero, lista)
    fim = time.perf_counter()
    total = fim - inicio
    print('comparacoes: ',qtd_comparacoes, ' Posicao: ', posicao, ' Tempo:', total)

if __name__ == '__main__':
    main()