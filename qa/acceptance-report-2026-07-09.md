# MVP Acceptance Report

Generated at: 2026-07-09T15:01:49.301170+00:00

Decision: **NOT RELEASE READY**

Release status: `failed`
Gate summary: 14 passed / 3 failed / 17 total

## Gate Results

| Gate | Status | Passed | Failure sample |
| --- | --- | --- | --- |
| data_validation | passed | yes |  |
| incremental_diff | unchanged | yes |  |
| batch_validation | success | yes |  |
| batch_diff | success | yes |  |
| batch_index | success | yes |  |
| batch_weknora_sync | success | yes |  |
| live_data | passed | yes |  |
| mit_gold_qa | passed | yes |  |
| mvp_uat | passed | yes |  |
| mvp_uat_conversations | passed | yes |  |
| human_qa_review | not_ready | no | status 'not_ready' not in accepted statuses ['passed']; human review file is missing or empty |
| mvp_scope | passed | yes |  |
| tool_consistency | passed | yes |  |
| weknora_worker_local | success | yes |  |
| external_readiness | not_ready | no | status 'not_ready' not in accepted statuses ['ready']; weknora: missing_config; l0: missing_config |
| external_live_smoke | not_ready | no | status 'not_ready' not in accepted statuses ['passed']; weknora: WEKNORA_BASE_URL is required for real WeKnora import mode.; l0: L0_API_BASE_URL is required. |
| external_agent_smoke | passed | yes |  |

## Scope

Normalized schools: 5
UAT school coverage: 5
Conversation school coverage: 5

## Human Review

Status: `not_ready`
Reviewed base cases: 0
Reviewed conversations: 0
