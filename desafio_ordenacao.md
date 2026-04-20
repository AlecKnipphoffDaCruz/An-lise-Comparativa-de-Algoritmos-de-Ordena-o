# Desafio 2 — Análise Comparativa de Algoritmos de Ordenação (Python)

> **Escopo atual:** Passos 1, 2 e 3 — Big-O, implementação dos algoritmos e testes nos 8 cenários.
> Os passos 4 e 5 (análise comparativa, tabelas e gráficos) serão implementados na próxima etapa.

---

## Estrutura do Projeto

```
desafio_ordenacao/
├── algorithms/
│   ├── __init__.py
│   ├── insertion_sort.py
│   ├── quick_sort.py
│   ├── merge_sort.py
│   ├── shell_sort.py
│   ├── selection_sort.py
│   └── radix_sort.py
├── data/
│   └── generator.py          # geração dos vetores com numpy
├── analysis/
│   ├── __init__.py
│   └── runner.py             # executa algoritmos nos cenários (retorna dados estruturados)
├── results/                  # reservado para tabelas e gráficos (próxima etapa)
│   └── .gitkeep
├── main.py                   # entry point
└── README.md
```

> `analysis/` e `results/` já existem na estrutura para que a próxima etapa encaixe naturalmente, sem refatoração.

---

## Dependências

```bash
pip install numpy
```

---

## Passo 1 — Classificação Big-O

Incluir esta tabela no `README.md` do projeto como documentação:

| Algoritmo      | Melhor caso | Caso médio  | Pior caso   | Espaço   |
|----------------|-------------|-------------|-------------|----------|
| Insertion Sort | O(n)        | O(n²)       | O(n²)       | O(1)     |
| Selection Sort | O(n²)       | O(n²)       | O(n²)       | O(1)     |
| Shell Sort     | O(n log n)  | O(n log²n)  | O(n²)       | O(1)     |
| Quick Sort     | O(n log n)  | O(n log n)  | O(n²)       | O(log n) |
| Merge Sort     | O(n log n)  | O(n log n)  | O(n log n)  | O(n)     |
| Radix Sort     | O(nk)       | O(nk)       | O(nk)       | O(n+k)   |

---

## Passo 2 — Implementação dos Algoritmos

### Padrão obrigatório de cada algoritmo

Cada função deve:
- Receber um `np.ndarray`
- Trabalhar sobre uma **cópia** do array (`arr.copy()`) para não modificar o original
- Contar `comparisons` e `swaps` internamente
- Medir o tempo com `time.perf_counter()`
- Retornar um dicionário no formato abaixo

```python
{
    "sorted_array": np.ndarray,
    "comparisons": int,
    "swaps": int,
    "time": float  # segundos
}
```

> Este formato de retorno é o mesmo que o `runner.py` vai consumir, tanto agora quanto na próxima etapa.

### Imports padrão de cada algoritmo

```python
import time
import numpy as np
```

### Exemplo — Insertion Sort (`algorithms/insertion_sort.py`)

```python
import time
import numpy as np

def insertion_sort(arr: np.ndarray) -> dict:
    array = arr.copy()
    comparisons = 0
    swaps = 0

    start = time.perf_counter()

    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            comparisons += 1
            array[j + 1] = array[j]
            swaps += 1
            j -= 1
        comparisons += 1  # comparação que encerrou o while
        array[j + 1] = key

    elapsed = time.perf_counter() - start

    return {
        "sorted_array": array,
        "comparisons": comparisons,
        "swaps": swaps,
        "time": elapsed
    }
```

> Seguir exatamente este mesmo padrão para todos os outros algoritmos.

### `algorithms/__init__.py`

```python
from .insertion_sort import insertion_sort
from .quick_sort import quick_sort
from .merge_sort import merge_sort
from .shell_sort import shell_sort
from .selection_sort import selection_sort
from .radix_sort import radix_sort
```

---

## Passo 3 — Geração dos Vetores e Testes

### `data/generator.py`

Usar **numpy** para gerar todos os vetores, conforme padrão da professora:

```python
import numpy as np
from numpy import random as rd

def generate(scenario: str, size: int) -> np.ndarray:
    """
    Gera um np.ndarray de acordo com o cenário e tamanho informados.

    Cenários disponíveis:
        random_small  — valores aleatórios entre 0 e 1000
        ascending     — vetor em ordem crescente
        descending    — vetor em ordem decrescente
        repeated      — poucos valores distintos (5 possíveis)
        empty         — vetor vazio
        single        — vetor com um único elemento
        many_repeated — muitos valores repetidos (0 a 10)
        long          — valores aleatórios em intervalo grande (0 a 1.000.000)
    """
    match scenario:
        case "random_small":
            return rd.randint(0, 1001, size=size)
        case "ascending":
            return np.arange(size)
        case "descending":
            return np.arange(size, 0, -1)
        case "repeated":
            return rd.randint(1, 6, size=size)
        case "empty":
            return np.array([], dtype=int)
        case "single":
            return np.array([42])
        case "many_repeated":
            return rd.randint(0, 11, size=size)
        case "long":
            return rd.randint(0, 1_000_001, size=size)
        case _:
            raise ValueError(f"Cenário desconhecido: {scenario}")
```

