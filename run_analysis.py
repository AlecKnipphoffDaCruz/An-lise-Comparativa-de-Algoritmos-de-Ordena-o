#!/usr/bin/env python3
"""
Script para executar a análise comparativa completa sem interação
"""
import sys
from analysis.runner import SCENARIO_LABELS_PT, SIZES, run_all
from analysis.reporter import write_report


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

if __name__ == "__main__":
    sys.setrecursionlimit(50_000)
    
    print("=" * 70)
    print("  ANÁLISE COMPARATIVA - TAMANHOS: 1K, 10K, 50K, 100K")
    print("=" * 70)
    print("\nGerando análise completa (todos algoritmos × 3 cenários × 4 tamanhos)...")
    print("Isto pode levar 5-10 minutos dependendo do hardware.\n")
    
    results = run_all(progress_callback=_mostrar_progresso)
    path = write_report(results)
    
    print(f"\n✓ Análise concluída com sucesso!")
    print(f"✓ Relatório gerado em: {path}")
