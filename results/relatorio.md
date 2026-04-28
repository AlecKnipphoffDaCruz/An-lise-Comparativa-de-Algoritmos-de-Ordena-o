# Análise Comparativa de Algoritmos de Ordenação

> **Análise comparativa final** — esta execução utiliza as massas
> 1,000, 10,000, 50,000, 100,000 para comparar os algoritmos nas mesmas condições de
> entrada, com 3 testes por combinação e a média aritmética dos
> resultados.

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
- **Tamanhos de vetor:** small (1000), medium (10000), large (50000), super_large (100000)
- **Repetições por combinação:** 3 (3 testes por algoritmo, com média aritmética)
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

### 3.1 Massa: `small` (1000 elementos)

#### Cenário: Aleatório

| Algoritmo       | Teste | Tempo (s)   | Comparações | Trocas      |
|-----------------|-------|-------------|-------------|-------------|
| Insertion Sort  | 1     |    0.083653 |     255,564 |     254,565 |
| Insertion Sort  | 2     |    0.076477 |     255,564 |     254,565 |
| Insertion Sort  | 3     |    0.072607 |     255,564 |     254,565 |
| **Insertion Sort** | **MÉD** | **  0.077579** | **   255,564** | **   254,565** |
|                 |-------|             |             |             |
| Selection Sort  | 1     |    0.091325 |     499,500 |         994 |
| Selection Sort  | 2     |    0.076850 |     499,500 |         994 |
| Selection Sort  | 3     |    0.072988 |     499,500 |         994 |
| **Selection Sort** | **MÉD** | **  0.080387** | **   499,500** | **       994** |
|                 |-------|             |             |             |
| Shell Sort      | 1     |    0.004060 |      15,728 |       7,722 |
| Shell Sort      | 2     |    0.004011 |      15,728 |       7,722 |
| Shell Sort      | 3     |    0.004014 |      15,728 |       7,722 |
| **Shell Sort    ** | **MÉD** | **  0.004029** | **    15,728** | **     7,722** |
|                 |-------|             |             |             |
| Quick Sort      | 1     |    0.003238 |      10,471 |       4,665 |
| Quick Sort      | 2     |    0.003166 |      10,471 |       4,665 |
| Quick Sort      | 3     |    0.003111 |      10,471 |       4,665 |
| **Quick Sort    ** | **MÉD** | **  0.003172** | **    10,471** | **     4,665** |
|                 |-------|             |             |             |
| Merge Sort      | 1     |    0.005175 |       8,688 |       9,976 |
| Merge Sort      | 2     |    0.005249 |       8,688 |       9,976 |
| Merge Sort      | 3     |    0.005120 |       8,688 |       9,976 |
| **Merge Sort    ** | **MÉD** | **  0.005181** | **     8,688** | **     9,976** |
|                 |-------|             |             |             |
| Radix Sort      | 1     |    0.003385 |           0 |       4,000 |
| Radix Sort      | 2     |    0.003305 |           0 |       4,000 |
| Radix Sort      | 3     |    0.003387 |           0 |       4,000 |
| **Radix Sort    ** | **MÉD** | **  0.003359** | **         0** | **     4,000** |

#### Cenário: Crescente

