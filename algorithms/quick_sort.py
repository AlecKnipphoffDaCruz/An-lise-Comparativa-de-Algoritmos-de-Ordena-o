import time
import numpy as np


def quick_sort(arr: np.ndarray) -> dict:
    # Cópia para preservar o vetor original
    array = arr.copy()
    # Usamos um dicionário para compartilhar contadores entre as chamadas recursivas
    counters = {"comparisons": 0, "swaps": 0}

    start = time.perf_counter()
    _quick_sort_recursive(array, 0, len(array) - 1, counters)
    elapsed = time.perf_counter() - start

    return {
        "sorted_array": array,
        "comparisons": counters["comparisons"],
        "swaps": counters["swaps"],
        "time": elapsed,
    }


def _quick_sort_recursive(array: np.ndarray, low: int, high: int, counters: dict) -> None:
    # Caso base: subvetor com 0 ou 1 elemento já está ordenado
    while low < high:
        pivot_idx = _partition(array, low, high, counters)

        # Recorre apenas no menor lado para limitar a profundidade da pilha.
        # O outro lado é processado via iteração no próprio loop.
        if pivot_idx - low < high - pivot_idx:
            _quick_sort_recursive(array, low, pivot_idx - 1, counters)
            low = pivot_idx + 1
        else:
            _quick_sort_recursive(array, pivot_idx + 1, high, counters)
            high = pivot_idx - 1


def _partition(array: np.ndarray, low: int, high: int, counters: dict) -> int:
    # Estratégia Lomuto: pivô é sempre o último elemento do subvetor
    pivot = array[high]
    i = low - 1  # posição do menor elemento encontrado até agora

    for j in range(low, high):
        counters["comparisons"] += 1
        if array[j] <= pivot:
            i += 1
            # Só troca se os índices forem diferentes (evita trocas redundantes)
            if i != j:
                array[i], array[j] = array[j], array[i]
                counters["swaps"] += 1

    # Coloca o pivô na sua posição final
    array[i + 1], array[high] = array[high], array[i + 1]
    counters["swaps"] += 1
    return i + 1
