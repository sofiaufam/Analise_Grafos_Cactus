# Verificador de Grafo Cactus em Python

Este projeto implementa um **verificador de grafos do tipo *cactus*** utilizando o algoritmo de **Busca em Profundidade (DFS)**.  
Um grafo é considerado *cactus* quando **cada aresta pertence a no máximo um único ciclo**.

---

## Funcionalidades

- Criação de grafos não direcionados
- Inserção de arestas
- Verificação automática se o grafo é do tipo *cactus*
- Detecção de ciclos usando DFS

---

## Lógica Utilizada

O algoritmo utiliza:
- Vetor de vértices visitados
- Vetor de pai para evitar retornar pela mesma aresta
- Controle de nível (profundidade)
- Um conjunto (`set`) para garantir que **nenhuma aresta participe de mais de um ciclo**

Sempre que uma aresta de retorno é encontrada, ela é marcada como pertencente a um ciclo.  
Se alguma aresta já pertencer a um ciclo anterior, o grafo **não é cactus**.

---

## Requisitos

- Python 3.x  
Não é necessária nenhuma biblioteca externa.

---

## Como Executar

1. Salve o código em um arquivo, por exemplo:

`verificador_cactus.py`

2. Execute no terminal:

```python3 verificador_cactus.py```

3. Saída esperada:

`É um grafo cactus? True`

