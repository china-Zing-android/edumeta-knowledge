# QA Review Rubric

## Scoring

Each QA answer is scored on five 0-2 dimensions.

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| answer_correctness | Incorrect | Partially correct | Correct |
| evidence_match | Evidence does not support answer | Partially supports | Fully supports |
| freshness_version_correctness | Wrong/unknown version | Partially clear | Correct and current for dataset |
| clarification_quality | Should clarify but does not | Clarifies weakly | Clarifies appropriately |
| task_completion | User task not completed | Partially completed | Completed |

## Flags

- `hallucination_flag`: true when the answer includes unsupported factual claims.
- `unsafe_or_overconfident_flag`: true when evidence is missing/conflicting but the answer is definitive.

## Blocking Rules

P0 cases block release if any of the following happen:

- Critical fact is wrong.
- Citation does not support the claim.
- Wrong school/program/degree evidence enters the answer.
- Ambiguous question is answered without clarification.
- Evidence missing but answer is overconfident.

