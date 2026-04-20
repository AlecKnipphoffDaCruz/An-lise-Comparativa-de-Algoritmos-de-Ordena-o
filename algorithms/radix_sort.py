import time
import numpy as np


def radix_sort(arr: np.ndarray) -> dict:
    # Cópia para preservar o vetor original
    array = arr.copy()
    # Radix sort não faz comparações entre elementos (ordena por dígito)
    # "swaps" aqui é o número de escritas no vetor de saída
    comparisons = 0
    swaps = 0

    start = time.perf_counter()

    # Caso de vetor vazio: nada a fazer
    if len(array) == 0:
        elapsed = time.perf_counter() - start
        return {
            "sorted_array": array,
            "comparisons": comparisons,
            "swaps": swaps,
            "time": elapsed,
        }

    # Encontra o maior valor para saber quantos dígitos processar
    max_val = int(array.max())

    # Ordena por dígito, do menos significativo para o mais significativo (LSD)
    exp = 1
    while max_val // exp > 0:
        array, swaps_pass = _counting_sort_by_digit(array, exp)
        swaps += swaps_pass
        exp *= 10

    elapsed = time.perf_counter() - start

    return {
        "sorted_array": array,
        "comparisons": comparisons,
        "swaps": swaps,
        "time": elapsed,
    }


def _counting_sort_by_digit(array: np.ndarray, exp: int):
    # Counting sort estável usando o dígito na posição 'exp' como chave
    n = len(array)
    output = np.zeros(n, dtype=array.dtype)
    count = np.zeros(10, dtype=int)
    swaps = 0

    # Conta a frequência de cada dígito (0 a 9)
    for i in range(n):
        digit = (int(array[i]) // exp) % 10
        count[digit] += 1

    # Transforma count em posições finais acumuladas
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Percorre de trás para frente para manter a estabilidade do sort
    for i in range(n - 1, -1, -1):
        digit = (int(array[i]) // exp) % 10
        count[digit] -= 1
        output[count[digit]] = array[i]
        swaps += 1

    return output, swaps
