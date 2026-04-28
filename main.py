import sys
from pathlib import Path

import numpy as np

from data.generator import generate
from analysis.runner import (
    ALGORITHMS,
    SCENARIOS,
    SCENARIO_LABELS_PT,
    SIZES,
    run_all,
)
from analysis.reporter import write_report


# Tamanhos oferecidos no menu — cobrem desde validação rápida até "massas de produção"
MENU_SIZES = {
    "1": ("tiny",        100),
    "2": ("small",       500),
    "3": ("medium",    1_000),
    "4": ("large",    10_000),
    "5": ("super",    50_000),
}

# Número de execuções para as opções interativas (não-relatório).
# Mantido igual ao runner — média das 3 execuções suaviza ruído de cronômetro.
INTERACTIVE_RUNS = 3


# -------------------- utilitários de entrada --------------------

def _prompt(msg: str) -> str:
    # Envolve input() com strip para tolerar espaços acidentais
    return input(msg).strip()


def _escolher_cenario() -> str:
    print()
    print("Escolha o cenário:")
    for idx, key in enumerate(SCENARIOS, start=1):
        print(f"  {idx}. {SCENARIO_LABELS_PT[key]}")
    while True:
        escolha = _prompt("Opção: ")
        if escolha.isdigit() and 1 <= int(escolha) <= len(SCENARIOS):
            return SCENARIOS[int(escolha) - 1]
        print("Opção inválida.")


def _escolher_tamanho() -> int:
    print()
    print("Escolha o tamanho do vetor:")
    for key, (label, size) in MENU_SIZES.items():
        print(f"  {key}. {label:<6} ({size:>6,} elementos)")
    print("  6. personalizado")
    while True:
        escolha = _prompt("Opção: ")
        if escolha in MENU_SIZES:
            return MENU_SIZES[escolha][1]
        if escolha == "6":
            valor = _prompt("Digite o tamanho (inteiro positivo): ")
            if valor.isdigit() and int(valor) > 0:
                return int(valor)
            print("Valor inválido.")
            continue
        print("Opção inválida.")


def _escolher_algoritmo() -> tuple[str, callable]:
    print()
    print("Escolha o algoritmo:")
    nomes = list(ALGORITHMS.keys())
    for idx, nome in enumerate(nomes, start=1):
        print(f"  {idx}. {nome}")
    while True:
        escolha = _prompt("Opção: ")
        if escolha.isdigit() and 1 <= int(escolha) <= len(nomes):
            nome = nomes[int(escolha) - 1]
            return nome, ALGORITHMS[nome]
        print("Opção inválida.")


# -------------------- execução e impressão --------------------

def _avisar_algoritmos_lentos(algo_name: str, scenario: str, size: int) -> bool:
    """
    Avisa o usuário se a combinação tende a ser muito lenta ou perigosa.
    Retorna False se o usuário decidir abortar.
    """
    # Insertion/Selection são O(n²) — ficam pesados a partir de ~10k
    if algo_name in ("Insertion Sort", "Selection Sort") and size >= 10_000:
        print(f"\nAVISO: {algo_name} é O(n²). Com n={size:,} pode demorar bastante.")
        return _prompt("Continuar mesmo assim? (s/n): ").lower().startswith("s")

    # Quick Sort com pivô Lomuto degenera em input ordenado/invertido
    if algo_name == "Quick Sort" and scenario in ("ascending", "descending") and size >= 5_000:
        print(f"\nAVISO: Quick Sort com pivô Lomuto em vetor {scenario} pode")
        print(f"degenerar para O(n²) e até estourar a pilha. n={size:,}.")
        return _prompt("Continuar mesmo assim? (s/n): ").lower().startswith("s")

    return True


def _executar_e_medir(algo_func, base_array: np.ndarray, runs: int) -> dict:
    """
    Executa o algoritmo 'runs' vezes sobre cópias do mesmo vetor base
    e retorna a média de comparações/trocas/tempo.
    Valida a corretude contra np.sort antes de aceitar o resultado.
    """
    expected = np.sort(base_array)
    runs_data = []

    for _ in range(runs):
        result = algo_func(base_array.copy())
        if not np.array_equal(result["sorted_array"], expected):
            raise AssertionError("Resultado incorreto — ordenação falhou.")
        runs_data.append(result)

    return {
        "comparisons": sum(r["comparisons"] for r in runs_data) / runs,
        "swaps":       sum(r["swaps"]       for r in runs_data) / runs,
        "time":        sum(r["time"]        for r in runs_data) / runs,
    }


def _imprimir_linha_resultado(nome: str, metrics: dict) -> None:
    print(
        f"| {nome:<15} "
        f"| {metrics['time']:>11.6f} "
        f"| {metrics['comparisons']:>13,.0f} "
        f"| {metrics['swaps']:>11,.0f} |"
    )


