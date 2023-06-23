from dataclasses import dataclass
from functools import cached_property
from pathlib import Path

from tsp.solucao import Ponto


PASTA_ARQUIVOS: Path = Path().cwd() / "arquivos"


def processar_linha(
    linha: str,
) -> tuple[str, float, float]:
    linha = linha.strip()

    identificador, resto = linha.split(" ", 1)
    resto = resto.strip()

    x, resto = resto.split(" ", 1)
    x = float(x)

    resto = resto.strip()
    y = float(resto)

    return identificador, x, y


def ler_arquivo(
    caminho: Path,
) -> list[Ponto]:
    pontos: list[Ponto] = []

    with open(caminho, "r") as arquivo:
        for linha in arquivo:
            if linha == "\n":
                continue

            identificador, x, y = processar_linha(linha)

            ponto = Ponto(id=identificador, x=x, y=y)
            pontos.append(ponto)

    return pontos


@dataclass
class Arquivo:
    nome: str
    melhor_distancia: float

    @cached_property
    def pontos(self) -> list[Ponto]:
        return ler_arquivo(PASTA_ARQUIVOS / f"{self.nome}.tsp.txt")


arquivos: list[Arquivo] = [
    Arquivo(nome="att48", melhor_distancia=10628),
    Arquivo(nome="berlin52", melhor_distancia=7542),
    Arquivo(nome="bier127", melhor_distancia=118282),
    Arquivo(nome="eil76", melhor_distancia=538),
    Arquivo(nome="kroA100", melhor_distancia=21282),
    Arquivo(nome="kroE100", melhor_distancia=22068),
    Arquivo(nome="pr76", melhor_distancia=108159),
    Arquivo(nome="rat99", melhor_distancia=1211),
    Arquivo(nome="st70", melhor_distancia=675),
]
