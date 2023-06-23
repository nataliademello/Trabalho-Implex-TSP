import math
from random import random
from tsp.solucao import Ponto, Solucao


def simulated_annealing(
    pontos: list[Ponto],
    T_max: float,
    T_min: float,
    k: float,
    K_t: float,
) -> Solucao:
    T = T_max

    vc_solucao_corrente = Solucao.gerar_aleatoria(pontos)

    while T > T_min:
        t = 0

        vizinhanca = vc_solucao_corrente.vizinhanca()
        while t < K_t:
            vizinho = next(vizinhanca, None)

            if vizinho is None:
                return vc_solucao_corrente

            if vizinho.distancia < vc_solucao_corrente.distancia:
                vc_solucao_corrente = vizinho
                vizinhanca = vc_solucao_corrente.vizinhanca()

            else:
                chance_de_aceitar = vc_solucao_corrente.distancia - vizinho.distancia
                chance_de_aceitar = chance_de_aceitar / T
                chance_de_aceitar = math.exp(chance_de_aceitar)

                if random() < chance_de_aceitar:
                    vc_solucao_corrente = vizinho
                    vizinhanca = vc_solucao_corrente.vizinhanca()

            t += 1

        T *= k

    return vc_solucao_corrente