| Algoritmo       | Teste | Tempo (s)   | Comparações | Trocas      |
|-----------------|-------|-------------|-------------|-------------|
| Insertion Sort  | 1     |    0.000228 |         999 |           0 |
| Insertion Sort  | 2     |    0.000241 |         999 |           0 |
| Insertion Sort  | 3     |    0.000242 |         999 |           0 |
| **Insertion Sort** | **MÉD** | **  0.000237** | **       999** | **         0** |
|                 |-------|             |             |             |
| Selection Sort  | 1     |    0.067150 |     499,500 |           0 |
| Selection Sort  | 2     |    0.067278 |     499,500 |           0 |
| Selection Sort  | 3     |    0.067130 |     499,500 |           0 |
| **Selection Sort** | **MÉD** | **  0.067186** | **   499,500** | **         0** |
|                 |-------|             |             |             |
| Shell Sort      | 1     |    0.001736 |       8,006 |           0 |
| Shell Sort      | 2     |    0.001792 |       8,006 |           0 |
| Shell Sort      | 3     |    0.001780 |       8,006 |           0 |
| **Shell Sort    ** | **MÉD** | **  0.001769** | **     8,006** | **         0** |
|                 |-------|             |             |             |
| Quick Sort      | 1     |    0.068537 |     499,500 |         999 |
| Quick Sort      | 2     |    0.068644 |     499,500 |         999 |
| Quick Sort      | 3     |    0.067332 |     499,500 |         999 |
| **Quick Sort    ** | **MÉD** | **  0.068171** | **   499,500** | **       999** |
|                 |-------|             |             |             |
| Merge Sort      | 1     |    0.004069 |       5,044 |       9,976 |
| Merge Sort      | 2     |    0.004079 |       5,044 |       9,976 |
| Merge Sort      | 3     |    0.004129 |       5,044 |       9,976 |
| **Merge Sort    ** | **MÉD** | **  0.004092** | **     5,044** | **     9,976** |
|                 |-------|             |             |             |
| Radix Sort      | 1     |    0.002333 |           0 |       3,000 |
| Radix Sort      | 2     |    0.002299 |           0 |       3,000 |
| Radix Sort      | 3     |    0.002304 |           0 |       3,000 |
| **Radix Sort    ** | **MÉD** | **  0.002312** | **         0** | **     3,000** |

#### Cenário: Decrescente

| Algoritmo       | Teste | Tempo (s)   | Comparações | Trocas      |
|-----------------|-------|-------------|-------------|-------------|
| Insertion Sort  | 1     |    0.116517 |     500,499 |     499,500 |
| Insertion Sort  | 2     |    0.111602 |     500,499 |     499,500 |
| Insertion Sort  | 3     |    0.111658 |     500,499 |     499,500 |
| **Insertion Sort** | **MÉD** | **  0.113259** | **   500,499** | **   499,500** |
|                 |-------|             |             |             |
| Selection Sort  | 1     |    0.068735 |     499,500 |         500 |
| Selection Sort  | 2     |    0.066305 |     499,500 |         500 |
| Selection Sort  | 3     |    0.068504 |     499,500 |         500 |
| **Selection Sort** | **MÉD** | **  0.067848** | **   499,500** | **       500** |
|                 |-------|             |             |             |
| Shell Sort      | 1     |    0.002909 |      12,706 |       4,700 |
| Shell Sort      | 2     |    0.002825 |      12,706 |       4,700 |
| Shell Sort      | 3     |    0.002805 |      12,706 |       4,700 |
| **Shell Sort    ** | **MÉD** | **  0.002847** | **    12,706** | **     4,700** |
|                 |-------|             |             |             |
| Quick Sort      | 1     |    0.068558 |     499,500 |         999 |
| Quick Sort      | 2     |    0.066676 |     499,500 |         999 |
| Quick Sort      | 3     |    0.066182 |     499,500 |         999 |
| **Quick Sort    ** | **MÉD** | **  0.067139** | **   499,500** | **       999** |
|                 |-------|             |             |             |
| Merge Sort      | 1     |    0.004026 |       4,932 |       9,976 |
| Merge Sort      | 2     |    0.004050 |       4,932 |       9,976 |
| Merge Sort      | 3     |    0.004091 |       4,932 |       9,976 |
| **Merge Sort    ** | **MÉD** | **  0.004056** | **     4,932** | **     9,976** |
|                 |-------|             |             |             |
| Radix Sort      | 1     |    0.003143 |           0 |       4,000 |
| Radix Sort      | 2     |    0.003397 |           0 |       4,000 |
| Radix Sort      | 3     |    0.003070 |           0 |       4,000 |
| **Radix Sort    ** | **MÉD** | **  0.003203** | **         0** | **     4,000** |

