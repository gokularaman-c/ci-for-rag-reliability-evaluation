from typing import Dict


def calculate_pass_rate(passed: int, total_tests: int) -> float:
    if total_tests == 0:
        return 0.0
    return round((passed / total_tests) * 100, 2)


def calculate_failure_rate(failed: int, total_tests: int) -> float:
    if total_tests == 0:
        return 0.0
    return round((failed / total_tests) * 100, 2)


def calculate_regression_drop(baseline_pass_rate: float, current_pass_rate: float) -> float:
    return round(baseline_pass_rate - current_pass_rate, 2)


def is_regression_detected(baseline_pass_rate: float, current_pass_rate: float, threshold: float = 5.0) -> bool:
    drop = calculate_regression_drop(baseline_pass_rate, current_pass_rate)
    return drop >= threshold


def build_reliability_summary(
    baseline_result: Dict,
    current_result: Dict,
    threshold: float = 5.0
) -> Dict:
    baseline_pass_rate = calculate_pass_rate(
        baseline_result["passed"],
        baseline_result["total_tests"]
    )

    current_pass_rate = calculate_pass_rate(
        current_result["passed"],
        current_result["total_tests"]
    )

    drop = calculate_regression_drop(baseline_pass_rate, current_pass_rate)

    return {
        "baseline_pass_rate": baseline_pass_rate,
        "current_pass_rate": current_pass_rate,
        "regression_drop": drop,
        "regression_detected": is_regression_detected(
            baseline_pass_rate,
            current_pass_rate,
            threshold
        )
    }