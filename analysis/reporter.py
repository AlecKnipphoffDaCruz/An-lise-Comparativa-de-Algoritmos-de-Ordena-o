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

    # Banner da análise comparativa final
    sizes_str = ", ".join(f"{v:,}" for v in SIZES.values())
    lines.append("> **Análise comparativa final** — esta execução utiliza as massas")
    lines.append(f"> {sizes_str} para comparar os algoritmos nas mesmas condições de")
    lines.append("> entrada, com 3 testes por combinação e a média aritmética dos")
    lines.append("> resultados.")
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
    lines.append(f"- **Repetições por combinação:** {RUNS} (3 testes por algoritmo, com média aritmética)")
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
            lines.append("| Algoritmo       | Teste | Tempo (s)   | Comparações | Trocas      |")
            lines.append("|-----------------|-------|-------------|-------------|-------------|")
            
            for algo_name in ALGORITHMS:
                r = results[(algo_name, scenario, size_label)]
                runs = r["runs"]
                avg = r["average"]
                
                # Exibe cada um dos 3 testes
                for test_num, test_data in enumerate(runs, start=1):
                    lines.append(
                        f"| {algo_name:<15} "
                        f"| {test_num}     "
                        f"| {test_data['time']:>11.6f} "
                        f"| {test_data['comparisons']:>11,.0f} "
                        f"| {test_data['swaps']:>11,.0f} |"
                    )
                
                # Exibe a linha de MÉDIA em negrito
                lines.append(
                    f"| **{algo_name:<14}** "
                    f"| **MÉD** "
                    f"| **{avg['time']:>10.6f}** "
                    f"| **{avg['comparisons']:>10,.0f}** "
                    f"| **{avg['swaps']:>10,.0f}** |"
                )
                lines.append("|                 |-------|             |             |             |")
            
            # Remove a última linha de separador desnecessária
            lines.pop()
            lines.append("")

    # Seção 4 — Conclusões (placeholder até rodada final)
    lines.append("## 4. Conclusões")
    lines.append("")
    lines.append("Esta é a execução comparativa final. O objetivo aqui é verificar")
    lines.append("como cada algoritmo se comporta em cenários e massas diferentes:")
    lines.append("")
    lines.append("1. Todos os algoritmos produzem saídas ordenadas corretamente")
    lines.append("   (garantido pelo `assert` no runner).")
    lines.append("2. Os contadores de comparações, trocas e tempos refletem o")
    lines.append("   comportamento esperado de cada algoritmo em cada cenário.")
    lines.append("3. O pipeline de geração de relatório funciona ponta a ponta.")
    lines.append("")
    lines.append("As conclusões comparativas completas devem ser interpretadas a partir")
    lines.append("das tabelas acima, observando tempo, comparações e trocas em cada")
    lines.append("cenário e massa de dados.")
    lines.append("")

    # Escreve o arquivo (cria results/ se não existir)
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")
    return path
