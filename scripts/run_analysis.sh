#!/bin/bash

echo "Running LLM reliability regression analysis..."

PYTHONPATH=. python3 scripts/compare_runs.py
PYTHONPATH=. python3 scripts/build_summary.py
python3 scripts/generate_charts.py

echo "Analysis pipeline completed."
echo "Generated outputs:"
echo "- results/processed/regression_analysis.json"
echo "- results/processed/regression_report.md"
echo "- results/charts/pass_rate_comparison.png"
echo "- results/charts/pass_fail_comparison.png"