### 3.2 Massa: `medium` (10000 elementos)

#### Cenário: Aleatório

| Algoritmo       | Teste | Tempo (s)   | Comparações | Trocas      |
|-----------------|-------|-------------|-------------|-------------|
| Insertion Sort  | 1     |    6.422811 |  25,210,062 |  25,200,063 |
| Insertion Sort  | 2     |    6.751361 |  25,210,062 |  25,200,063 |
| Insertion Sort  | 3     |    6.462548 |  25,210,062 |  25,200,063 |
| **Insertion Sort** | **MÉD** | **  6.545573** | **25,210,062** | **25,200,063** |
|                 |-------|             |             |             |
| Selection Sort  | 1     |    7.237312 |  49,995,000 |       9,984 |
| Selection Sort  | 2     |    7.562248 |  49,995,000 |       9,984 |
| Selection Sort  | 3     |    7.096432 |  49,995,000 |       9,984 |
| **Selection Sort** | **MÉD** | **  7.298664** | **49,995,000** | **     9,984** |
|                 |-------|             |             |             |
| Shell Sort      | 1     |    0.062982 |     250,319 |     130,314 |
| Shell Sort      | 2     |    0.062699 |     250,319 |     130,314 |
| Shell Sort      | 3     |    0.064659 |     250,319 |     130,314 |
| **Shell Sort    ** | **MÉD** | **  0.063446** | **   250,319** | **   130,314** |
|                 |-------|             |             |             |
| Quick Sort      | 1     |    0.048506 |     168,511 |      68,139 |
| Quick Sort      | 2     |    0.056296 |     168,511 |      68,139 |
| Quick Sort      | 3     |    0.052815 |     168,511 |      68,139 |
| **Quick Sort    ** | **MÉD** | **  0.052539** | **   168,511** | **    68,139** |
|                 |-------|             |             |             |
| Merge Sort      | 1     |    0.063100 |     120,562 |     133,616 |
| Merge Sort      | 2     |    0.063426 |     120,562 |     133,616 |
| Merge Sort      | 3     |    0.063016 |     120,562 |     133,616 |
| **Merge Sort    ** | **MÉD** | **  0.063181** | **   120,562** | **   133,616** |
|                 |-------|             |             |             |
| Radix Sort      | 1     |    0.038692 |           0 |      40,000 |
| Radix Sort      | 2     |    0.036013 |           0 |      40,000 |
| Radix Sort      | 3     |    0.031274 |           0 |      40,000 |
| **Radix Sort    ** | **MÉD** | **  0.035327** | **         0** | **    40,000** |

#### Cenário: Crescente

| Algoritmo       | Teste | Tempo (s)   | Comparações | Trocas      |
|-----------------|-------|-------------|-------------|-------------|
| Insertion Sort  | 1     |    0.002389 |       9,999 |           0 |
| Insertion Sort  | 2     |    0.002393 |       9,999 |           0 |
| Insertion Sort  | 3     |    0.002415 |       9,999 |           0 |
| **Insertion Sort** | **MÉD** | **  0.002399** | **     9,999** | **         0** |
|                 |-------|             |             |             |
| Selection Sort  | 1     |    6.883821 |  49,995,000 |           0 |
| Selection Sort  | 2     |    6.839305 |  49,995,000 |           0 |
| Selection Sort  | 3     |    6.871316 |  49,995,000 |           0 |
| **Selection Sort** | **MÉD** | **  6.864814** | **49,995,000** | **         0** |
|                 |-------|             |             |             |
| Shell Sort      | 1     |    0.026461 |     120,005 |           0 |
| Shell Sort      | 2     |    0.026377 |     120,005 |           0 |
| Shell Sort      | 3     |    0.026859 |     120,005 |           0 |
| **Shell Sort    ** | **MÉD** | **  0.026566** | **   120,005** | **         0** |
|                 |-------|             |             |             |
| Quick Sort      | 1     |    7.214578 |  49,995,000 |       9,999 |
| Quick Sort      | 2     |    7.175052 |  49,995,000 |       9,999 |
| Quick Sort      | 3     |    7.175356 |  49,995,000 |       9,999 |
| **Quick Sort    ** | **MÉD** | **  7.188329** | **49,995,000** | **     9,999** |
|                 |-------|             |             |             |
| Merge Sort      | 1     |    0.053398 |      69,008 |     133,616 |
| Merge Sort      | 2     |    0.053360 |      69,008 |     133,616 |
| Merge Sort      | 3     |    0.052514 |      69,008 |     133,616 |
| **Merge Sort    ** | **MÉD** | **  0.053091** | **    69,008** | **   133,616** |
|                 |-------|             |             |             |
| Radix Sort      | 1     |    0.032206 |           0 |      40,000 |
| Radix Sort      | 2     |    0.031720 |           0 |      40,000 |
| Radix Sort      | 3     |    0.032009 |           0 |      40,000 |
| **Radix Sort    ** | **MÉD** | **  0.031979** | **         0** | **    40,000** |

