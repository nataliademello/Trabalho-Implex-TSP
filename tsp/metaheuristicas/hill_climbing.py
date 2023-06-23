from typing import Iterator
from tsp.solucao import Ponto, Solucao


def encontra_melhor_vizinho(
    vizinhanca: Iterator[Solucao],
) -> Solucao:
    melhor_vizinho = next(vizinhanca)

    for vizinho in vizinhanca:
        if vizinho.distancia < melhor_vizinho.distancia:
            melhor_vizinho = vizinho

    return melhor_vizinho


def hill_climbing(
    pontos: list[Ponto],
    max_iter: int,
) -> Solucao:
    iter_atual = 0

    melhor = Solucao(pontos)

    while iter_atual < max_iter:
        encontrou_otimo_local = False

        vc_solucao_corrente = Solucao.gerar_aleatoria(pontos)

        # encontra ótimo local
        while not encontrou_otimo_local:
            vn_melhor_vizinho = encontra_melhor_vizinho(
                vc_solucao_corrente.vizinhanca()
            )

            if vn_melhor_vizinho.distancia < vc_solucao_corrente.distancia:
                vc_solucao_corrente = vn_melhor_vizinho

            else:
                encontrou_otimo_local = True

        iter_atual += 1

        # se o ótimo local é melhor que a melhor solução encontrada até agora, atualiza
        if vc_solucao_corrente.distancia < melhor.distancia:
            melhor = vc_solucao_corrente

    return melhor
