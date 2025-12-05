from collections import defaultdict

class VerificadorCactus:
    def __init__(self, quantidade_vertices):
        self.quantidade_vertices = quantidade_vertices
        self.grafo = defaultdict(list)
        self.visitado = [False] * quantidade_vertices
        self.aresta_em_ciclo = set()   
        self.pai = [-1] * quantidade_vertices
        self.total_ciclos = 0

    def adicionar_aresta(self, origem, destino):
        self.grafo[origem].append(destino)
        self.grafo[destino].append(origem)

    def verifica_cactus(self):
        for vertice in range(self.quantidade_vertices):
            if not self.visitado[vertice]:
                if not self.busca_profundidade(vertice):
                    return False
        return True

    def busca_profundidade(self, vertice):
        self.visitado[vertice] = True

        for vizinho in self.grafo[vertice]:
            if not self.visitado[vizinho]:
                self.pai[vizinho] = vertice
                if not self.busca_profundidade(vizinho):
                    return False

            elif vizinho != self.pai[vertice]:
                aresta = tuple(sorted((vertice, vizinho)))

                if aresta in self.aresta_em_ciclo:
                    return False

                self.aresta_em_ciclo.add(aresta)
                self.total_ciclos += 1

        return True



verificador = VerificadorCactus(5)
verificador.adicionar_aresta(0, 1)
verificador.adicionar_aresta(1, 2)
verificador.adicionar_aresta(2, 0)  
verificador.adicionar_aresta(1, 3)
verificador.adicionar_aresta(3, 4)
verificador.adicionar_aresta(4, 1)  

print("É um grafo cactus?", verificador.verifica_cactus())
print("Quant. de ciclos detectados:", verificador.total_ciclos)