#### Cenário: Decrescente

| Algoritmo       | Teste | Tempo (s)   | Comparações | Trocas      |
|-----------------|-------|-------------|-------------|-------------|
| Insertion Sort  | 1     |   11.966138 |  50,004,999 |  49,995,000 |
| Insertion Sort  | 2     |   11.993005 |  50,004,999 |  49,995,000 |
| Insertion Sort  | 3     |   11.819058 |  50,004,999 |  49,995,000 |
| **Insertion Sort** | **MÉD** | ** 11.926067** | **50,004,999** | **49,995,000** |
|                 |-------|             |             |             |
| Selection Sort  | 1     |    6.886398 |  49,995,000 |       5,000 |
| Selection Sort  | 2     |    6.844613 |  49,995,000 |       5,000 |
| Selection Sort  | 3     |    6.831265 |  49,995,000 |       5,000 |
| **Selection Sort** | **MÉD** | **  6.854092** | **49,995,000** | **     5,000** |
|                 |-------|             |             |             |
| Shell Sort      | 1     |    0.043821 |     182,565 |      62,560 |
| Shell Sort      | 2     |    0.043148 |     182,565 |      62,560 |
| Shell Sort      | 3     |    0.043160 |     182,565 |      62,560 |
| **Shell Sort    ** | **MÉD** | **  0.043376** | **   182,565** | **    62,560** |
|                 |-------|             |             |             |
| Quick Sort      | 1     |    6.853812 |  49,995,000 |       9,999 |
| Quick Sort      | 2     |    6.721646 |  49,995,000 |       9,999 |
| Quick Sort      | 3     |    6.602150 |  49,995,000 |       9,999 |
| **Quick Sort    ** | **MÉD** | **  6.725869** | **49,995,000** | **     9,999** |
|                 |-------|             |             |             |
| Merge Sort      | 1     |    0.051393 |      64,608 |     133,616 |
| Merge Sort      | 2     |    0.051158 |      64,608 |     133,616 |
| Merge Sort      | 3     |    0.050969 |      64,608 |     133,616 |
| **Merge Sort    ** | **MÉD** | **  0.051174** | **    64,608** | **   133,616** |
|                 |-------|             |             |             |
| Radix Sort      | 1     |    0.042851 |           0 |      50,000 |
| Radix Sort      | 2     |    0.041141 |           0 |      50,000 |
| Radix Sort      | 3     |    0.039367 |           0 |      50,000 |
| **Radix Sort    ** | **MÉD** | **  0.041119** | **         0** | **    50,000** |

### 3.3 Massa: `large` (50000 elementos)

#### Cenário: Aleatório

