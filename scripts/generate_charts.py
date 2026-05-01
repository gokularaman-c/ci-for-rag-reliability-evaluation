import json
from pathlib import Path

import matplotlib.pyplot as plt


def load_json(file_path: str) -> dict:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def ensure_output_dir(output_dir: str) -> Path:
    path = Path(output_dir)
    path.mkdir(parents=True, exist_ok=True)
    return path


def create_pass_rate_chart(summary: dict, output_dir: Path) -> None:
    labels = ["Baseline Prompt", "Weak Prompt"]
    pass_rates = [
        summary["baseline_run"]["pass_rate"],
        summary["weak_prompt_run"]["pass_rate"],
    ]

    plt.figure(figsize=(7, 5))
    plt.bar(labels, pass_rates)
    plt.ylim(0, 100)
    plt.ylabel("Pass Rate (%)")
    plt.title("Prompt Regression: Pass Rate Comparison")

    for index, value in enumerate(pass_rates):
        plt.text(index, value + 2, f"{value}%", ha="center")

    plt.tight_layout()
    plt.savefig(output_dir / "pass_rate_comparison.png", dpi=200)
    plt.close()


def create_pass_fail_chart(summary: dict, output_dir: Path) -> None:
    labels = ["Baseline Prompt", "Weak Prompt"]
    passed = [
        summary["baseline_run"]["passed"],
        summary["weak_prompt_run"]["passed"],
    ]
    failed = [
        summary["baseline_run"]["failed"],
        summary["weak_prompt_run"]["failed"],
    ]

    x_positions = range(len(labels))
    width = 0.35

    plt.figure(figsize=(7, 5))
    plt.bar([x - width / 2 for x in x_positions], passed, width, label="Passed")
    plt.bar([x + width / 2 for x in x_positions], failed, width, label="Failed")
    plt.xticks(list(x_positions), labels)
    plt.ylabel("Number of Test Cases")
    plt.title("Prompt Regression: Passed vs Failed")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_dir / "pass_fail_comparison.png", dpi=200)
    plt.close()


def create_model_pass_rate_chart(model_summary: dict, output_dir: Path) -> None:
    model_results = model_summary["per_model_results"]

    labels = [
        result["model"].replace("ollama:chat:", "").upper()
        for result in model_results
    ]

    pass_rates = [
        result["pass_rate"]
        for result in model_results
    ]

    plt.figure(figsize=(7, 5))
    plt.bar(labels, pass_rates)
    plt.ylim(0, 100)
    plt.ylabel("Pass Rate (%)")
    plt.title("LLM Reliability Comparison")

    for index, value in enumerate(pass_rates):
        plt.text(index, value + 2, f"{value}%", ha="center")

    plt.tight_layout()
    plt.savefig(output_dir / "model_pass_rate_comparison.png", dpi=200)
    plt.close()


def create_model_pass_fail_chart(model_summary: dict, output_dir: Path) -> None:
    model_results = model_summary["per_model_results"]

    labels = [
        result["model"].replace("ollama:chat:", "").upper()
        for result in model_results
    ]

    passed = [
        result["passed"]
        for result in model_results
    ]

    failed = [
        result["failed"]
        for result in model_results
    ]

    x_positions = range(len(labels))
    width = 0.35

    plt.figure(figsize=(7, 5))
    plt.bar([x - width / 2 for x in x_positions], passed, width, label="Passed")
    plt.bar([x + width / 2 for x in x_positions], failed, width, label="Failed")
    plt.xticks(list(x_positions), labels)
    plt.ylabel("Number of Test Cases")
    plt.title("LLM Comparison: Passed vs Failed")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_dir / "model_pass_fail_comparison.png", dpi=200)
    plt.close()


def main() -> None:
    summary = load_json("results/summary.json")
    output_dir = ensure_output_dir("results/charts")

    create_pass_rate_chart(summary, output_dir)
    create_pass_fail_chart(summary, output_dir)

    model_summary_path = Path("results/model_comparison_summary.json")
    if model_summary_path.exists():
        model_summary = load_json(str(model_summary_path))
        create_model_pass_rate_chart(model_summary, output_dir)
        create_model_pass_fail_chart(model_summary, output_dir)

    print("Charts generated successfully:")
    print(f"- {output_dir / 'pass_rate_comparison.png'}")
    print(f"- {output_dir / 'pass_fail_comparison.png'}")
    print(f"- {output_dir / 'model_pass_rate_comparison.png'}")
    print(f"- {output_dir / 'model_pass_fail_comparison.png'}")


if __name__ == "__main__":
    main()