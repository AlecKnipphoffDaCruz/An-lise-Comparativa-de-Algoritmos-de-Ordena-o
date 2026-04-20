# Análise Comparativa de Algoritmos de Ordenação

> **⚠️ Rodada de validação** — esta execução utiliza massas reduzidas
> (100, 500, 1000) apenas para confirmar a correção dos algoritmos e do
> pipeline de relatório. A análise final com massas de produção
> (10k / 50k / 100k) será produzida em uma execução separada,
> substituindo os valores em `SIZES` no `analysis/runner.py`.

## 1. Complexidade (Big-O)

| Algoritmo      | Melhor caso | Caso médio  | Pior caso   | Espaço   |
|----------------|-------------|-------------|-------------|----------|
| Insertion Sort | O(n)        | O(n²)       | O(n²)       | O(1)     |
| Selection Sort | O(n²)       | O(n²)       | O(n²)       | O(1)     |
| Shell Sort     | O(n log n)  | O(n log²n)  | O(n²)       | O(1)     |
| Quick Sort     | O(n log n)  | O(n log n)  | O(n²)       | O(log n) |
| Merge Sort     | O(n log n)  | O(n log n)  | O(n log n)  | O(n)     |
| Radix Sort     | O(nk)       | O(nk)       | O(nk)       | O(n+k)   |

## 2. Metodologia

- **Cenários testados:** Aleatório, Crescente, Decrescente
- **Tamanhos de vetor:** tiny (100), small (500), medium (1000)
- **Repetições por combinação:** 3 (média aritmética)
- **Geração de vetores:** NumPy — o mesmo vetor base é passado
  (via `.copy()`) para todos os algoritmos em cada combinação,
  garantindo condições iniciais idênticas.
- **Instrumentação:** cada algoritmo conta `comparisons` e `swaps`
  internamente; o tempo é medido com `time.perf_counter()`.
- **Validação de corretude:** após cada execução, o resultado é
  comparado com `np.sort(base_array)` — se algum algoritmo falhar,
  o programa aborta com erro em vez de gerar dados falsos.

### Observações sobre os contadores

- **Merge Sort:** não possui "trocas" tradicionais — o contador
  registra cada **escrita** no vetor durante a intercalação.
- **Radix Sort:** não faz comparações entre elementos (ordena por 
  dígito), portanto `comparações = 0` é esperado. O contador de
  "trocas" registra as escritas no vetor de saída.

## 3. Resultados

### 3.1 Massa: `tiny` (100 elementos)

#### Cenário: Aleatório

| Algoritmo       | Tempo (s)   | Comparações | Trocas      |
|-----------------|-------------|-------------|-------------|
| Insertion Sort  |    0.000707 |       2,646 |       2,547 |
| Selection Sort  |    0.000822 |       4,950 |          93 |
| Shell Sort      |    0.000265 |         986 |         483 |
| Quick Sort      |    0.000206 |         614 |         290 |
| Merge Sort      |    0.000399 |         548 |         672 |
| Radix Sort      |    0.000262 |           0 |         300 |

#### Cenário: Crescente

| Algoritmo       | Tempo (s)   | Comparações | Trocas      |
|-----------------|-------------|-------------|-------------|
| Insertion Sort  |    0.000034 |          99 |           0 |
| Selection Sort  |    0.000858 |       4,950 |           0 |
| Shell Sort      |    0.000132 |         503 |           0 |
| Quick Sort      |    0.000839 |       4,950 |          99 |
| Merge Sort      |    0.000343 |         356 |         672 |
| Radix Sort      |    0.000178 |           0 |         200 |

#### Cenário: Decrescente

| Algoritmo       | Tempo (s)   | Comparações | Trocas      |
|-----------------|-------------|-------------|-------------|
| Insertion Sort  |    0.001634 |       5,049 |       4,950 |
| Selection Sort  |    0.001020 |       4,950 |          50 |
| Shell Sort      |    0.000238 |         763 |         260 |
| Quick Sort      |    0.000935 |       4,950 |          99 |
| Merge Sort      |    0.000393 |         316 |         672 |
| Radix Sort      |    0.000297 |           0 |         300 |

### 3.2 Massa: `small` (500 elementos)

