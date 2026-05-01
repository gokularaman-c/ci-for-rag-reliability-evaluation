# Regression Experiment Summary

## Objective
To evaluate whether the reliability testing platform can detect behavioral regressions when prompt instructions are weakened.

## Experimental Setup
Two prompt configurations were compared:

1. Baseline Reliability Prompt
   - Uses strict grounding rules
   - Requires unsupported answers to return "I don't know."
   - Prevents revealing hidden/system instructions
   - Enforces business and safety policies

2. Weak Generic Prompt
   - Removes strict grounding rules
   - Encourages complete and helpful responses
   - Does not strongly enforce refusal behavior

## Results

| Configuration | Passed | Failed | Pass Rate |
|---|---:|---:|---:|
| Baseline Reliability Prompt | 10 | 0 | 100% |
| Weak Generic Prompt | 7 | 3 | 70% |

## Regression Detected
Reliability dropped from 100% to 70%.

Regression impact:
- 30 percentage-point drop in pass rate
- Failures observed in hallucination prevention, refusal correctness, and business-rule compliance
- Weak prompt increased unsupported and policy-violating responses

## Conclusion
The experiment shows that the proposed reliability evaluation pipeline can detect regressions when the LLM prompt is modified. This supports the need for CI-style testing and reliability validation in LLM/RAG systems.