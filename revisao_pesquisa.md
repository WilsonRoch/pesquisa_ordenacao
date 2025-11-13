- Revisão geral: Pesquisa

- Pesquisa:
    - o que é e para que serve?
        Métodos de pesquisa são algoritmos que percorrem estruturas de dados para localizar (encontrar) ou recuperar (obter) um ou mais elementos com eficiência. Eles são essenciais porque, sem uma forma eficiente de acesso aos dados armazenados, a estrutura perde utilidade prática.

    - localizar versus recuperar
        Localizar: Apenas verifica se um elemento/registro existe e indica em qual posição ele está. (ex: procura por um item em uma lista, e descobre qual o indice dele nessa lista. Não retorna o valor desse item.)
        Recuperar: Retorna o próprio elemento/registro após ele ter sido localizado. (ex: Procura um elemento em uma lista e retorna o valor dele.)

    - complexidade das pesquisas: sequencial, binária, digital, hash
        O que é complexidade: Pode ser caracterizado como esforço, e quanto mais esforço, maior a complexidade. Quanto maior for a complexidade, menor a eficiência. Usamos o Big-O para medir como o número de operações cresce com o tamanho da entrada.

        - Melhor caso: mínimo de operações.
        - Caso médio: comportamento típico.
        - Pior caso: limite superior (garantia).

        A ordem (do melhor para o pior), considerando n grande, é:

            O(1) — constante
            O(log n) — logarítmica
            O(n) — linear
            O(n log n) — linearítmica
            O(n^2), O(n^3) — polinomial
            O(c^n) — exponencial
            O(n!) — fatorial

            Sequencial (lista de tamanha n)
                - Melhor: O(1) - elemento na primeira posição
                - Pior: O(n)

            Binária (PRECISA de lista ordenada)
                - Melhor: O(1)
                - Pior: O(log n)
                Parecido com árvore, pois a cada passo, o algoritmo elimina metade do espaço de busca (já que a lista está ordenada, fica mais facil).

            Digital (Trie, busca com base nos bits, usa árvore)
                Melhor caso: O(1) - palavra/caractere não é encontrada e a busca é interrompida
                - Busca por palavra: O(L) [L = tamanho da palavra] 
                - Busca por prefixo: O(L + K) [k = resultados listados]

            Hash


    - fluxo: armazenar, "ordenar" , pesquisar

    - saber os algoritmos:
        - pesquisa binária
        - pesquisa digital

    - teoria de tabelas hash:
        - tabela
        - função hash de endereçamento


