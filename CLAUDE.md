# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project purpose

"Desafio 2 — Análise Comparativa de Algoritmos de Ordenação" (Python). Academic assignment that benchmarks six sorting algorithms (Insertion, Selection, Shell, Quick, Merge, Radix) across three input scenarios (random, ascending, descending) at multiple sizes, measuring comparisons, swaps, and wall time. Final artifact is `results/relatorio.md`.

The current run is a **validation run** (small sizes: 100, 500, 1000) — this is intentional until the user explicitly asks for the production run. The banner at the top of `relatorio.md` documents this.

## Commands

```bash
pip install numpy           # only runtime dependency
python main.py              # launches interactive menu
```

The menu offers:
1. Generate full report to `results/relatorio.md`
2. Run a single algorithm (user picks algo + scenario + size)
3. Run all 6 algorithms in one scenario (comparative table in terminal)
4. Display the `GUIA.md` contents
0. Exit

Options 2 and 3 include an "personalizado" size so the user can benchmark arbitrary n.

## Architecture — non-negotiables

These are grading criteria or design commitments to the user — do not "improve" them away.

- **Uniform return contract.** Every algorithm in `algorithms/` accepts an `np.ndarray`, operates on `arr.copy()` (never mutates the input), instruments `comparisons` and `swaps` as integer counters, times with `time.perf_counter()`, and returns exactly `{"sorted_array", "comparisons", "swaps", "time"}`. `analysis/runner.py` and `main.py` both depend on this shape.
- **Same base vector across algorithms and runs.** For each `(scenario, size)` pair, the base array is generated once and each algorithm/run receives `base_array.copy()`. Identical initial conditions.
- **NumPy is mandatory** for vector generation (`import numpy as np`, `from numpy import random as rd`). Professor's required style.
- **Correctness assert.** After every execution, the result is compared to `np.sort(base_array)` via `np.array_equal`. A failure aborts the program — no silent bad data in reports.
- **Results key shape:** `results[(algo_name, scenario, size_label)]` — a 3-tuple.
- **Portuguese code comments are a grading requirement.** Keep them; don't strip.
- **Single source of truth for scenarios.** `SCENARIOS` and `SCENARIO_LABELS_PT` live in `analysis/runner.py`. `reporter.py` and `main.py` import from there.

## Known-fragile combinations

`main.py` has `_avisar_algoritmos_lentos` that warns the user before running:
- **Insertion/Selection at n ≥ 10k** (O(n²) — will take a while).
- **Quick Sort in ascending/descending at n ≥ 5k** — Lomuto pivot (last element) degenerates to O(n²) and can blow the Python recursion stack. `main.py` sets `sys.setrecursionlimit(50_000)` but a pathological case can still stack-overflow; the `acao_todos_num_cenario` action catches `RecursionError` and marks the row as "stack overflow" rather than crashing the whole menu.

These are intentional properties of the algorithms — do not "fix" them (e.g., don't swap in a median-of-three pivot to hide Quick Sort's weakness). The analysis is meant to expose these behaviors.

## Counter semantics (documented in `GUIA.md` and `relatorio.md` too)

- **Merge Sort** has no traditional swap — the counter records **writes** to the destination array during merging.
- **Radix Sort** performs **0 comparisons** by design (it sorts by digit, not by comparing values). Its `swaps` counter records writes to the output buffer during each counting-sort pass.

## Files

- `algorithms/{insertion,selection,shell,quick,merge,radix}_sort.py` — one algorithm each, following the contract above.
- `data/generator.py` — `generate(scenario, size)` using `np.arange` / `np.random.randint`.
- `analysis/runner.py` — owns `ALGORITHMS`, `SCENARIOS`, `SCENARIO_LABELS_PT`, `SIZES`, `RUNS`, and `run_all()`.
- `analysis/reporter.py` — `write_report(results, path)` produces the markdown with Big-O table, methodology, and 3 × len(SIZES) result tables.
- `main.py` — interactive menu. Ties runner + reporter + ad-hoc single-algo runs together.
- `GUIA.md` — beginner-friendly explanation of what sorting is, each algorithm, what comparisons/swaps mean, where NumPy fits. The user is new to this — when asked to explain things, match this document's tone and depth.
- `results/relatorio.md` — generated artifact.
- `desafio_ordenacao.md` — original assignment spec. `analysis/` and `results/` directory names come from it.

## Switching to the production run

Edit `SIZES` in `analysis/runner.py` to `{"small": 1_000, "medium": 10_000, "large": 50_000, "super_large": 100_000}` and regenerate via menu option 1. Expect Insertion/Selection at 100k to take minutes on adversarial scenarios; this is expected output for the analysis.