| Algoritmo       | Teste | Tempo (s)   | Comparações | Trocas      |
|-----------------|-------|-------------|-------------|-------------|
| Insertion Sort  | 1     |  157.779193 | 623,914,323 | 623,864,324 |
| Insertion Sort  | 2     |  156.295362 | 623,914,323 | 623,864,324 |
| Insertion Sort  | 3     |  155.426812 | 623,914,323 | 623,864,324 |
| **Insertion Sort** | **MÉD** | **156.500456** | **623,914,323** | **623,864,324** |
|                 |-------|             |             |             |
| Selection Sort  | 1     |  170.572802 | 1,249,975,000 |      49,938 |
| Selection Sort  | 2     |  170.613047 | 1,249,975,000 |      49,938 |
| Selection Sort  | 3     |  170.681220 | 1,249,975,000 |      49,938 |
| **Selection Sort** | **MÉD** | **170.622356** | **1,249,975,000** | **    49,938** |
|                 |-------|             |             |             |
| Shell Sort      | 1     |    0.396325 |   1,634,908 |     934,902 |
| Shell Sort      | 2     |    0.404310 |   1,634,908 |     934,902 |
| Shell Sort      | 3     |    0.407194 |   1,634,908 |     934,902 |
| **Shell Sort    ** | **MÉD** | **  0.402609** | ** 1,634,908** | **   934,902** |
|                 |-------|             |             |             |
| Quick Sort      | 1     |    0.414603 |   1,930,655 |     409,512 |
| Quick Sort      | 2     |    0.396569 |   1,930,655 |     409,512 |
| Quick Sort      | 3     |    0.451456 |   1,930,655 |     409,512 |
| **Quick Sort    ** | **MÉD** | **  0.420876** | ** 1,930,655** | **   409,512** |
|                 |-------|             |             |             |
| Merge Sort      | 1     |    0.388441 |     717,889 |     784,464 |
| Merge Sort      | 2     |    0.369860 |     717,889 |     784,464 |
| Merge Sort      | 3     |    0.374021 |     717,889 |     784,464 |
| **Merge Sort    ** | **MÉD** | **  0.377441** | **   717,889** | **   784,464** |
|                 |-------|             |             |             |
| Radix Sort      | 1     |    0.156941 |           0 |     200,000 |
| Radix Sort      | 2     |    0.156091 |           0 |     200,000 |
| Radix Sort      | 3     |    0.155505 |           0 |     200,000 |
| **Radix Sort    ** | **MÉD** | **  0.156179** | **         0** | **   200,000** |

#### Cenário: Crescente

| Algoritmo       | Teste | Tempo (s)   | Comparações | Trocas      |
|-----------------|-------|-------------|-------------|-------------|
| Insertion Sort  | 1     |    0.012058 |      49,999 |           0 |
| Insertion Sort  | 2     |    0.012389 |      49,999 |           0 |
| Insertion Sort  | 3     |    0.012446 |      49,999 |           0 |
| **Insertion Sort** | **MÉD** | **  0.012298** | **    49,999** | **         0** |
|                 |-------|             |             |             |
| Selection Sort  | 1     |  172.094449 | 1,249,975,000 |           0 |
| Selection Sort  | 2     |  170.067736 | 1,249,975,000 |           0 |
| Selection Sort  | 3     |  171.080947 | 1,249,975,000 |           0 |
| **Selection Sort** | **MÉD** | **171.081044** | **1,249,975,000** | **         0** |
|                 |-------|             |             |             |
| Shell Sort      | 1     |    0.180041 |     700,006 |           0 |
| Shell Sort      | 2     |    0.166127 |     700,006 |           0 |
| Shell Sort      | 3     |    0.160442 |     700,006 |           0 |
| **Shell Sort    ** | **MÉD** | **  0.168870** | **   700,006** | **         0** |
|                 |-------|             |             |             |
| Quick Sort      | 1     |  181.616910 | 1,249,975,000 |      49,999 |
| Quick Sort      | 2     |  183.186023 | 1,249,975,000 |      49,999 |
| Quick Sort      | 3     |  182.962337 | 1,249,975,000 |      49,999 |
| **Quick Sort    ** | **MÉD** | **182.588423** | **1,249,975,000** | **    49,999** |
|                 |-------|             |             |             |
| Merge Sort      | 1     |    0.293898 |     401,952 |     784,464 |
| Merge Sort      | 2     |    0.293133 |     401,952 |     784,464 |
| Merge Sort      | 3     |    0.295070 |     401,952 |     784,464 |
| **Merge Sort    ** | **MÉD** | **  0.294034** | **   401,952** | **   784,464** |
|                 |-------|             |             |             |
| Radix Sort      | 1     |    0.211597 |           0 |     250,000 |
| Radix Sort      | 2     |    0.203729 |           0 |     250,000 |
| Radix Sort      | 3     |    0.196414 |           0 |     250,000 |
| **Radix Sort    ** | **MÉD** | **  0.203914** | **         0** | **   250,000** |

