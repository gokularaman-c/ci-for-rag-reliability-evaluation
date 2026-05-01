import json
from pathlib import Path

from src.regression_analyzer import compare_runs
from src.report_generator import generate_markdown_report, save_report


def load_json(file_path: str) -> dict:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_json(data: dict, file_path: str) -> None:
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)


def main() -> None:
    summary = load_json("results/summary.json")

    baseline_result = summary["baseline_run"]
    weak_prompt_result = summary["weak_prompt_run"]
    failure_categories = summary["regression_analysis"]["main_failure_categories"]

    analysis = compare_runs(
        baseline_result=baseline_result,
        current_result=weak_prompt_result,
        failure_categories=failure_categories,
        threshold=5.0
    )

    save_json(analysis, "results/processed/regression_analysis.json")

    markdown_report = generate_markdown_report(analysis)
    save_report(markdown_report, "results/processed/regression_report.md")

    print("Regression analysis generated successfully.")
    print("- results/processed/regression_analysis.json")
    print("- results/processed/regression_report.md")


if __name__ == "__main__":
    main()