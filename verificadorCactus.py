from collections import defaultdict

class VerificadorCactus:
    def __init__(self, quantidade_vertices):
        self.n = quantidade_vertices
        self.grafo = defaultdict(list)
        self.visitado = [False] * self.n
        self.pai = [-1] * self.n
        self.nivel = [-1] * self.n
        self.aresta_em_ciclo = set()

    def adicionar_aresta(self, u, v):
        self.grafo[u].append(v)
        self.grafo[v].append(u)

    def verifica_cactus(self):
        for v in range(self.n):
            if not self.visitado[v]:
                self.nivel[v] = 0
                if not self.dfs(v):
                    return False
        return True

    def dfs(self, v):
        self.visitado[v] = True

        for u in self.grafo[v]:
            if not self.visitado[u]:
                self.pai[u] = v
                self.nivel[u] = self.nivel[v] + 1
                if not self.dfs(u):
                    return False

            elif u != self.pai[v] and self.nivel[u] < self.nivel[v]:
                aresta = tuple(sorted((u, v)))

                if aresta in self.aresta_em_ciclo:
                    return False

                self.aresta_em_ciclo.add(aresta)

        return True


verificador = VerificadorCactus(5)
verificador.adicionar_aresta(0, 1)
verificador.adicionar_aresta(1, 2)
verificador.adicionar_aresta(2, 0)  
verificador.adicionar_aresta(1, 3)
verificador.adicionar_aresta(3, 4)
verificador.adicionar_aresta(4, 1)  

print("É um grafo cactus?", verificador.verifica_cactus())
