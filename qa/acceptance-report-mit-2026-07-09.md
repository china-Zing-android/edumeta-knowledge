# MIT Acceptance Report

Generated at: 2026-07-09T14:59:11.308131+00:00

Decision: **NOT RELEASE READY**

Release status: `failed`
Gate summary: 8 passed / 3 failed / 11 total

## Gate Results

| Gate | Status | Passed | Failure sample |
| --- | --- | --- | --- |
| data_validation | passed | yes |  |
| incremental_diff | unchanged | yes |  |
| live_data | passed | yes |  |
| mit_gold_qa | passed | yes |  |
| mit_uat_conversations | passed | yes |  |
| human_qa_review_mit | not_ready | no | status 'not_ready' not in accepted statuses ['passed']; human review file is missing or empty |
| tool_consistency_mit | passed | yes |  |
| weknora_worker_local | success | yes |  |
| external_readiness | not_ready | no | status 'not_ready' not in accepted statuses ['ready']; weknora: missing_config; l0: missing_config |
| external_live_smoke | not_ready | no | status 'not_ready' not in accepted statuses ['passed']; weknora: WEKNORA_BASE_URL is required for real WeKnora import mode.; l0: L0_API_BASE_URL is required. |
| external_agent_smoke | passed | yes |  |

## Scope

Acceptance profile: MIT only
Normalized scope: `mit`
MIT live data status: `passed`
MIT catalog entries: 157
MIT URL manifest rows: 107
MIT quick facts: 241

## Human Review

Status: `not_ready`
Reviewed base cases: 0
Reviewed conversations: 0
