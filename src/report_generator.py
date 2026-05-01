from pathlib import Path
from typing import Dict


def generate_markdown_report(analysis: Dict) -> str:
    baseline = analysis["baseline"]
    current = analysis["current"]
    metrics = analysis["metrics"]
    failure_categories = analysis["failure_categories"]

    categories_text = "\n".join([f"- {category}" for category in failure_categories])

    return f"""# LLM Reliability Regression Report

## Experiment Overview

This report compares a baseline reliability-focused prompt against a weaker generic prompt to evaluate whether the system can detect reliability regressions in LLM/RAG-style outputs.

## Baseline Configuration

| Metric | Value |
|---|---:|
| Total Tests | {baseline["total_tests"]} |
| Passed | {baseline["passed"]} |
| Failed | {baseline["failed"]} |
| Pass Rate | {baseline["pass_rate"]}% |

## Current / Weak Prompt Configuration

| Metric | Value |
|---|---:|
| Total Tests | {current["total_tests"]} |
| Passed | {current["passed"]} |
| Failed | {current["failed"]} |
| Pass Rate | {current["pass_rate"]}% |

## Regression Summary

| Metric | Value |
|---|---:|
| Baseline Pass Rate | {metrics["baseline_pass_rate"]}% |
| Current Pass Rate | {metrics["current_pass_rate"]}% |
| Regression Drop | {metrics["regression_drop"]} percentage points |
| Regression Detected | {metrics["regression_detected"]} |

## Main Failure Categories

{categories_text}

## Interpretation

{analysis["interpretation"]}

## Conclusion

The experiment shows that weakening prompt-level reliability instructions can reduce the reliability of LLM outputs. The proposed system detects this degradation through automated pass/fail evaluation and regression comparison.
"""


def save_report(markdown_report: str, output_path: str) -> None:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        file.write(markdown_report)