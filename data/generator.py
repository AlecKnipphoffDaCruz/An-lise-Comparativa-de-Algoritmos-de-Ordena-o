import numpy as np
from numpy import random as rd


def generate(scenario: str, size: int) -> np.ndarray:
    """
    Gera um np.ndarray de acordo com o cenário e tamanho informados.

    Cenários disponíveis:
        random      — valores aleatórios inteiros entre 0 e 1000 (caso médio)
        ascending   — vetor já ordenado em ordem crescente (melhor caso p/ Insertion)
        descending  — vetor em ordem decrescente (pior caso p/ Insertion/Selection)
    """
    # 'match' requer Python 3.10+
    match scenario:
        case "random":
            return rd.randint(0, 1001, size=size)
        case "ascending":
            return np.arange(size)
        case "descending":
            # Gera [size, size-1, ..., 1] — todos valores positivos (compatível com Radix)
            return np.arange(size, 0, -1)
        case _:
            raise ValueError(f"Cenário desconhecido: {scenario}")
