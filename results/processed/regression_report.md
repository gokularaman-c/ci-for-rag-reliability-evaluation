# LLM Reliability Regression Report

## Experiment Overview

This report compares a baseline reliability-focused prompt against a weaker generic prompt to evaluate whether the system can detect reliability regressions in LLM/RAG-style outputs.

## Baseline Configuration

| Metric | Value |
|---|---:|
| Total Tests | 20 |
| Passed | 20 |
| Failed | 0 |
| Pass Rate | 100% |

## Current / Weak Prompt Configuration

| Metric | Value |
|---|---:|
| Total Tests | 20 |
| Passed | 14 |
| Failed | 6 |
| Pass Rate | 70% |

## Regression Summary

| Metric | Value |
|---|---:|
| Baseline Pass Rate | 100.0% |
| Current Pass Rate | 70.0% |
| Regression Drop | 30.0 percentage points |
| Regression Detected | True |

## Main Failure Categories

- hallucination_prevention
- refusal_correctness
- unsupported_information_handling
- prompt_injection_resistance
- strict_behavioral_compliance

## Interpretation

Regression detected with a pass-rate drop of 30.0 percentage points. Failures were mainly observed in: hallucination_prevention, refusal_correctness, unsupported_information_handling, prompt_injection_resistance, strict_behavioral_compliance.

## Conclusion

The experiment shows that weakening prompt-level reliability instructions can reduce the reliability of LLM outputs. The proposed system detects this degradation through automated pass/fail evaluation and regression comparison.
