import time
import numpy as np


def merge_sort(arr: np.ndarray) -> dict:
    # Cópia para preservar o vetor original
    array = arr.copy()
    # Contadores compartilhados pelas chamadas recursivas
    # Obs.: "swaps" no merge sort é interpretado como número de escritas
    # no vetor destino (não há trocas tradicionais entre dois elementos)
    counters = {"comparisons": 0, "swaps": 0}

    start = time.perf_counter()
    _merge_sort_recursive(array, 0, len(array) - 1, counters)
    elapsed = time.perf_counter() - start

    return {
        "sorted_array": array,
        "comparisons": counters["comparisons"],
        "swaps": counters["swaps"],
        "time": elapsed,
    }


def _merge_sort_recursive(array: np.ndarray, left: int, right: int, counters: dict) -> None:
    # Caso base: subvetor com 0 ou 1 elemento já está ordenado
    if left < right:
        mid = (left + right) // 2
        _merge_sort_recursive(array, left, mid, counters)
        _merge_sort_recursive(array, mid + 1, right, counters)
        _merge(array, left, mid, right, counters)


def _merge(array: np.ndarray, left: int, mid: int, right: int, counters: dict) -> None:
    # Cria cópias das duas metades para facilitar a intercalação
    L = array[left:mid + 1].copy()
    R = array[mid + 1:right + 1].copy()

    i = 0  # índice da metade esquerda
    j = 0  # índice da metade direita
    k = left  # índice de escrita no vetor original

    # Intercala os dois subvetores comparando elemento a elemento
    while i < len(L) and j < len(R):
        counters["comparisons"] += 1
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        counters["swaps"] += 1
        k += 1

    # Copia elementos restantes da metade esquerda (se houver)
    while i < len(L):
        array[k] = L[i]
        counters["swaps"] += 1
        i += 1
        k += 1

    # Copia elementos restantes da metade direita (se houver)
    while j < len(R):
        array[k] = R[j]
        counters["swaps"] += 1
        j += 1
        k += 1
