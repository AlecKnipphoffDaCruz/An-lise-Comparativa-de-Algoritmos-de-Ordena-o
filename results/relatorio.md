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
| Insertion Sort  |    0.000806 |       2,340 |       2,241 |
| Selection Sort  |    0.000857 |       4,950 |          93 |
| Shell Sort      |    0.000290 |         931 |         428 |
| Quick Sort      |    0.000262 |         632 |         338 |
| Merge Sort      |    0.000477 |         530 |         672 |
| Radix Sort      |    0.000330 |           0 |         300 |

#### Cenário: Crescente

| Algoritmo       | Tempo (s)   | Comparações | Trocas      |
|-----------------|-------------|-------------|-------------|
| Insertion Sort  |    0.000012 |          99 |           0 |
| Selection Sort  |    0.000353 |       4,950 |           0 |
| Shell Sort      |    0.000054 |         503 |           0 |
| Quick Sort      |    0.000413 |       4,950 |          99 |
| Merge Sort      |    0.000160 |         356 |         672 |
| Radix Sort      |    0.000077 |           0 |         200 |

#### Cenário: Decrescente

| Algoritmo       | Tempo (s)   | Comparações | Trocas      |
|-----------------|-------------|-------------|-------------|
| Insertion Sort  |    0.000680 |       5,049 |       4,950 |
| Selection Sort  |    0.000372 |       4,950 |          50 |
| Shell Sort      |    0.000087 |         763 |         260 |
| Quick Sort      |    0.000368 |       4,950 |          99 |
| Merge Sort      |    0.000156 |         316 |         672 |
| Radix Sort      |    0.000111 |           0 |         300 |

### 3.2 Massa: `small` (500 elementos)

#### Cenário: Aleatório

| Algoritmo       | Tempo (s)   | Comparações | Trocas      |
|-----------------|-------------|-------------|-------------|
| Insertion Sort  |    0.014307 |      61,430 |      60,931 |
| Selection Sort  |    0.011057 |     124,750 |         493 |
| Shell Sort      |    0.000873 |       6,406 |       2,900 |
| Quick Sort      |    0.000869 |       5,228 |       2,364 |
| Merge Sort      |    0.001374 |       3,872 |       4,488 |
| Radix Sort      |    0.000571 |           0 |       1,500 |

#### Cenário: Crescente

| Algoritmo       | Tempo (s)   | Comparações | Trocas      |
|-----------------|-------------|-------------|-------------|
| Insertion Sort  |    0.000067 |         499 |           0 |
| Selection Sort  |    0.008740 |     124,750 |           0 |
| Shell Sort      |    0.000416 |       3,506 |           0 |
| Quick Sort      |    0.009152 |     124,750 |         499 |
| Merge Sort      |    0.000981 |       2,272 |       4,488 |
| Radix Sort      |    0.000547 |           0 |       1,500 |

#### Cenário: Decrescente

| Algoritmo       | Tempo (s)   | Comparações | Trocas      |
|-----------------|-------------|-------------|-------------|
| Insertion Sort  |    0.015281 |     125,249 |     124,750 |
| Selection Sort  |    0.009286 |     124,750 |         250 |
| Shell Sort      |    0.000626 |       5,606 |       2,100 |
| Quick Sort      |    0.008165 |     124,750 |         499 |
| Merge Sort      |    0.000982 |       2,216 |       4,488 |
| Radix Sort      |    0.000571 |           0 |       1,500 |

### 3.3 Massa: `medium` (1000 elementos)

#### Cenário: Aleatório

| Algoritmo       | Tempo (s)   | Comparações | Trocas      |
|-----------------|-------------|-------------|-------------|
| Insertion Sort  |    0.032499 |     251,916 |     250,917 |
| Selection Sort  |    0.037203 |     499,500 |         993 |
| Shell Sort      |    0.001848 |      15,172 |       7,166 |
| Quick Sort      |    0.001598 |      10,328 |       5,080 |
| Merge Sort      |    0.002680 |       8,747 |       9,976 |
| Radix Sort      |    0.001142 |           0 |       3,000 |

#### Cenário: Crescente

| Algoritmo       | Tempo (s)   | Comparações | Trocas      |
|-----------------|-------------|-------------|-------------|
| Insertion Sort  |    0.000126 |         999 |           0 |
| Selection Sort  |    0.035913 |     499,500 |           0 |
| Shell Sort      |    0.000872 |       8,006 |           0 |
| Quick Sort      |    0.036176 |     499,500 |         999 |
| Merge Sort      |    0.002136 |       5,044 |       9,976 |
| Radix Sort      |    0.001140 |           0 |       3,000 |

#### Cenário: Decrescente

| Algoritmo       | Tempo (s)   | Comparações | Trocas      |
|-----------------|-------------|-------------|-------------|
| Insertion Sort  |    0.064051 |     500,499 |     499,500 |
| Selection Sort  |    0.036500 |     499,500 |         500 |
| Shell Sort      |    0.001453 |      12,706 |       4,700 |
| Quick Sort      |    0.033868 |     499,500 |         999 |
| Merge Sort      |    0.002093 |       4,932 |       9,976 |
| Radix Sort      |    0.001398 |           0 |       4,000 |

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
