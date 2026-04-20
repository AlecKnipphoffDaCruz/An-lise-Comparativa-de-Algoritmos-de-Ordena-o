# Guia do Projeto — Análise Comparativa de Algoritmos de Ordenação

Este guia explica, **sem pressupor conhecimento prévio**, o que este projeto faz, o que cada algoritmo significa, e onde o NumPy entra na história.

---

## 1. Para que serve este projeto?

Queremos responder a uma pergunta antiga da computação: **qual é o "melhor" jeito de colocar uma lista de números em ordem crescente?**

Existem dezenas de maneiras de ordenar. Algumas são simples mas lentas; outras são complicadas mas muito rápidas; algumas são rápidas num tipo de lista mas horríveis em outro. Este projeto implementa 6 algoritmos famosos, roda cada um em 3 tipos de lista e 3 tamanhos diferentes, e gera um relatório com:

- **Tempo** que cada um levou.
- **Quantas comparações** fez (perguntas do tipo "A é maior que B?").
- **Quantas trocas** fez (quantas vezes moveu elementos dentro do vetor).

Com esses 3 números, dá pra comparar os algoritmos objetivamente.

---

## 2. O que significa "ordenar" e "algoritmo de ordenação"?

**Ordenar:** pegar uma sequência de valores fora de ordem (ex.: `[5, 2, 9, 1, 7]`) e rearranjar para ordem crescente (`[1, 2, 5, 7, 9]`).

**Algoritmo de ordenação:** uma receita de passos que transforma o vetor bagunçado no vetor ordenado. Exemplo grosseiro de receita:
1. Olhe cada par de vizinhos.
2. Se o da esquerda for maior, troque.
3. Repita até não precisar mais trocar.

Essa receita funciona (é o "Bubble Sort"), mas é lenta. Os 6 algoritmos aqui são receitas **diferentes** para a mesma tarefa.

---

## 3. Os 6 algoritmos, explicados com analogias

### 3.1 Insertion Sort ("Ordenação por Inserção")

**Analogia:** organizar cartas de baralho na mão. Você recebe uma carta nova, e a encaixa no lugar certo empurrando as outras para a direita.

**Como funciona:** percorre o vetor da esquerda pra direita. Para cada elemento, compara com os anteriores e vai deslocando todos os que forem maiores, até achar a posição correta onde encaixar.

**Quando é bom:** quando a lista já está quase ordenada — nesses casos ele quase não faz trocas.
**Quando é ruim:** quando a lista está em ordem invertida — ele faz o máximo de trabalho possível.

### 3.2 Selection Sort ("Ordenação por Seleção")

**Analogia:** pegar fichas de dominó espalhadas e, a cada rodada, procurar a menor de todas para colocar na pilha.

**Como funciona:** para cada posição `i`, varre **todo** o resto do vetor procurando o menor valor, e troca com o que está em `i`.

**Quando é bom:** nunca é "o melhor", mas faz **pouquíssimas trocas** (no máximo n-1), o que é útil se mover elementos for caro.
**Quando é ruim:** sempre faz o mesmo número de comparações (n²/2), independente do input. Não se beneficia de listas quase ordenadas.

### 3.3 Shell Sort ("Ordenação de Shell")

**Analogia:** imagine o Insertion Sort, mas em vez de comparar só vizinhos imediatos, você primeiro compara elementos bem distantes (ex.: posição 0 com posição 50), para ir "grosseiramente" arrumando a lista. Depois reduz a distância, e no final faz um Insertion Sort normal num vetor que já está bem quase ordenado.

**Como funciona:** usa uma sequência de "saltos" (gaps) — tipicamente n/2, n/4, ..., 2, 1. Para cada salto, faz um Insertion Sort pulando de `gap` em `gap`.

**Quando é bom:** na média é muito melhor que Insertion Sort puro.
**Observação:** sua complexidade exata depende da sequência de gaps usada. É um algoritmo histórico importante.

### 3.4 Quick Sort ("Ordenação Rápida")

**Analogia:** "dividir pra conquistar". Pegue uma pessoa qualquer da fila (o *pivô*), peça pra todos mais baixos que ela irem pra esquerda e mais altos pra direita. Agora resolva cada lado separadamente (recursivamente) e pronto.

**Como funciona:** escolhe um elemento como pivô (nesta implementação: o último do subvetor), reorganiza para que tudo menor fique à esquerda dele e tudo maior à direita, e chama a si mesmo recursivamente nas duas metades.

