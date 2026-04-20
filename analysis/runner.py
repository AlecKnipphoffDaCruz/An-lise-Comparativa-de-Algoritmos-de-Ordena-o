import numpy as np

from data.generator import generate
from algorithms import (
    insertion_sort,
    selection_sort,
    shell_sort,
    quick_sort,
    merge_sort,
    radix_sort,
)

# Ordem dos algoritmos no relatório final
ALGORITHMS = {
    "Insertion Sort": insertion_sort,
    "Selection Sort": selection_sort,
    "Shell Sort":     shell_sort,
    "Quick Sort":     quick_sort,
    "Merge Sort":     merge_sort,
    "Radix Sort":     radix_sort,
}

# 3 cenários pedagogicamente distintos: caso médio, melhor e pior caso
SCENARIOS = ["random", "ascending", "descending"]

# Rótulos em português para exibição (consumidos pelo reporter e pelo menu)
SCENARIO_LABELS_PT = {
    "random":     "Aleatório",
    "ascending":  "Crescente",
    "descending": "Decrescente",
}

# Tamanhos de VALIDAÇÃO — propositadamente pequenos para confirmar corretude
# do pipeline e dos algoritmos antes de rodar a análise final.
# Para a rodada final, substituir por:
#     {"small": 1_000, "medium": 10_000, "large": 50_000, "super_large": 100_000}
SIZES = {
    "tiny":   100,
    "small":  500,
    "medium": 1_000,
}

# Número de repetições por combinação — a média suaviza o ruído de time.perf_counter()
RUNS = 3


def run_all() -> dict:
    """
    Executa todos os algoritmos em todos os cenários e tamanhos.

    Para cada (cenário, tamanho), gera UM vetor base e cada algoritmo recebe
    uma cópia desse mesmo vetor — garantindo condições iniciais idênticas.

    Após cada execução, valida que o resultado bate com np.sort(base_array):
    se algum algoritmo estiver errado, o programa quebra imediatamente.

    Retorno:
        results[(algo_name, scenario, size_label)] = {
            "comparisons": float,  # média das RUNS execuções
            "swaps":       float,
            "time":        float,
        }
    """
    results = {}

    for scenario in SCENARIOS:
        for size_label, size in SIZES.items():
            # Gera o vetor UMA vez por combinação — todos os algoritmos recebem o mesmo
            base_array = generate(scenario, size)
            # Resultado esperado para validação de corretude
            expected = np.sort(base_array)

            for algo_name, algo_func in ALGORITHMS.items():
                runs_data = []

                for _ in range(RUNS):
                    # Cada execução recebe uma cópia fresca do vetor base
                    result = algo_func(base_array.copy())

                    # Validação: se o algoritmo falhou, aborta com mensagem clara
                    assert np.array_equal(result["sorted_array"], expected), (
                        f"{algo_name} falhou em ({scenario}, {size_label})"
                    )

                    runs_data.append(result)

                # Média aritmética dos 3 runs — dados brutos são descartados
                results[(algo_name, scenario, size_label)] = {
                    "comparisons": sum(r["comparisons"] for r in runs_data) / RUNS,
                    "swaps":       sum(r["swaps"]       for r in runs_data) / RUNS,
                    "time":        sum(r["time"]        for r in runs_data) / RUNS,
                }

    return results
