from typing import Iterator
from tsp.solucao import Ponto, Solucao


def encontra_melhor_vizinho(
    vizinhanca: Iterator[Solucao],
) -> Solucao:
    # melhor_vizinho recebe o próximo vizinho
    melhor_vizinho = next(vizinhanca)
    
    for vizinho in vizinhanca:
        # se a distância do vizinho for menor (ou seja, melhor) que a distância do melhor vizinho, atualiza
        if vizinho.distancia < melhor_vizinho.distancia:
            melhor_vizinho = vizinho

    return melhor_vizinho


def hill_climbing(
    pontos: list[Ponto],
    max_iter: int,
) -> Solucao:
    iter_atual = 0

    melhor = Solucao(pontos)
    # enquanto a iteração atual for menor que o número máximo de iterações 
    while iter_atual < max_iter:
        encontrou_otimo_local = False
        #embaralha os pontos e assume como sendo a solução corrente
        vc_solucao_corrente = Solucao.gerar_aleatoria(pontos)

        # encontra ótimo local
        while not encontrou_otimo_local:
            vizinhanca_solucao_corrente = vc_solucao_corrente.vizinhanca()
            vn_melhor_vizinho = encontra_melhor_vizinho(
               vizinhanca_solucao_corrente
            )
            # se a distância do melhor vizinho for melhor que a distância da solução corrente, a solução
            # corrente vai receber o melhor vizinho
            if vn_melhor_vizinho.distancia < vc_solucao_corrente.distancia:
                vc_solucao_corrente = vn_melhor_vizinho

            else:
                encontrou_otimo_local = True

        iter_atual += 1

        # se o ótimo local é melhor que a melhor solução encontrada até agora, atualiza
        if vc_solucao_corrente.distancia < melhor.distancia:
            melhor = vc_solucao_corrente

    return melhor
