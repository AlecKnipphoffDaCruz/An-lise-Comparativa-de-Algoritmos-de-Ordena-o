#!/usr/bin/env python3
"""
Script para executar a análise comparativa completa sem interação
"""
import sys
from analysis.runner import run_all
from analysis.reporter import write_report

if __name__ == "__main__":
    sys.setrecursionlimit(50_000)
    
    print("=" * 70)
    print("  ANÁLISE COMPARATIVA - TAMANHOS: 1K, 10K, 50K, 100K")
    print("=" * 70)
    print("\nGerando análise completa (todos algoritmos × 3 cenários × 4 tamanhos)...")
    print("Isto pode levar 5-10 minutos dependendo do hardware.\n")
    
    results = run_all()
    path = write_report(results)
    
    print(f"\n✓ Análise concluída com sucesso!")
    print(f"✓ Relatório gerado em: {path}")
