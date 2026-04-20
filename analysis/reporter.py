from pathlib import Path

from analysis.runner import (
    ALGORITHMS,
    SCENARIOS,
    SCENARIO_LABELS_PT,
    SIZES,
    RUNS,
)


# Tabela de complexidade (Passo 1) — fixa, retirada do spec
BIG_O_TABLE = """\
| Algoritmo      | Melhor caso | Caso médio  | Pior caso   | Espaço   |
|----------------|-------------|-------------|-------------|----------|
| Insertion Sort | O(n)        | O(n²)       | O(n²)       | O(1)     |
| Selection Sort | O(n²)       | O(n²)       | O(n²)       | O(1)     |
| Shell Sort     | O(n log n)  | O(n log²n)  | O(n²)       | O(1)     |
| Quick Sort     | O(n log n)  | O(n log n)  | O(n²)       | O(log n) |
| Merge Sort     | O(n log n)  | O(n log n)  | O(n log n)  | O(n)     |
| Radix Sort     | O(nk)       | O(nk)       | O(nk)       | O(n+k)   |
"""


def write_report(results: dict, output_path: str = "results/relatorio.md") -> Path:
    """
    Gera o relatório de comparação em Markdown a partir do dicionário do runner.
    Retorna o Path do arquivo escrito.
    """
    lines: list[str] = []

    # Cabeçalho
    lines.append("# Análise Comparativa de Algoritmos de Ordenação")
    lines.append("")

    # Banner destacando que esta é uma rodada de VALIDAÇÃO
    sizes_str = ", ".join(str(s) for s in SIZES.values())
    lines.append("> **⚠️ Rodada de validação** — esta execução utiliza massas reduzidas")
    lines.append(f"> ({sizes_str}) apenas para confirmar a correção dos algoritmos e do")
    lines.append("> pipeline de relatório. A análise final com massas de produção")
    lines.append("> (10k / 50k / 100k) será produzida em uma execução separada,")
    lines.append("> substituindo os valores em `SIZES` no `analysis/runner.py`.")
    lines.append("")

    # Seção 1 — Complexidade
    lines.append("## 1. Complexidade (Big-O)")
    lines.append("")
    lines.append(BIG_O_TABLE)

    # Seção 2 — Metodologia
    lines.append("## 2. Metodologia")
    lines.append("")
    scenarios_pt = ", ".join(SCENARIO_LABELS_PT[s] for s in SCENARIOS)
    sizes_desc = ", ".join(f"{k} ({v})" for k, v in SIZES.items())
    lines.append(f"- **Cenários testados:** {scenarios_pt}")
    lines.append(f"- **Tamanhos de vetor:** {sizes_desc}")
    lines.append(f"- **Repetições por combinação:** {RUNS} (média aritmética)")
    lines.append("- **Geração de vetores:** NumPy — o mesmo vetor base é passado")
    lines.append("  (via `.copy()`) para todos os algoritmos em cada combinação,")
    lines.append("  garantindo condições iniciais idênticas.")
    lines.append("- **Instrumentação:** cada algoritmo conta `comparisons` e `swaps`")
    lines.append("  internamente; o tempo é medido com `time.perf_counter()`.")
    lines.append("- **Validação de corretude:** após cada execução, o resultado é")
    lines.append("  comparado com `np.sort(base_array)` — se algum algoritmo falhar,")
    lines.append("  o programa aborta com erro em vez de gerar dados falsos.")
    lines.append("")

    # Notas de interpretação dos contadores
    lines.append("### Observações sobre os contadores")
    lines.append("")
    lines.append("- **Merge Sort:** não possui \"trocas\" tradicionais — o contador")
    lines.append("  registra cada **escrita** no vetor durante a intercalação.")
    lines.append("- **Radix Sort:** não faz comparações entre elementos (ordena por")
    lines.append("  dígito), portanto `comparações = 0` é esperado. O contador de")
    lines.append("  \"trocas\" registra as escritas no vetor de saída.")
    lines.append("")

    # Seção 3 — Resultados
    lines.append("## 3. Resultados")
    lines.append("")

    size_labels = list(SIZES)
    for size_idx, size_label in enumerate(size_labels, start=1):
        size = SIZES[size_label]
        lines.append(f"### 3.{size_idx} Massa: `{size_label}` ({size} elementos)")
        lines.append("")

        for scenario in SCENARIOS:
            lines.append(f"#### Cenário: {SCENARIO_LABELS_PT[scenario]}")
            lines.append("")
            lines.append("| Algoritmo       | Tempo (s)   | Comparações | Trocas      |")
            lines.append("|-----------------|-------------|-------------|-------------|")
            for algo_name in ALGORITHMS:
                r = results[(algo_name, scenario, size_label)]
                lines.append(
                    f"| {algo_name:<15} "
                    f"| {r['time']:>11.6f} "
                    f"| {r['comparisons']:>11,.0f} "
                    f"| {r['swaps']:>11,.0f} |"
                )
            lines.append("")

    # Seção 4 — Conclusões (placeholder até rodada final)
    lines.append("## 4. Conclusões")
    lines.append("")
    lines.append("Esta é uma **rodada de validação**. O objetivo aqui é apenas")
    lines.append("confirmar que:")
    lines.append("")
    lines.append("1. Todos os algoritmos produzem saídas ordenadas corretamente")
    lines.append("   (garantido pelo `assert` no runner).")
    lines.append("2. Os contadores de comparações e trocas estão coerentes com o")
    lines.append("   esperado teórico (ex.: Insertion Sort em vetor crescente deve")
    lines.append("   ter ~0 trocas; Selection Sort deve ter sempre O(n²) comparações).")
    lines.append("3. O pipeline de geração de relatório funciona ponta a ponta.")
    lines.append("")
    lines.append("As conclusões comparativas completas (qual algoritmo é mais rápido")
    lines.append("em cada cenário, como a diferença escala com o tamanho, etc.) serão")
    lines.append("escritas após a execução com massas de produção.")
    lines.append("")

    # Escreve o arquivo (cria results/ se não existir)
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")
    return path
