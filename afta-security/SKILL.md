---
name: afta-security
description: Apply the supplied AFTA network application security checklist v1.9 to project design, implementation, and evidence-based review when the user requests AFTA requirements, an AFTA audit, or development against this checklist.
---

# AFTA application security

This portable Agent Skill works in Claude Code, GitHub Copilot, Cursor and Codex. Use the supplied Persian checklist to help teams implement and assess network applications. Answer in the user's language. This is engineering assistance against the supplied baseline, not certification or a claim of current official requirements.

## Choose the requested work

- **Design or implementation:** identify the relevant requirements and dependencies, turn them into acceptance criteria, implement within the requested scope, and verify the affected behavior. Do not perform a full audit or unrelated refactor by default.
- **Review:** inspect the project and available deployment evidence, assess each in-scope requirement, and report evidence, gaps and next actions. A review request alone does not authorize modifying the project.
- **Full checklist assessment:** include every catalog ID, even when evidence is unavailable; explicitly mark exclusions and unknowns. Never describe a partial review as full compliance.

## Start with the baseline and scope

1. Read [source-notes.md](references/source-notes.md) for provenance and unresolved source ambiguities, then [workflow.md](references/workflow.md) for applicability and evidence rules.
2. Identify project revision, components, environment, authentication, network paths, TLS termination, external integrations and update mechanism. Use available project files before asking for missing facts. Unknown facts remain unknown; continue independent work.
3. Read [the index](references/index.md), then the category files needed for the task. [catalog.json](references/catalog.json) is the authoritative packaged transcription, including selection instructions and all option rows. Do not choose options merely because a previous product used them: no previous product answers are included.
4. Resolve conditional dependencies using project facts and the source text. Preserve source wording separately from your interpretation. Missing implementation of a required capability is a gap, not grounds to mark it inapplicable.

## Assess and implement

Use exact requirement IDs and subitem IDs in findings and acceptance criteria. Options are not all mandatory: preserve “one is sufficient,” optional language, exceptions and conditional subclauses. Record the chosen options and why. Follow relevant local project instructions and use available code exploration tools; this skill has no required MCP dependency.

Inspect code, configuration and meaningful tests together. Runtime, infrastructure and process requirements need appropriate evidence; source inspection alone cannot establish deployed compliance. For status and evidence rules, use [workflow.md](references/workflow.md).

Do not silently weaken cryptography or change a source requirement to resolve a contradiction. Record ambiguous requirements as `needs_review` and explain the decision needed. Distinguish checklist findings from additional security recommendations.

## Deliver

Use [report-template.md](assets/report-template.md) for human-readable reports. Include baseline version, project revision/environment, scope, coverage, per-ID status/evidence, unresolved interpretations and prioritized actions. Never fabricate evidence or approval. Do not call a project compliant or certified based on an AI review.

For a complete machine-readable assessment, copy [project-profile.json](assets/project-profile.json), fill known facts and supporting evidence, then run the bundled helper with Python 3:

```sh
python3 <skill-dir>/scripts/afta.py init --profile <project-profile.json> --out <new-report.json>
python3 <skill-dir>/scripts/afta.py validate <report.json>
python3 <skill-dir>/scripts/afta.py render <report.json> --out <new-report.md>
```

On Windows, use `py -3` or `python` if `python3` is unavailable. The checklist and human-readable reporting do not require Python; only the optional helper does.

Paths are examples; resolve `<skill-dir>` to this skill's directory. The helper initializes all 79 main requirements and 307 detail rows, validates structure and evidence fields, and renders reports. It does not scan code or prove controls work. New files are created exclusively to avoid overwriting existing assessments. For category filtering use `python3 <skill-dir>/scripts/afta.py list --section 2-3`.
