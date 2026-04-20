import time
import numpy as np


def selection_sort(arr: np.ndarray) -> dict:
    # Cópia para preservar o vetor original
    array = arr.copy()
    comparisons = 0
    swaps = 0
    n = len(array)

    start = time.perf_counter()

    # A cada passagem, seleciona o menor elemento do subvetor não ordenado
    # e coloca na posição i
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if array[j] < array[min_idx]:
                min_idx = j
        # Só conta troca se realmente houve mudança de posição
        if min_idx != i:
            array[i], array[min_idx] = array[min_idx], array[i]
            swaps += 1

    elapsed = time.perf_counter() - start

    return {
        "sorted_array": array,
        "comparisons": comparisons,
        "swaps": swaps,
        "time": elapsed,
    }
