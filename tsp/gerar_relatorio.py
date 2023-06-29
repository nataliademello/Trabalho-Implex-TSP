from dataclasses import dataclass

from tsp.arquivos import arquivos
from tsp.metaheuristicas.hill_climbing import hill_climbing
from tsp.metaheuristicas.simulated_annealing import simulated_annealing


@dataclass
class ParametrosSimulatedAnnealing:
    T_max: float
    T_min: float
    k: float
    K_t: float


parametros_simulated_annealing = [
    # Caso A
    ParametrosSimulatedAnnealing(
        T_max=10,
        k=0.95,
        K_t=20,
        T_min=5,
    ),
    # Caso B
    ParametrosSimulatedAnnealing(
        T_max=100,
        k=0.9,
        K_t=25,
        T_min=10,
    ),
    # Caso C (definir)
    # ParametrosSimulatedAnnealing(
    #     T_max=-1,
    #     k=-1,
    #     K_t=-1,
    #     T_min=-1,
    # ),
]


@dataclass
class ParametrosHillClimbing:
    max_iter: int


parametros_hill_climbing = [
    ParametrosHillClimbing(
        max_iter=3,
    ),
    ParametrosHillClimbing(
        max_iter=5,
    ),
    ParametrosHillClimbing(
        max_iter=7,
    ),
]


def main():
    with open("relatorio.md", "w") as relatorio:

        def append(x: str):
            relatorio.write(x + "\n")
            print(x)

        append("# Relatório\n")

        append("## Resultados\n")
        for arquivo in arquivos:
            append(f"### {arquivo.nome}\n")

            melhor_distancia = arquivo.melhor_distancia
            append(f"- Melhor distância: {melhor_distancia}\n")

            append("#### Hill Climbing\n")

            append("max_iter | distância")
            append("--- | ---")

            for parametro in parametros_hill_climbing:
                melhor_solucao_hill_climbing = hill_climbing(
                    pontos=arquivo.pontos,
                    max_iter=parametro.max_iter,
                )
                append(
                    f"{parametro.max_iter} | {melhor_solucao_hill_climbing.distancia}"
                )

            append("")

            append("#### Simulated Annealing\n")

            append("k | K_t | T_max | T_min | distância")
            append("--- | --- | --- | --- | ---")

            for parametro in parametros_simulated_annealing:
                melhor_solucao_simulated_annealing = simulated_annealing(
                    k=parametro.k,
                    K_t=parametro.K_t,
                    pontos=arquivo.pontos,
                    T_max=parametro.T_max,
                    T_min=parametro.T_min,
                )

                append(
                    f"{parametro.k} | {parametro.K_t} | {parametro.T_max} | {parametro.T_min} | {melhor_solucao_simulated_annealing.distancia}"
                )

            append("")


if __name__ == "__main__":
    main()