def _imprimir_cabecalho_tabela() -> None:
    print("| Algoritmo       | Tempo (s)   | Comparações   | Trocas      |")
    print("|-----------------|-------------|---------------|-------------|")


def _formatar_barra_progresso(atual: int, total: int, largura: int = 24) -> str:
    preenchimento = int(largura * atual / total)
    barra = "#" * preenchimento + "-" * (largura - preenchimento)
    return f"[{barra}] {atual}/{total}"


def _mostrar_progresso(atual: int, total: int, algo_name: str, scenario: str, size_label: str, pacote: dict) -> None:
    size = SIZES[size_label]
    print()
    print(f"{_formatar_barra_progresso(atual, total)} {algo_name} | {SCENARIO_LABELS_PT[scenario]} | {size:,} elementos")
    for idx, teste in enumerate(pacote["runs"], start=1):
        print(
            f"  Teste {idx}: "
            f"tempo={teste['time']:.6f}s, "
            f"comparações={teste['comparisons']:,.0f}, "
            f"trocas={teste['swaps']:,.0f}"
        )
    media = pacote["average"]
    print(
        f"  Média: tempo={media['time']:.6f}s, "
        f"comparações={media['comparisons']:,.0f}, "
        f"trocas={media['swaps']:,.0f}"
    )


# -------------------- ações do menu --------------------

def acao_relatorio_completo() -> None:
    print("\nGerando relatório completo (todos algoritmos × 3 cenários × 4 tamanhos)...")
    print("Isto pode levar alguns segundos.\n")
    results = run_all(progress_callback=_mostrar_progresso)
    path = write_report(results)
    print(f"Relatório gerado em: {path}")


def acao_um_algoritmo() -> None:
    nome, algo_func = _escolher_algoritmo()
    scenario = _escolher_cenario()
    size = _escolher_tamanho()

    if not _avisar_algoritmos_lentos(nome, scenario, size):
        print("Execução cancelada.")
        return

    print(f"\nGerando vetor {SCENARIO_LABELS_PT[scenario].lower()} com {size:,} elementos...")
    base_array = generate(scenario, size)

    print(f"Executando {nome} ({INTERACTIVE_RUNS} repetições, média)...")
    metrics = _executar_e_medir(algo_func, base_array, INTERACTIVE_RUNS)

    print()
    _imprimir_cabecalho_tabela()
    _imprimir_linha_resultado(nome, metrics)


def acao_todos_num_cenario() -> None:
    scenario = _escolher_cenario()
    size = _escolher_tamanho()

    print(f"\nGerando vetor {SCENARIO_LABELS_PT[scenario].lower()} com {size:,} elementos...")
    base_array = generate(scenario, size)

    print(f"Executando os 6 algoritmos ({INTERACTIVE_RUNS} repetições cada, média)...\n")
    _imprimir_cabecalho_tabela()
    for nome, algo_func in ALGORITHMS.items():
        # Pula algoritmos que o usuário decidir evitar quando o aviso disparar
        if not _avisar_algoritmos_lentos(nome, scenario, size):
            print(f"| {nome:<15} | {'(pulado)':^11} | {'':>13} | {'':>11} |")
            continue
        try:
            metrics = _executar_e_medir(algo_func, base_array, INTERACTIVE_RUNS)
            _imprimir_linha_resultado(nome, metrics)
        except RecursionError:
            # Quick Sort pode estourar a pilha em vetores ordenados grandes
            print(f"| {nome:<15} | {'stack overflow':^11} | {'':>13} | {'':>11} |")


# -------------------- loop principal do menu --------------------

def menu() -> None:
    # Quick Sort recursivo pode exigir profundidade maior que o padrão (1000)
    sys.setrecursionlimit(50_000)

    acoes = {
        "1": ("Gerar relatório completo em results/relatorio.md", acao_relatorio_completo),
        "2": ("Executar um algoritmo (escolhido por você)",        acao_um_algoritmo),
        "3": ("Executar todos os 6 algoritmos num cenário",        acao_todos_num_cenario),
        "0": ("Sair",                                              None),
    }

    while True:
        print()
        print("=" * 60)
        print("  ANÁLISE COMPARATIVA DE ALGORITMOS DE ORDENAÇÃO")
        print("=" * 60)
        for key, (label, _) in acoes.items():
            print(f"  {key}. {label}")
        print("=" * 60)

        escolha = _prompt("Opção: ")
        if escolha == "0":
            print("Até logo.")
            return
        if escolha not in acoes:
            print("Opção inválida.")
            continue

        _, acao = acoes[escolha]
        try:
            acao()
        except KeyboardInterrupt:
            print("\nExecução interrompida pelo usuário.")
        except Exception as e:
            print(f"\nErro durante a execução: {e}")


if __name__ == "__main__":
    menu()