#### Cenário: Decrescente

| Algoritmo       | Teste | Tempo (s)   | Comparações | Trocas      |
|-----------------|-------|-------------|-------------|-------------|
| Insertion Sort  | 1     |  302.892039 | 1,250,024,999 | 1,249,975,000 |
| Insertion Sort  | 2     |  304.983313 | 1,250,024,999 | 1,249,975,000 |
| Insertion Sort  | 3     |  305.979844 | 1,250,024,999 | 1,249,975,000 |
| **Insertion Sort** | **MÉD** | **304.618398** | **1,250,024,999** | **1,249,975,000** |
|                 |-------|             |             |             |
| Selection Sort  | 1     |  173.619764 | 1,249,975,000 |      25,000 |
| Selection Sort  | 2     |  173.428214 | 1,249,975,000 |      25,000 |
| Selection Sort  | 3     |  173.529318 | 1,249,975,000 |      25,000 |
| **Selection Sort** | **MÉD** | **173.525765** | **1,249,975,000** | **    25,000** |
|                 |-------|             |             |             |
| Shell Sort      | 1     |    0.262823 |   1,097,286 |     397,280 |
| Shell Sort      | 2     |    0.255202 |   1,097,286 |     397,280 |
| Shell Sort      | 3     |    0.265519 |   1,097,286 |     397,280 |
| **Shell Sort    ** | **MÉD** | **  0.261181** | ** 1,097,286** | **   397,280** |
|                 |-------|             |             |             |
| Quick Sort      | 1     |  168.209846 | 1,249,975,000 |      49,999 |
| Quick Sort      | 2     |  167.633634 | 1,249,975,000 |      49,999 |
| Quick Sort      | 3     |  167.349579 | 1,249,975,000 |      49,999 |
| **Quick Sort    ** | **MÉD** | **167.731020** | **1,249,975,000** | **    49,999** |
|                 |-------|             |             |             |
| Merge Sort      | 1     |    0.296240 |     382,512 |     784,464 |
| Merge Sort      | 2     |    0.292806 |     382,512 |     784,464 |
| Merge Sort      | 3     |    0.317058 |     382,512 |     784,464 |
| **Merge Sort    ** | **MÉD** | **  0.302035** | **   382,512** | **   784,464** |
|                 |-------|             |             |             |
| Radix Sort      | 1     |    0.207643 |           0 |     250,000 |
| Radix Sort      | 2     |    0.207712 |           0 |     250,000 |
| Radix Sort      | 3     |    0.194890 |           0 |     250,000 |
| **Radix Sort    ** | **MÉD** | **  0.203415** | **         0** | **   250,000** |

### 3.4 Massa: `super_large` (100000 elementos)

#### Cenário: Aleatório

