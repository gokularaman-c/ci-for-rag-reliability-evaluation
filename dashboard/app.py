import json
from pathlib import Path

import streamlit as st


BASE_DIR = Path(__file__).resolve().parents[1]

SUMMARY_PATH = BASE_DIR / "results" / "summary.json"
MODEL_COMPARISON_PATH = BASE_DIR / "results" / "model_comparison_summary.json"
REPORT_PATH = BASE_DIR / "results" / "processed" / "regression_report.md"

PASS_RATE_CHART = BASE_DIR / "results" / "charts" / "pass_rate_comparison.png"
PASS_FAIL_CHART = BASE_DIR / "results" / "charts" / "pass_fail_comparison.png"
MODEL_PASS_RATE_CHART = BASE_DIR / "results" / "charts" / "model_pass_rate_comparison.png"
MODEL_PASS_FAIL_CHART = BASE_DIR / "results" / "charts" / "model_pass_fail_comparison.png"


def load_json(path: Path) -> dict:
    if not path.exists():
        st.warning(f"Missing file: {path}")
        return {}

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def load_text(path: Path) -> str:
    if not path.exists():
        return f"Missing file: {path}"

    return path.read_text(encoding="utf-8")


st.set_page_config(
    page_title="LLM Reliability Dashboard",
    layout="wide"
)

st.title("LLM Reliability Engineering Platform")
st.caption("RAG-based evaluation, prompt regression testing, and multi-model reliability comparison")

summary = load_json(SUMMARY_PATH)
model_comparison = load_json(MODEL_COMPARISON_PATH)

if summary:
    baseline = summary["baseline_run"]
    weak = summary["weak_prompt_run"]
    regression = summary["regression_analysis"]

    st.header("1. Prompt Regression Experiment")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Tests", baseline["total_tests"])
    col2.metric("Baseline Pass Rate", f"{baseline['pass_rate']}%")
    col3.metric("Weak Prompt Pass Rate", f"{weak['pass_rate']}%")
    col4.metric("Regression Drop", f"{regression['pass_rate_drop']}%")

    st.write(
        """
        This experiment compares a reliability-focused prompt against a weak generic prompt.
        The objective is to detect whether LLM reliability drops when grounding, refusal,
        and safety instructions are weakened.
        """
    )

    st.table(
        {
            "Configuration": [
                str(baseline["configuration"]),
                str(weak["configuration"])
            ],
            "Total Tests": [
                str(baseline["total_tests"]),
                str(weak["total_tests"])
            ],
            "Passed": [
                str(baseline["passed"]),
                str(weak["passed"])
            ],
            "Failed": [
                str(baseline["failed"]),
                str(weak["failed"])
            ],
            "Pass Rate": [
                f"{baseline['pass_rate']}%",
                f"{weak['pass_rate']}%"
            ]
        }
    )

    st.subheader("Prompt Regression Charts")

    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:
        if PASS_RATE_CHART.exists():
            st.image(str(PASS_RATE_CHART), caption="Pass Rate Comparison")
        else:
            st.warning("Pass-rate chart not found.")

    with chart_col2:
        if PASS_FAIL_CHART.exists():
            st.image(str(PASS_FAIL_CHART), caption="Passed vs Failed Test Cases")
        else:
            st.warning("Pass/fail chart not found.")

    st.subheader("Failure Categories")

    for category in regression["main_failure_categories"]:
        st.markdown(f"- `{category}`")

    st.divider()

if model_comparison:
    st.header("2. Multi-Model Reliability Comparison")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Models Compared", len(model_comparison["models"]))
    col2.metric("Total Evaluations", model_comparison["total_evaluations"])
    col3.metric("Passed", model_comparison["passed"])
    col4.metric("Overall Pass Rate", f"{model_comparison['overall_pass_rate']}%")

    st.write(
        """
        This experiment evaluates the same reliability test suite across multiple local LLMs.
        The goal is to verify whether the platform can compare reliability behavior across
        different model backends using the same RAG context and evaluation rules.
        """
    )

    st.table(
        {
            "Metric": [
                "Models",
                "Test cases per model",
                "Total evaluations",
                "Passed",
                "Failed",
                "Overall pass rate",
                "Total tokens"
            ],
            "Value": [
                ", ".join(model_comparison["models"]),
                str(model_comparison["test_cases_per_model"]),
                str(model_comparison["total_evaluations"]),
                str(model_comparison["passed"]),
                str(model_comparison["failed"]),
                f"{model_comparison['overall_pass_rate']}%",
                str(model_comparison["tokens"]["total"])
            ]
        }
    )

    st.subheader("Model Comparison Charts")

    model_chart_col1, model_chart_col2 = st.columns(2)

    with model_chart_col1:
        if MODEL_PASS_RATE_CHART.exists():
            st.image(str(MODEL_PASS_RATE_CHART), caption="Model-wise Pass Rate Comparison")
        else:
            st.warning("Model pass-rate chart not found.")

    with model_chart_col2:
        if MODEL_PASS_FAIL_CHART.exists():
            st.image(str(MODEL_PASS_FAIL_CHART), caption="Model-wise Passed vs Failed Test Cases")
        else:
            st.warning("Model pass/fail chart not found.")

    st.subheader("Model Comparison Interpretation")
    st.info(model_comparison["interpretation"])

    st.divider()

st.header("3. Generated Regression Report")

report_text = load_text(REPORT_PATH)
st.markdown(report_text)