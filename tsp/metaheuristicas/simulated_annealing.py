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
    # embaralha os pontos e assume como sendo a solução corrente
    vc_solucao_corrente = Solucao.gerar_aleatoria(pontos)
    # enquanto a temperatura for maior que a temperatura mínima (temperatura final), ou seja, até T<Tmin
    while T > T_min:
        t = 0
        # essa parte de gerar a vizinhança está fora do próximo while para que caso a solução corrente não seja alterada,
        # a mesma vizinhança não seja gerada novamente
        vizinhanca = vc_solucao_corrente.vizinhanca()
        while t < K_t:
            # vizinho recebe próximo vizinho
            vizinho = next(vizinhanca, None)
            # caso não existam mais vizinhos, retorna a solução corrente considerando-a como melhor solução
            if vizinho is None:
                return vc_solucao_corrente
            # se a distância do vizinho for menor que a distância da solução corrente (ou seja, melhor),
            # faz a solução corrente receber o vizinho
            if vizinho.distancia < vc_solucao_corrente.distancia:
                vc_solucao_corrente = vizinho
                # troca a vizinhança pela vizinhança da nova solução corrente
                vizinhanca = vc_solucao_corrente.vizinhanca()

            else:
                # vc_solucao_corrente.distancia - vizinho.distancia corresponde a aval(vc) - aval(vn) no pdf do trabalho
                chance_de_aceitar = vc_solucao_corrente.distancia - vizinho.distancia
                chance_de_aceitar = chance_de_aceitar / T
                chance_de_aceitar = math.exp(chance_de_aceitar)

                if random() < chance_de_aceitar:
                    vc_solucao_corrente = vizinho
                    # troca a vizinhança pela vizinhança da nova solução corrente
                    vizinhanca = vc_solucao_corrente.vizinhanca()
                    
            # incrementa o numero de iterações 
            t += 1
        # multiplica a temperatura atual pela razão de resfriamento
        T *= k
        

    return vc_solucao_corrente
