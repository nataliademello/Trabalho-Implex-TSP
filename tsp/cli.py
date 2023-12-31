from tsp.arquivos import arquivos
from tsp.solucao import Ponto, Solucao
from tsp.metaheuristicas.hill_climbing import hill_climbing
from tsp.metaheuristicas.simulated_annealing import simulated_annealing


def executar_simulated_annealing(pontos: list[Ponto]) -> Solucao:
    T_max = input("Digite a temperatura inicial: ")
    k = input("Digite a razão de resfriamento (decimais separados por '.'): ")
    K_t = input("Digite a quantidade de iterações: ")
    T_min = input("Digite a temperatura final: ")

    melhor_solucao = simulated_annealing(
        T_max=float(T_max),
        T_min=float(T_min),
        k=float(k),
        K_t=float(K_t),
        pontos=pontos,
    )

    return melhor_solucao


def executar_hill_climbing(pontos: list[Ponto]) -> Solucao:
    max_iter = input("Digite o número máximo de iterações: ")
    max_iter = int(max_iter)
    print("=" * 38)

    melhor_solucao = hill_climbing(pontos, max_iter)

    return melhor_solucao


def main():
    for i, arquivo in enumerate(arquivos):
        print(f"{i + 1}: {arquivo.nome}")

    numero_arquivo = input("Digite o número do arquivo: ")
    arquivo = arquivos[int(numero_arquivo) - 1]
    print("=" * 29)

    pontos = arquivo.pontos
    melhor_distancia = arquivo.melhor_distancia

    meta_heuristicas = ["Simulated Annealing", "Hill Climbing"]
    for i, meta_heuristica in enumerate(meta_heuristicas):
        print(f"{i + 1}: {meta_heuristica}")

    meta_heuristica = input("Digite o número da metaheurística: ")
    meta_heuristica = meta_heuristicas[int(meta_heuristica) - 1]
    print("=" * 36)

    if meta_heuristica == "Simulated Annealing":
        solucao = executar_simulated_annealing(pontos)

    elif meta_heuristica == "Hill Climbing":
        solucao = executar_hill_climbing(pontos)

    else:
        raise ValueError("Metaheurística inválida")

    print(f"A solução encontrada possui distância {solucao.distancia}")
    print(f"A melhor solução existente é de distância {melhor_distancia}")


if __name__ == "__main__":
    main()