| Algoritmo       | Teste | Tempo (s)   | Comparações | Trocas      |
|-----------------|-------|-------------|-------------|-------------|
| Insertion Sort  | 1     |  609.208754 | 2,486,109,890 | 2,486,009,891 |
| Insertion Sort  | 2     |  615.017842 | 2,486,109,890 | 2,486,009,891 |
| Insertion Sort  | 3     |  629.851317 | 2,486,109,890 | 2,486,009,891 |
| **Insertion Sort** | **MÉD** | **618.025971** | **2,486,109,890** | **2,486,009,891** |
|                 |-------|             |             |             |
| Selection Sort  | 1     |  699.011844 | 4,999,950,000 |      99,884 |
| Selection Sort  | 2     |  698.512448 | 4,999,950,000 |      99,884 |
| Selection Sort  | 3     |  700.542778 | 4,999,950,000 |      99,884 |
| **Selection Sort** | **MÉD** | **699.355690** | **4,999,950,000** | **    99,884** |
|                 |-------|             |             |             |
| Shell Sort      | 1     |    0.902640 |   3,675,534 |   2,175,528 |
| Shell Sort      | 2     |    0.957338 |   3,675,534 |   2,175,528 |
| Shell Sort      | 3     |    0.923920 |   3,675,534 |   2,175,528 |
| **Shell Sort    ** | **MÉD** | **  0.927966** | ** 3,675,534** | ** 2,175,528** |
|                 |-------|             |             |             |
| Quick Sort      | 1     |    1.169122 |   6,373,374 |     812,168 |
| Quick Sort      | 2     |    1.169901 |   6,373,374 |     812,168 |
| Quick Sort      | 3     |    1.231638 |   6,373,374 |     812,168 |
| **Quick Sort    ** | **MÉD** | **  1.190220** | ** 6,373,374** | **   812,168** |
|                 |-------|             |             |             |
| Merge Sort      | 1     |    0.815076 |   1,536,419 |   1,668,928 |
| Merge Sort      | 2     |    0.776619 |   1,536,419 |   1,668,928 |
| Merge Sort      | 3     |    0.817707 |   1,536,419 |   1,668,928 |
| **Merge Sort    ** | **MÉD** | **  0.803134** | ** 1,536,419** | ** 1,668,928** |
|                 |-------|             |             |             |
| Radix Sort      | 1     |    0.316125 |           0 |     400,000 |
| Radix Sort      | 2     |    0.314961 |           0 |     400,000 |
| Radix Sort      | 3     |    0.314211 |           0 |     400,000 |
| **Radix Sort    ** | **MÉD** | **  0.315099** | **         0** | **   400,000** |

#### Cenário: Crescente

| Algoritmo       | Teste | Tempo (s)   | Comparações | Trocas      |
|-----------------|-------|-------------|-------------|-------------|
| Insertion Sort  | 1     |    0.023888 |      99,999 |           0 |
| Insertion Sort  | 2     |    0.023840 |      99,999 |           0 |
| Insertion Sort  | 3     |    0.023916 |      99,999 |           0 |
| **Insertion Sort** | **MÉD** | **  0.023881** | **    99,999** | **         0** |
|                 |-------|             |             |             |
| Selection Sort  | 1     |  708.945489 | 4,999,950,000 |           0 |
| Selection Sort  | 2     |  703.527421 | 4,999,950,000 |           0 |
| Selection Sort  | 3     |  706.540360 | 4,999,950,000 |           0 |
| **Selection Sort** | **MÉD** | **706.337757** | **4,999,950,000** | **         0** |
|                 |-------|             |             |             |
| Shell Sort      | 1     |    0.348284 |   1,500,006 |           0 |
| Shell Sort      | 2     |    0.342949 |   1,500,006 |           0 |
| Shell Sort      | 3     |    0.335506 |   1,500,006 |           0 |
| **Shell Sort    ** | **MÉD** | **  0.342246** | ** 1,500,006** | **         0** |
|                 |-------|             |             |             |
| Quick Sort      | 1     |  766.195323 | 4,999,950,000 |      99,999 |
| Quick Sort      | 2     |  764.395968 | 4,999,950,000 |      99,999 |
| Quick Sort      | 3     |  755.043254 | 4,999,950,000 |      99,999 |
| **Quick Sort    ** | **MÉD** | **761.878182** | **4,999,950,000** | **    99,999** |
|                 |-------|             |             |             |
| Merge Sort      | 1     |    0.640678 |     853,904 |   1,668,928 |
| Merge Sort      | 2     |    0.645314 |     853,904 |   1,668,928 |
| Merge Sort      | 3     |    0.668648 |     853,904 |   1,668,928 |
| **Merge Sort    ** | **MÉD** | **  0.651547** | **   853,904** | ** 1,668,928** |
|                 |-------|             |             |             |
| Radix Sort      | 1     |    0.390840 |           0 |     500,000 |
| Radix Sort      | 2     |    0.387156 |           0 |     500,000 |
| Radix Sort      | 3     |    0.383862 |           0 |     500,000 |
| **Radix Sort    ** | **MÉD** | **  0.387286** | **         0** | **   500,000** |

