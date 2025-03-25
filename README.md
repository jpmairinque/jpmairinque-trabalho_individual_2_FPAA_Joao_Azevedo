# Trabalho Individual 2 - MaxMin Select - João Pedro Mairinque

## Algoritmo MaxMin Select

O algoritmo de seleção MaxMin Select segue a abordagem dividir para conquistar, onde o problema é dividido em duas sublistas e utiliza recursão para encontrar os elementos. Nesta atividade, analiso a complexidade assintótica da implementação do algoritmo em Python, pelo método de contagem de operações e pelo Teorema Mestre.

A aplicação da recursividade reduz o número de comparações necessárias para encontrar o menor e o maior valor da lista. A explicação de cada linha está contida em comentários no algoritmo, no arquivo *functions.py*.


## Complexidade Assintótica (Contagem de operações)

O algoritmo divide o array em duas partes aproximadamente iguais até que os casos base sejam alcançados. Os casos base são:

- n = 1 (nenhuma comparação é feita)
- n = 2 (uma única comparação é feita)

Em cada nível da recursão, o algoritmo realiza 𝑂(1) operações para combinar os resultados.

Dois subproblemas são resolvidos (2T).

O número de níveis da recursão é proporcional a log₂ 𝑛, já que o tamanho do problema é reduzido pela metade a cada nível.

Em cada nível, são feitas `2^𝑘⋅𝑂(1)` operações, onde 𝑘 é o nível da recursão.

Dessa forma, o número de operações cresce linearmente com n, e a complexidade assintótica é 𝑂(n).

## Complexidade Assintótica (Teorema mestre)

Considerando a recorrência `𝑇(𝑛) = 2𝑇 (𝑛 / 2) + 𝑂(1)` do algoritmo, temos:

- a = 2
- b = 2
- f(n) = 𝑂(1)

Calculamos p = log 𝑏 𝑎 = log₂ 2 = 1

Comparando 𝑂(1) com 𝑂(n), o custo externo é menor que o custo da recursão, nos levando ao **Caso 1**.

Logo, `𝑇(𝑛) = Θ(n)`


## Execução


### Executando o projeto


Acesse a raiz do projeto no terminal e execute:

```bash
python3 main.py
```

### Caso não possua o python

### MacOS

Instale o python 3 com Homebrew

```bash
brew install python
```

### Windows

1. Baixe o instalador do Python no site oficial:  
   [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)
2. Durante a instalação, marque a opção **"Add Python to PATH"**.
3. Após a instalação, abra um novo terminal e confirme a instalação com:

```bash
python --version
```

## Saída da Execução

```
Digite uma série de números separados por espaço: 1 5 3 5 4 1 5 4 8 
Menor elemento: 1, Maior elemento: 8
Tempo de execução: 0.000061 segundos
```

## Documentação e links úteis

- [Divisão e Conquista - Wikipedia](https://pt.wikipedia.org/wiki/Divis%C3%A3o_e_conquista)
- [Divisão e conquista - IME](https://www.ime.usp.br/~pf/analise_de_algoritmos/aulas/divide-and-conquer.html)

## Licença

Este projeto está licenciado sob a Licença MIT. e execute:
