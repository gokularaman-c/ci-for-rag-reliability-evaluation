# CI for RAG: Automated Regression Detection and Attribution in LLM-Based QA Systems

This project implements a CI-style reliability evaluation framework for Retrieval-Augmented Generation (RAG) based Large Language Model (LLM) question-answering systems. The framework evaluates whether model responses are grounded in retrieved context, safe, policy-compliant, and stable across prompt and model changes.

## Project Overview

Retrieval-Augmented Generation improves factual grounding by providing external context to Large Language Models before generating responses. However, RAG systems can still produce hallucinated, unsupported, or unsafe answers.

Common reliability issues in RAG-based systems include:

- Hallucinated answers
- Unsupported information generation
- Weak refusal behavior
- Ignoring retrieved context
- Prompt-injection vulnerability
- Business-rule violation
- Reliability regression after prompt or model changes

This project addresses these problems by creating a repeatable reliability testing pipeline for RAG-based LLM applications.

## Problem Statement

LLM-based RAG systems are increasingly used to answer questions from external documents and knowledge bases. Even with retrieved context, these systems may hallucinate, ignore evidence, fail to refuse unsupported queries, or become vulnerable to prompt-injection attacks.

Prompt changes, model changes, or retrieval changes can silently reduce reliability without clear runtime errors. Therefore, there is a need for a systematic framework to test RAG-based QA systems for hallucination, refusal correctness, prompt-injection resistance, policy compliance, and reliability regression.

## Objectives

The main objectives of this project are:

- To build a controlled policy-based knowledge base for RAG-style question answering.
- To retrieve relevant context for each user query and pass it to local LLMs.
- To design reliability test cases covering hallucination prevention, grounded answering, refusal correctness, policy compliance, and prompt-injection resistance.
- To compare a reliability-focused prompt with a weak generic prompt and detect prompt-level regression.
- To compare Llama3 and Mistral using the same reliability test suite.
- To generate pass/fail results, regression analysis, charts, reports, and dashboard output.

## Key Features

- Policy-based knowledge base for RAG-style QA
- Context retrieval for each test query
- 20 structured reliability test cases
- Prompt regression testing
- Multi-model comparison using Llama3 and Mistral
- Promptfoo-based pass/fail evaluation
- Python scripts for result analysis and chart generation
- Streamlit dashboard for result visualization
- JSON and Markdown report generation
- Charts for prompt regression and model comparison

## Reliability Checks

The reliability test suite covers the following categories:

- Grounded answering
- Hallucination prevention
- Refusal correctness
- Business-rule compliance
- Account-safety behavior
- Prompt-injection resistance
- Unsupported-information handling
- Strict behavioral compliance

## System Workflow

The system follows this evaluation pipeline:

```text
User Query / Test Case
        ↓
Context Retrieval from Policy Knowledge Base
        ↓
Prompt + Retrieved Context
        ↓
Local LLM Execution through Ollama
        ↓
Promptfoo Evaluation using Assertions
        ↓
Pass / Fail Result
        ↓
Regression Analysis and Model Comparison
        ↓
Charts, Reports, and Streamlit Dashboard
```

## Knowledge Base

The project uses a controlled policy-based knowledge base instead of a large public dataset. The knowledge base simulates a customer-support RAG system.

The knowledge base contains:

- Return Policy
- Order Support Policy
- Account Security Policy
- Damaged Package Policy
- Security / Prompt-Injection Policy

Each reliability test query retrieves relevant context from these documents. The retrieved context is then passed to the local LLM for response generation.

## Tech Stack

- Python
- Ollama
- Llama3
- Mistral
- Promptfoo
- Streamlit
- Matplotlib
- Pandas
- NumPy
- YAML
- JSON
- CSV

## Project Structure

```text
llm-reliability-platform/
├── context.py
├── promptfooconfig.yaml
├── promptfooconfig_baseline.yaml
├── promptfooconfig_weak.yaml
├── promptfooconfig_model_compare.yaml
├── data/
│   ├── test_cases.csv
│   └── knowledge_base/
├── src/
│   ├── context_provider.py
│   ├── rag_retriever.py
│   ├── reliability_metrics.py
│   ├── regression_analyzer.py
│   ├── report_generator.py
│   └── category_metrics.py
├── scripts/
│   ├── compare_runs.py
│   ├── generate_charts.py
│   ├── build_summary.py
│   ├── run_analysis.sh
│   └── category_report.py
├── results/
│   ├── summary.json
│   ├── model_comparison_summary.json
│   ├── category_scores.csv
│   ├── processed/
│   └── charts/
├── promptfoo/
├── dashboard/
│   └── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Experiments and Results

### 1. Prompt Regression Experiment

The prompt regression experiment compares a reliability-focused prompt with a weak generic prompt using the same 20 reliability test cases.

| Prompt Configuration | Total Tests | Passed | Failed | Pass Rate |
|---|---:|---:|---:|---:|
| Reliability-Focused Prompt | 20 | 20 | 0 | 100% |
| Weak Generic Prompt | 20 | 14 | 6 | 70% |

Regression Drop:

```text
Regression Drop = Baseline Pass Rate - Weak Prompt Pass Rate
Regression Drop = 100% - 70% = 30%
```

The result shows that removing strict grounding, refusal, and safety instructions caused a 30 percentage-point reliability drop.

### 2. Multi-Model Comparison

The same 20 reliability test cases were evaluated across two local LLMs: Llama3 and Mistral.

| Model | Total Tests | Passed | Failed | Pass Rate |
|---|---:|---:|---:|---:|
| Llama3 | 20 | 20 | 0 | 100% |
| Mistral | 20 | 16 | 4 | 80% |
| Overall | 40 | 36 | 4 | 90% |

The result shows that different LLMs can behave differently under the same prompt, same retrieved context, and same reliability test suite.

## Output

The system generates the following outputs:

- Pass/fail result for each reliability test case
- Prompt regression summary
- Multi-model comparison summary
- Regression drop calculation
- JSON result files
- Markdown regression report
- Pass-rate comparison charts
- Passed-vs-failed comparison charts
- Streamlit dashboard views

## How to Run

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Check Ollama Models

Make sure Ollama is installed and the required models are available.

```bash
ollama list
```

Required models:

```text
llama3
mistral
```

### 3. Run Baseline Evaluation

```bash
npx promptfoo eval
```

Expected result:

```text
20 passed, 0 failed, 100%
```

### 4. Run Weak Prompt Evaluation

```bash
npx promptfoo eval -c promptfooconfig_weak.yaml
```

Expected result:

```text
14 passed, 6 failed, 70%
```

### 5. Run Multi-Model Comparison

```bash
npx promptfoo eval -c promptfooconfig_model_compare.yaml
```

Expected result:

```text
36 passed, 4 failed, 90%
```

### 6. Generate Charts

```bash
python scripts/generate_charts.py
```

Generated chart files are stored in:

```text
results/charts/
```

### 7. Run Streamlit Dashboard

```bash
streamlit run dashboard/app.py
```

The dashboard displays prompt regression results, model comparison results, charts, and generated reports.

## Main Result Summary

| Experiment | Result |
|---|---|
| Reliability-focused prompt | 20/20 passed, 100% pass rate |
| Weak generic prompt | 14/20 passed, 70% pass rate |
| Regression drop | 30 percentage points |
| Llama3 | 20/20 passed, 100% pass rate |
| Mistral | 16/20 passed, 80% pass rate |
| Overall multi-model comparison | 36/40 passed, 90% pass rate |

## Practical Use Cases

This framework can be useful in real-world scenarios such as:

- Customer-support chatbots
- Enterprise knowledge assistants
- Policy-based document QA systems
- Educational assistants
- Healthcare, legal, or finance QA systems
- Pre-deployment testing of RAG-based LLM applications
- Prompt version testing
- Model comparison before deployment

## Outcome

The project demonstrates that RAG reliability can be tested using a CI-style workflow. It detects prompt-level regression, compares model reliability, and provides interpretable outputs through charts, reports, and dashboard views.

The final outcome is a working prototype for repeatable reliability evaluation of RAG-based LLM question-answering systems.

## Author

Gokularaman C  
