from typing import Dict, List

from src.reliability_metrics import build_reliability_summary


def compare_runs(
    baseline_result: Dict,
    current_result: Dict,
    failure_categories: List[str],
    threshold: float = 5.0
) -> Dict:
    metrics_summary = build_reliability_summary(
        baseline_result=baseline_result,
        current_result=current_result,
        threshold=threshold
    )

    return {
        "baseline": baseline_result,
        "current": current_result,
        "metrics": metrics_summary,
        "failure_categories": failure_categories,
        "interpretation": generate_interpretation(metrics_summary, failure_categories)
    }


def generate_interpretation(metrics_summary: Dict, failure_categories: List[str]) -> str:
    if metrics_summary["regression_detected"]:
        categories = ", ".join(failure_categories)
        return (
            f"Regression detected with a pass-rate drop of "
            f"{metrics_summary['regression_drop']} percentage points. "
            f"Failures were mainly observed in: {categories}."
        )

    return "No significant regression detected between the compared runs."