### `analysis/runner.py`

Executa todos os algoritmos em todos os cenários e massas de dados.
Retorna os dados estruturados — prontos para a próxima etapa gerar tabelas e gráficos.

```python
import numpy as np
from data.generator import generate
from algorithms import (
    insertion_sort, quick_sort, merge_sort,
    shell_sort, selection_sort, radix_sort
)

ALGORITHMS = {
    "Insertion Sort": insertion_sort,
    "Quick Sort": quick_sort,
    "Merge Sort": merge_sort,
    "Shell Sort": shell_sort,
    "Selection Sort": selection_sort,
    "Radix Sort": radix_sort,
}

SCENARIOS = [
    "random_small",
    "ascending",
    "descending",
    "repeated",
    "empty",
    "single",
    "many_repeated",
    "long",
]

SIZES = {
    "small":        1_000,
    "medium":      10_000,
    "large":       50_000,
    "super_large": 100_000,
}

RUNS = 3  # casos de teste por cenário (mínimo exigido)


def run_all() -> dict:
    """
    Executa todos os algoritmos em todos os cenários e massas de dados.

    Para cada combinação, roda RUNS vezes sobre o MESMO vetor base
    e calcula a média dos indicadores.

    Retorna um dicionário no formato:
        results[(algo_name, scenario, size_label)] = {
            "comparisons": float,
            "swaps": float,
            "time": float,
            "runs": list  # dados brutos de cada execução (útil na próxima etapa)
        }
    """
    results = {}

    for scenario in SCENARIOS:
        for size_label, size in SIZES.items():

            # Gerar o vetor UMA VEZ — todos os algoritmos recebem o mesmo
            base_array = generate(scenario, size)

            for algo_name, algo_func in ALGORITHMS.items():
                runs_data = []

                for _ in range(RUNS):
                    arr_copy = base_array.copy()  # mesma situação inicial
                    result = algo_func(arr_copy)
                    runs_data.append(result)

                avg = {
                    "comparisons": sum(r["comparisons"] for r in runs_data) / RUNS,
                    "swaps":       sum(r["swaps"]       for r in runs_data) / RUNS,
                    "time":        sum(r["time"]         for r in runs_data) / RUNS,
                    "runs":        runs_data,  # dados brutos preservados para próxima etapa
                }

                results[(algo_name, scenario, size_label)] = avg

    return results
```

### `main.py`

```python
from analysis.runner import run_all, ALGORITHMS, SCENARIOS, SIZES

def main():
    print("Executando análise comparativa...\n")
    results = run_all()

    # Exibição simples no terminal — próxima etapa substitui por gráficos/tabelas
    for scenario in SCENARIOS:
        for size_label in SIZES:
            print(f"\n{'='*60}")
            print(f"Cenário: {scenario:<20} | Massa: {size_label}")
            print(f"{'='*60}")
            print(f"{'Algoritmo':<20} {'Comparações':>14} {'Trocas':>10} {'Tempo (s)':>12}")
            print(f"{'-'*60}")

            for algo_name in ALGORITHMS:
                key = (algo_name, scenario, size_label)
                r = results[key]
                print(
                    f"{algo_name:<20} "
                    f"{r['comparisons']:>14.0f} "
                    f"{r['swaps']:>10.0f} "
                    f"{r['time']:>12.6f}"
                )

if __name__ == "__main__":
    main()
```

---

## Resumo do que será entregue nesta etapa

| Passo | O que fazer | Status |
|-------|-------------|--------|
| 1 | Tabela Big-O de todos os algoritmos no README | ✅ incluir |
| 2 | Implementar os 6 algoritmos instrumentados (comparisons, swaps, time) | ✅ implementar |
| 3 | Gerar vetores com numpy nos 8 cenários e rodar o runner | ✅ implementar |
| 4 | Análise comparativa com tabelas e gráficos | 🔜 próxima etapa |
| 5 | Gráficos e relatório final | 🔜 próxima etapa |

---

## Observações importantes

- **Mesmo vetor para todos:** `base_array` é gerado uma vez e cada algoritmo recebe `base_array.copy()`. Isso garante a mesma situação inicial.
- **Numpy obrigatório:** toda geração de vetores usa `numpy` e `numpy.random`, conforme padrão da professora (`import numpy as np` / `from numpy import random as rd`).
- **Algoritmos operam sobre `np.ndarray`** com indexação padrão (`arr[i]`, `arr[j]`).
- **Dados brutos preservados** em `runs_data` dentro do resultado — a próxima etapa pode usá-los diretamente para gerar gráficos sem re-executar.
- **Comentários no código** são obrigatórios pelo critério de avaliação.
