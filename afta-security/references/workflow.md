# Assessment workflow

## Scope and applicability

Identify the project's technical stack, architecture, product boundary, and infrastructure responsibilities. TLS may terminate at a reverse proxy; the absence of TLS configuration in application code alone proves neither failure nor satisfaction. An identity provider or framework-managed memory is not sufficient evidence for every related requirement.

Use `assets/project-profile.json` to record the revision, environment, and features. Feature values must be `true`, `false`, or `null`. Every true/false value needs supporting `feature_evidence`; null means unknown. Example profile fragment:

```json
{
  "feature_evidence": {
    "https": [
      {
        "kind": "configuration",
        "reference": "deploy/proxy.conf:24",
        "observation": "TLS is configured at ingress; deployed behavior has not yet been verified."
      }
    ]
  }
}
```

Features describe the **project's required scope and selections**, not merely what is implemented today. A required control being disabled is not a reason to mark its feature false. Assess distinct components and communication paths separately; simple flags do not replace architecture analysis.

- **Base requirements:** Section 2 is in scope, except explicit conditions for key generation/digital signatures in 2-2 and external security products/automatic updates in 2-6. Also assess optional language and conditions within individual requirements.
- **HTTPS:** The source references sections 3-1 and 3-3. Assess certificate validation in 3-5 for the relevant paths. Determine the external-product communication condition in AFTA-3-1-03 separately.
- **TLS:** AFTA-2-9-01 references sections 3-2, 3-3, and 3-4. Record the roles and communication scope.
- **Independent TLS client/server role:** Assess the corresponding category and certificate validation. If the overall TLS selection applies, do not bypass its implications for sections 3-2 through 3-4.
- **SSH:** Assess section 3-6 when SSH is part of the product scope. Administrative SSH on a host does not necessarily make SSH a product capability; establish the responsibility boundary.
- **Key generation, digital signatures, external security products, and automatic updates:** These activate the conditions in AFTA-2-2-03, AFTA-2-2-04, AFTA-2-6-03, and AFTA-2-6-06 respectively.

For an OR group, one true condition makes the requirement applicable. If none is true and at least one is unknown, applicability remains unknown. Use `not_applicable` only when every condition in the group is false with supporting evidence. Helper conditions are an initial filter; assess conditions within details and documented interpretations manually. Use `needs_review` for unresolved applicability or interpretations outside these flags.

## Evidence and status

Assign one status per main requirement:

| Value | Meaning | Minimum documentation |
|---|---|---|
| `satisfied` | Sufficient evidence of satisfaction within the assessed scope | Evidence, detail coverage and selection decisions, and verification appropriate to the control |
| `not_satisfied` | An observed gap or failed test | Gap evidence, impact, and corrective action |
| `needs_review` | Insufficient information, testing, or interpretation | Reason and next action; missing evidence does not count as success |
| `not_applicable` | Applicability conditions do not hold | A specific rationale and evidence of non-applicability |

For each evidence item, record its kind (`code`, `configuration`, `test`, `runtime`, `document`, or `process`), reference, and observation. Keep the commit and environment with the report. Code evidence should identify a file and line or symbol. Test evidence should include the method and result. Runtime evidence should identify the configuration/output and collection time. Treat developer statements as claims needing review, not test results. Do not include secrets or key/password contents in reports.

In each JSON requirement row, `detail_decisions` must explain every detail ID: mandatory, selected, not selected, or not applicable, with a reason. Alternative options are not all mandatory. Not choosing an alternative does not mean failure; distinguish alternatives from mandatory subrequirements. If part of a required control is not satisfied, do not mark the whole requirement satisfied. Explain partial coverage in the rationale.

`verification` must be `not_run`, `static`, `tested`, or `mixed`. Use `verification_notes` to describe the method and limits. Static evidence can support `satisfied` only when the claim is fully demonstrable from that evidence. Behavior such as session termination, log storage failure, invalid-certificate rejection, authentication, access control, and failure recovery requires behavioral tests or relevant execution evidence. If the necessary environment is unavailable, use `needs_review`. A review request does not imply permission to perform destructive testing on a live environment.

## Category review guidance

The following are suggested assessment methods supplied by this package, not official requirement text:

| Category | Useful evidence |
|---|---|
| Audit | Event generation paths, redacted logs, ACLs, integrity, thresholds, write-failure and storage-full behavior |
| Cryptography | Libraries, algorithm settings, key lifecycle, generation/storage/destruction, without revealing keys |
| Identification and authentication | All login and recovery paths, failed-attempt limits, password policies, multiple mechanisms, session invalidation, security attribute changes |
| User data protection | Server-side authorization, data ownership boundaries, import/export, residual data, integrity and error response |
| Security management | Role/operation matrix, restricted administrative operations, defaults, and management settings |
| Security function protection | Secure failure state, component communication, trusted time, update delivery and authenticity |
| Resource allocation | Authorized failure tests for core functions and documented service behavior |
| Product access and sessions | Concurrent sessions, timeout, logout and actual server-side invalidation, access history and session initiation conditions |
| Trusted channels | All ingress/egress, TLS termination, and component paths, followed by conditional protocol requirements |
| HTTPS/TLS/SSH/certificates | Actual endpoint configuration, versions/cipher suites, chain and identity validation, rejection scenarios and error policy |

## Results and priorities

For a full assessment, account for all 79 requirements and report counts for all four statuses. Unknown requirements remain in the coverage denominator; do not silently exclude them from percentages. Avoid vague security percentages. For a limited assessment, identify covered and uncovered IDs.

Prioritize actions by actual impact and exploitability, not requirement number. If an owner or due date was not supplied, mark it as unassigned. Connect corrections to requirement IDs, acceptance criteria, and verification methods. Preserve the pre-remediation report and change statuses only when supported by new evidence.
