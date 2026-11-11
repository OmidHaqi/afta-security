# Baseline provenance and limitations

Package version: 1.1.0. Supplied document version: 1.9. The original Persian title is «سند الزامات امنیتی برنامه‌های کاربردی تحت شبکه» (Security Requirements for Network Applications). The document states that it is based on version 1.1 of the network application protection profile. This package was built from a user-supplied document; its authenticity, current validity, and status as the latest version have not been independently verified. Assessments reference this supplied baseline.

The input, `QuestAfta.V1.9.docx`, was a populated form. The product introduction, answers, implementation explanations, and selection marks were excluded. Requirement cells, selection instructions, and general options were preserved. The original Word document is not distributed. Its SHA-256 fingerprint in `catalog.json` can be used to identify the input file. Do not assume permission to redistribute the source text publicly.

## Extraction and identifiers

The catalog contains 79 main requirements across 15 categories and 307 detail/option rows. `AFTA-2-1-01` means section 2-1, requirement 1. The `.s01` suffix identifies a detail row within that requirement; it is not a new official requirement number. `source.table_index` and `row_index` are zero-based indices into the Word document's tables, not page numbers. Keep these mappings stable; changes in later versions require an explicit migration. Interpret each ID together with the source version.

Rows contained a requirement or selection instruction, option text, and selection/answer columns. Only general requirement/instruction and option content was extracted; status marks and product-answer columns were excluded. The Persian option «سایر موارد» means “other” and leaves space for a project-specific decision. It is not a reason to reuse a previous product's answer.

Documentation and explanatory labels are in English. Source requirements, selection instructions, and option text remain in Persian without translation or silent correction. `catalog.json` remains the packaged source transcription. The optional Python helper currently generates Persian report text.

## Ambiguities to preserve and review

These issues were identified by comparing statements within the supplied document. They are not official corrections or definitive interpretations:

- **AFTA-3-2-01:** The TLS client text calls for TLS 1.2 and rejection of other versions, but the options include cipher suites attributed to RFC 8446. Do not silently convert this to a TLS 1.3 acceptance or rejection rule. Obtain a documented security owner/assessor decision.
- **AFTA-3-5-01:** The Code Signing name in one detail needs reconciliation with the identifier and OID in the same row. The OCSP reference is written as “RFC 696.” Preserve the raw text and consult the primary standard and responsible reviewer before implementation.
- **AFTA-2-9-01 and section 3-4:** The explicit TLS selection references sections 3-2 through 3-4. Section 3-4 includes mutual authentication; do not mark it inapplicable solely because mTLS is not implemented. HTTPS explicitly references 3-1 and 3-3; do not automatically extend the 3-4 requirement to HTTPS without further review.
- **Sections 2-2 and 3-6:** An algorithm appearing among the supplied options is not a current recommendation to enable it. Choose a secure option compatible with the requirements, and check current primary sources before choosing algorithms or changing cryptographic settings. Separate v1.9 conformance findings from additional security recommendations.
- **AFTA-2-5-06:** The source explicitly states one role per account. Do not automatically treat multiple project roles as equivalent; record any role-model mismatch.
- **AFTA-3-6-09:** Reconcile the description of server authentication and the host-key database with the project's actual client/server roles. Do not silently rewrite the source.

Keep approved company interpretations in a separate record containing the requirement ID, decision, reference/approver, date, and project scope. Do not merge them into source text. Unresolved contradictions prevent a `satisfied` status for the affected requirement.