#### Cenário: Aleatório

| Algoritmo       | Tempo (s)   | Comparações | Trocas      |
|-----------------|-------------|-------------|-------------|
| Insertion Sort  |    0.018149 |      61,161 |      60,662 |
| Selection Sort  |    0.025558 |     124,750 |         491 |
| Shell Sort      |    0.002212 |       6,724 |       3,218 |
| Quick Sort      |    0.001969 |       4,738 |       2,448 |
| Merge Sort      |    0.002872 |       3,850 |       4,488 |
| Radix Sort      |    0.001466 |           0 |       1,500 |

#### Cenário: Crescente

| Algoritmo       | Tempo (s)   | Comparações | Trocas      |
|-----------------|-------------|-------------|-------------|
| Insertion Sort  |    0.000147 |         499 |           0 |
| Selection Sort  |    0.021541 |     124,750 |           0 |
| Shell Sort      |    0.000970 |       3,506 |           0 |
| Quick Sort      |    0.020934 |     124,750 |         499 |
| Merge Sort      |    0.002220 |       2,272 |       4,488 |
| Radix Sort      |    0.001313 |           0 |       1,500 |

#### Cenário: Decrescente

| Algoritmo       | Tempo (s)   | Comparações | Trocas      |
|-----------------|-------------|-------------|-------------|
| Insertion Sort  |    0.038379 |     125,249 |     124,750 |
| Selection Sort  |    0.022695 |     124,750 |         250 |
| Shell Sort      |    0.001853 |       5,606 |       2,100 |
| Quick Sort      |    0.022792 |     124,750 |         499 |
| Merge Sort      |    0.002782 |       2,216 |       4,488 |
| Radix Sort      |    0.001466 |           0 |       1,500 |

### 3.3 Massa: `medium` (1000 elementos)

#### Cenário: Aleatório

| Algoritmo       | Tempo (s)   | Comparações | Trocas      |
|-----------------|-------------|-------------|-------------|
| Insertion Sort  |    0.080400 |     248,101 |     247,102 |
| Selection Sort  |    0.103999 |     499,500 |         990 |
| Shell Sort      |    0.005088 |      15,075 |       7,069 |
| Quick Sort      |    0.004140 |      11,292 |       5,881 |
| Merge Sort      |    0.005704 |       8,703 |       9,976 |
| Radix Sort      |    0.003473 |           0 |       4,000 |

#### Cenário: Crescente

| Algoritmo       | Tempo (s)   | Comparações | Trocas      |
|-----------------|-------------|-------------|-------------|
| Insertion Sort  |    0.000305 |         999 |           0 |
| Selection Sort  |    0.088975 |     499,500 |           0 |
| Shell Sort      |    0.002285 |       8,006 |           0 |
| Quick Sort      |    0.083378 |     499,500 |         999 |
| Merge Sort      |    0.005484 |       5,044 |       9,976 |
| Radix Sort      |    0.002987 |           0 |       3,000 |

#### Cenário: Decrescente

| Algoritmo       | Tempo (s)   | Comparações | Trocas      |
|-----------------|-------------|-------------|-------------|
| Insertion Sort  |    0.151475 |     500,499 |     499,500 |
| Selection Sort  |    0.091021 |     499,500 |         500 |
| Shell Sort      |    0.003802 |      12,706 |       4,700 |
| Quick Sort      |    0.086687 |     499,500 |         999 |
| Merge Sort      |    0.005593 |       4,932 |       9,976 |
| Radix Sort      |    0.004016 |           0 |       4,000 |

## 4. Conclusões

Esta é uma **rodada de validação**. O objetivo aqui é apenas
confirmar que:

1. Todos os algoritmos produzem saídas ordenadas corretamente
   (garantido pelo `assert` no runner).
2. Os contadores de comparações e trocas estão coerentes com o
   esperado teórico (ex.: Insertion Sort em vetor crescente deve
   ter ~0 trocas; Selection Sort deve ter sempre O(n²) comparações).
3. O pipeline de geração de relatório funciona ponta a ponta.

As conclusões comparativas completas (qual algoritmo é mais rápido
em cada cenário, como a diferença escala com o tamanho, etc.) serão
escritas após a execução com massas de produção.
