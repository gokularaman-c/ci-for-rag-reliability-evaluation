import json
from pathlib import Path


def load_summary(file_path: str) -> dict:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Summary file not found: {file_path}")

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def calculate_regression(baseline: dict, weak_run: dict) -> dict:
    baseline_rate = baseline["pass_rate"]
    weak_rate = weak_run["pass_rate"]
    drop = baseline_rate - weak_rate

    return {
        "baseline_pass_rate": baseline_rate,
        "weak_prompt_pass_rate": weak_rate,
        "drop": drop,
        "regression_detected": drop > 0
    }


def print_report(summary: dict) -> None:
    baseline = summary["baseline_run"]
    weak_run = summary["weak_prompt_run"]
    regression = calculate_regression(baseline, weak_run)

    print("\nLLM Reliability Regression Report")
    print("=" * 45)
    print(f"Project: {summary['project']}")
    print(f"Model: {summary['model']}")
    print("\nBaseline Run")
    print(f"  Configuration : {baseline['configuration']}")
    print(f"  Total Tests   : {baseline['total_tests']}")
    print(f"  Passed        : {baseline['passed']}")
    print(f"  Failed        : {baseline['failed']}")
    print(f"  Pass Rate     : {baseline['pass_rate']}%")

    print("\nWeak Prompt Run")
    print(f"  Configuration : {weak_run['configuration']}")
    print(f"  Total Tests   : {weak_run['total_tests']}")
    print(f"  Passed        : {weak_run['passed']}")
    print(f"  Failed        : {weak_run['failed']}")
    print(f"  Pass Rate     : {weak_run['pass_rate']}%")

    print("\nRegression Analysis")
    if regression["regression_detected"]:
        print(f"  Regression Detected : YES")
        print(f"  Pass Rate Drop      : {regression['drop']} percentage points")
        print("  Interpretation      : Weakening the prompt reduced reliability.")
    else:
        print("  Regression Detected : NO")
        print("  Interpretation      : No reliability drop observed.")

    print("\nMain Failure Categories")
    for category in summary["regression_analysis"]["main_failure_categories"]:
        print(f"  - {category}")


if __name__ == "__main__":
    summary_data = load_summary("results/summary.json")
    print_report(summary_data)