**Quando é bom:** caso médio — é um dos mais rápidos que existem.
**Quando é ruim:** se o vetor já está ordenado (ou invertido) e o pivô é escolhido nas extremidades, ele degenera para O(n²). Isso aparece nos nossos resultados: Quick Sort tem excelente desempenho em `random`, e péssimo em `ascending`/`descending`.

### 3.5 Merge Sort ("Ordenação por Intercalação")

**Analogia:** dá metade do baralho para um amigo. Cada um ordena sua metade. Depois vocês juntam as duas pilhas ordenadas numa só, sempre olhando o menor de cada pilha e colocando na pilha final.

**Como funciona:** divide o vetor ao meio, ordena cada metade (recursivamente), e depois **intercala** as duas metades já ordenadas.

**Quando é bom:** sempre. É **O(n log n) no pior caso também** — é o mais previsível dos rápidos.
**Preço que paga:** usa **memória extra O(n)** para os vetores temporários da intercalação. Os outros algoritmos ordenam "in-place" (no próprio vetor).

### 3.6 Radix Sort ("Ordenação por Dígitos")

**Analogia:** você tem mil envelopes com números de conta bancária. Primeiro separa em 10 caixas pelo último dígito (0 a 9). Depois junta tudo de volta e separa pelo penúltimo dígito. E assim por diante. No fim, está tudo ordenado.

**Como funciona:** ordena pelo dígito menos significativo (unidade), depois pelas dezenas, depois pelas centenas, e assim por diante. **Não compara elementos entre si** — só olha dígitos.

**Quando é bom:** quando os números têm poucos dígitos e você tem muitos deles. Pode ser mais rápido que todos os outros.
**Limitação:** funciona bem com inteiros não-negativos. Não se adapta bem a strings grandes, números em ponto flutuante, etc.

---

## 4. O que contamos durante a execução?

Três métricas para cada algoritmo:

### 4.1 Comparações
Cada vez que o algoritmo pergunta "este elemento é maior/menor que aquele?", incrementamos o contador. Os 5 algoritmos baseados em comparação (todos menos Radix) fazem isso o tempo inteiro.

**Observação sobre o Radix:** ele sempre aparece com **0 comparações**. Isso é correto e esperado — Radix não olha os valores, só os dígitos individualmente.

### 4.2 Trocas
Quantas vezes o algoritmo move elementos dentro do vetor. Existe uma sutileza:
- Em Insertion, Selection, Shell, Quick: "troca" é a operação clássica de trocar dois elementos de posição.
- Em Merge Sort: contamos cada **escrita** no vetor, já que não há troca clássica — ele copia de vetores auxiliares.
- Em Radix Sort: cada escrita no vetor de saída.

### 4.3 Tempo
Mede quanto tempo real o algoritmo leva. Usamos `time.perf_counter()`, que é o relógio mais preciso do Python para medir intervalos curtos.

**Por que o tempo é "barulhento":** o sistema operacional pode pausar seu programa no meio da execução, a CPU muda de velocidade sozinha, outros processos rodam em paralelo... Tudo isso afeta o tempo medido. Para amenizar, rodamos cada teste **3 vezes** e tiramos a média.

---

## 5. O que é NumPy e onde ele entra?

**NumPy** é a biblioteca padrão do Python para trabalhar com **vetores numéricos** de forma eficiente. Em vez de listas do Python comum (`[1, 2, 3]`), usamos "arrays NumPy" (`np.ndarray`).

### Por que usamos aqui?
1. **Exigência da disciplina** — o padrão da professora pede NumPy.
2. **Geração rápida de vetores de teste** — ex.: `np.arange(1000)` cria `[0, 1, 2, ..., 999]` numa operação só, bem mais rápido que um `for` em Python puro.
3. **Geração de aleatórios reprodutíveis** — `numpy.random.randint(0, 1001, size=1000)` gera 1000 inteiros aleatórios entre 0 e 1000 numa chamada.

### Onde o NumPy aparece no código?
| Local | O que faz |
|-------|-----------|
| `data/generator.py` | Cria os vetores de teste com `np.arange()` e `np.random.randint()`. |
| Todos os `algorithms/*.py` | Os algoritmos recebem um `np.ndarray` e fazem `arr.copy()` para não mexer no original. |
| `analysis/runner.py` | Usa `np.sort()` (que é o próprio sort interno do NumPy, muito rápido) só como **gabarito de validação** — nunca para ordenar os dados que vão ao relatório. |
| `analysis/runner.py` | Usa `np.array_equal()` para comparar o resultado do nosso algoritmo com o gabarito. |

**Importante:** nenhum dos nossos 6 algoritmos usa funcionalidades especiais do NumPy para ordenar — eles ordenam "no braço", elemento por elemento, com `for` e `while`. O NumPy é só o container do vetor e a ferramenta de validação.

