from random import sample
from functools import cached_property
from math import sqrt
from dataclasses import dataclass
from itertools import pairwise
from typing import Iterator


@dataclass
class Ponto:
    """Armazena um ponto cartesiano."""

    id: str
    x: float
    y: float

    def distancia(self, outro_ponto: "Ponto") -> float:
        """Calcula a distância euclidiana entre dois pontos.

        Args:
            outro_ponto (Ponto): Ponto para calcular a distância.

        Returns:
            Distância euclidiana entre os pontos.
        """
        distancia_x = (self.x - outro_ponto.x) ** 2
        distancia_y = (self.y - outro_ponto.y) ** 2

        return sqrt(distancia_x + distancia_y)


@dataclass
class Solucao:
    """Armazena a lista de pontos que compõem uma solução."""

    pontos: list[Ponto]

    @cached_property
    def distancia(self) -> float:
        """Distância total da solução.

        Soma a distância de cada par sobreposto de pontos,
        e adiciona a distância entre o último e primeiro ponto.

        Returns:
            A distância total da solução.
        """  # noqa: E501
        distancia = 0
        for p1, p2 in pairwise(self.pontos):
            distancia += p1.distancia(p2)

        origem = self.pontos[0]
        final = self.pontos[len(self.pontos) - 1]

        distancia += final.distancia(origem)

        return distancia

    def gera_vizinho(self, i: int, k: int) -> "Solucao":
        """Gera um vizinho dessa solução.

        Para gerar o vizinho, os pontos de `i` até `k` da solução corrente
        são colocados em ordem reversa na nova solução.

        Args:
            i (int): Limite inferior do intervalo de pontos a serem trocados.
            k (int): Limite superior do intervalo de pontos a serem trocados.

        Returns:
            Vizinho da solução corrente com os pontos trocados.
        """
        vizinho: list[Ponto] = [Ponto("0", 0, 0)] * len(self.pontos)

        # repete os pontos iniciais da solução corrente até `i - 1`
        for j in range(i):
            vizinho[j] = self.pontos[j]

        # colocar os pontos de `i` até `k` da solução corrente em ordem reversa
        # ou seja:
        # vizinho[i] = solucao_corrente[k],
        # vizinho[i + 1] = solucao_corrente[k - 1]
        # vizinho[i + 2] = solucao_corrente[k - 2]
        # ...
        # vizinho[k] = solucao_corrente[i]
        for j in range(i, k + 1):
            indice_de_troca = k - j + i
            vizinho[j] = self.pontos[indice_de_troca]

        # repete os pontos finais da solução corrente de `k + 1` até o final
        for j in range(k + 1, len(self.pontos)):
            vizinho[j] = self.pontos[j]

        return Solucao(vizinho)

    def vizinhanca(self) -> Iterator["Solucao"]:
        """Gerador da vizinhança dessa solução (considerando a estratégia implementada).

        Os vizinhos são gerados invertendo sub-sequências da solução corrente.

        Yields:
            Uma solução vizinha da solução corrente.
        """  # noqa: E501
        for k in range(2, len(self.pontos) - 1):
            yield self.gera_vizinho(i=1, k=k)

        for i in range(2, len(self.pontos) - 1):
            for k in range(i + 1, len(self.pontos)):
                yield self.gera_vizinho(i=i, k=k)

    @classmethod
    def gerar_aleatoria(cls, pontos: list[Ponto]) -> "Solucao":
        pontos_embaralhados = sample(pontos, k=len(pontos))

        return Solucao(pontos=pontos_embaralhados)
