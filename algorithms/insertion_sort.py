import time
import numpy as np


def insertion_sort(arr: np.ndarray) -> dict:
    # Cópia para não modificar o vetor original (mesmo vetor é passado aos outros algoritmos)
    array = arr.copy()
    comparisons = 0
    swaps = 0

    start = time.perf_counter()

    # Percorre o vetor a partir do segundo elemento, inserindo cada um na posição correta
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        # Desloca elementos maiores que 'key' uma posição à frente
        while j >= 0 and array[j] > key:
            comparisons += 1
            array[j + 1] = array[j]
            swaps += 1
            j -= 1
        # Conta a comparação que encerrou o while (ou que saiu por j < 0)
        comparisons += 1
        array[j + 1] = key

    elapsed = time.perf_counter() - start

    return {
        "sorted_array": array,
        "comparisons": comparisons,
        "swaps": swaps,
        "time": elapsed,
    }