---

## 6. Os 3 cenários de teste

Cada cenário testa o algoritmo em uma situação diferente, para revelar onde ele brilha e onde ele sofre.

### Aleatório (`random`)
Vetor com inteiros aleatórios entre 0 e 1000. Representa o **caso médio** — o que você esperaria encontrar na vida real.

### Crescente (`ascending`)
Vetor já em ordem: `[0, 1, 2, ..., n-1]`.
- **Melhor caso** para Insertion Sort (quase nenhum trabalho).
- **Pior caso** para Quick Sort com pivô nas extremidades (a recursão degenera).

### Decrescente (`descending`)
Vetor em ordem invertida: `[n, n-1, ..., 1]`.
- **Pior caso** para Insertion Sort (cada elemento tem que ir até o começo).
- **Também pior caso** para Quick Sort (mesmo problema de pivô).

---

## 7. Por que repetir 3 vezes?

O relógio do computador é sensível. Se eu medir o mesmo código duas vezes seguidas, o tempo vai ser ligeiramente diferente. Rodando 3 vezes e tirando a média, as flutuações se cancelam parcialmente e o número fica mais estável.

Importante: **o vetor é o mesmo nas 3 rodadas**. Não é injusto — todos os algoritmos recebem a mesma entrada para cada (cenário, tamanho).

---

## 8. A validação (`assert`) e por que ela existe

Depois que cada algoritmo termina, o runner compara o resultado com `np.sort(vetor_original)` (o "gabarito correto"). Se estiverem diferentes, o programa **aborta imediatamente** com uma mensagem de erro.

Por quê? Porque o **pior cenário possível** é gerar um relatório bonitinho, com tabelas e números convincentes, mas com **dados errados** porque um dos algoritmos está bugado e ninguém percebeu. O `assert` é a rede de segurança que impede isso.

---

## 9. Como usar o programa

Rode no terminal:

```bash
python main.py
```

Vai aparecer um menu com estas opções:

| Opção | O que faz |
|-------|-----------|
| 1 | Gera o relatório completo em `results/relatorio.md` (todos algoritmos × todos cenários × todos tamanhos). |
| 2 | Roda **um** algoritmo específico em um cenário e tamanho que você escolhe — imprime o resultado no terminal. |
| 3 | Roda **todos os 6** algoritmos em um cenário e tamanho que você escolhe — imprime uma tabela comparativa no terminal. |
| 4 | Exibe este guia. |
| 0 | Sai. |

Nas opções 2 e 3, você escolhe:
- **Qual cenário** (aleatório, crescente, decrescente).
- **Qual tamanho** (100, 500, 1.000, 10.000, ou um número personalizado).

---

## 10. Avisos importantes sobre tamanhos

### Algoritmos O(n²) em tamanhos grandes

**Insertion Sort** e **Selection Sort** têm complexidade O(n²). Traduzindo:
| n | Operações aproximadas | Tempo esperado |
|---|----------------------|----------------|
| 1.000 | 1 milhão | instantâneo |
| 10.000 | 100 milhões | alguns segundos |
| 50.000 | 2,5 bilhões | dezenas de segundos |
| 100.000 | 10 bilhões | muito tempo — minutos |

### Quick Sort em input ordenado

Esta implementação usa o **pivô clássico do Lomuto** (último elemento do subvetor). Esse pivô tem uma fraqueza famosa: em vetores **já ordenados** ou **já invertidos**, a recursão degenera e a profundidade fica O(n). Para `n ≥ 5.000` + cenário `ascending`/`descending`, o Quick Sort pode:
- Fazer O(n²) comparações (muito lento).
- **Estourar a pilha de recursão do Python** e crashear.

No cenário `random`, ele se comporta normalmente e roda rápido até tamanhos bem grandes.

---

## 11. Estrutura dos arquivos

```
trab2/
├── algorithms/           # as 6 implementações
│   ├── __init__.py
│   ├── insertion_sort.py
│   ├── selection_sort.py
│   ├── shell_sort.py
│   ├── quick_sort.py
│   ├── merge_sort.py
│   └── radix_sort.py
├── data/
│   ├── __init__.py
│   └── generator.py      # cria vetores de teste com NumPy
├── analysis/
│   ├── __init__.py
│   ├── runner.py         # orquestra as execuções e valida corretude
│   └── reporter.py       # gera o relatório Markdown
├── results/
│   └── relatorio.md      # saída (gerada pela opção 1 do menu)
├── main.py               # menu interativo — ponto de entrada
├── GUIA.md               # este guia
└── desafio_ordenacao.md  # enunciado original do trabalho
```