#### Cenário: Decrescente

| Algoritmo       | Teste | Tempo (s)   | Comparações | Trocas      |
|-----------------|-------|-------------|-------------|-------------|
| Insertion Sort  | 1     | 1293.310082 | 5,000,049,999 | 4,999,950,000 |
| Insertion Sort  | 2     | 1232.953465 | 5,000,049,999 | 4,999,950,000 |
| Insertion Sort  | 3     | 1229.486393 | 5,000,049,999 | 4,999,950,000 |
| **Insertion Sort** | **MÉD** | **1251.916647** | **5,000,049,999** | **4,999,950,000** |
|                 |-------|             |             |             |
| Selection Sort  | 1     |  705.702914 | 4,999,950,000 |      50,000 |
| Selection Sort  | 2     |  710.730472 | 4,999,950,000 |      50,000 |
| Selection Sort  | 3     |  713.502682 | 4,999,950,000 |      50,000 |
| **Selection Sort** | **MÉD** | **709.978689** | **4,999,950,000** | **    50,000** |
|                 |-------|             |             |             |
| Shell Sort      | 1     |    0.588855 |   2,344,566 |     844,560 |
| Shell Sort      | 2     |    0.587679 |   2,344,566 |     844,560 |
| Shell Sort      | 3     |    0.560493 |   2,344,566 |     844,560 |
| **Shell Sort    ** | **MÉD** | **  0.579009** | ** 2,344,566** | **   844,560** |
|                 |-------|             |             |             |
| Quick Sort      | 1     |  701.560537 | 4,999,950,000 |      99,999 |
| Quick Sort      | 2     |  642.203479 | 4,999,950,000 |      99,999 |
| Quick Sort      | 3     |  546.905461 | 4,999,950,000 |      99,999 |
| **Quick Sort    ** | **MÉD** | **630.223159** | **4,999,950,000** | **    99,999** |
|                 |-------|             |             |             |
| Merge Sort      | 1     |    0.498245 |     815,024 |   1,668,928 |
| Merge Sort      | 2     |    0.471883 |     815,024 |   1,668,928 |
| Merge Sort      | 3     |    0.490120 |     815,024 |   1,668,928 |
| **Merge Sort    ** | **MÉD** | **  0.486749** | **   815,024** | ** 1,668,928** |
|                 |-------|             |             |             |
| Radix Sort      | 1     |    0.384094 |           0 |     600,000 |
| Radix Sort      | 2     |    0.359960 |           0 |     600,000 |
| Radix Sort      | 3     |    0.369083 |           0 |     600,000 |
| **Radix Sort    ** | **MÉD** | **  0.371046** | **         0** | **   600,000** |

## 4. Conclusões

Esta é a execução comparativa final. O objetivo aqui é verificar
como cada algoritmo se comporta em cenários e massas diferentes:

1. Todos os algoritmos produzem saídas ordenadas corretamente
   (garantido pelo `assert` no runner).
2. Os contadores de comparações, trocas e tempos refletem o
   comportamento esperado de cada algoritmo em cada cenário.
3. O pipeline de geração de relatório funciona ponta a ponta.

As conclusões comparativas completas devem ser interpretadas a partir
das tabelas acima, observando tempo, comparações e trocas em cada
cenário e massa de dados.
