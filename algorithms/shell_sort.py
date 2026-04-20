import time
import numpy as np


def shell_sort(arr: np.ndarray) -> dict:
    # Cópia para preservar o vetor original
    array = arr.copy()
    comparisons = 0
    swaps = 0
    n = len(array)

    start = time.perf_counter()

    # Sequência de gaps de Shell clássica: n/2, n/4, ..., 1
    gap = n // 2
    while gap > 0:
        # Para cada posição a partir do gap, faz uma inserção ordenada
        # usando o gap como passo (insertion sort intercalado)
        for i in range(gap, n):
            temp = array[i]
            j = i
            while j >= gap and array[j - gap] > temp:
                comparisons += 1
                array[j] = array[j - gap]
                swaps += 1
                j -= gap
            # Conta a comparação que encerrou o while (ou saída por j < gap)
            comparisons += 1
            array[j] = temp
        gap //= 2

    elapsed = time.perf_counter() - start

    return {
        "sorted_array": array,
        "comparisons": comparisons,
        "swaps": swaps,
        "time": elapsed,
    }
