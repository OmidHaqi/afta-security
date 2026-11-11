# AFTA Security Skill

A portable skill for developing and reviewing network applications against the supplied AFTA security requirements checklist, version **1.9**.

Supports **Claude Code, GitHub Copilot, Cursor, and Codex**. Includes **79 main requirements** and **307 detail and option rows** across 15 categories. Package version: **1.1.0**.

## Installation

Clone this repository, then run the installer from its root directory:

```bash
git clone https://github.com/OmidHaqi/afta-security.git
cd afta-security
```

Bash:

```bash
bash ./install.sh --agent all --scope user
```

Windows PowerShell:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Agent all -Scope user
```

See [INSTALL.md](INSTALL.md) for project installation, individual agents, previews, and updates with backups.

## Usage

Ask your agent:

```text
Use the afta-security skill to review this project against the AFTA v1.9 checklist.
For each requirement, report evidence, status, gaps, and the next action.
Mark anything requiring runtime testing or a security owner's interpretation as needs_review.
```

The workflow and resources are defined in [SKILL.md](afta-security/SKILL.md). The optional report helper requires Python 3.9 or later. Installing the skill and using its instructions do not require Python.

## Language and source

The documentation, workflow, and report template are in English. Original requirement text and selection options remain in Persian to preserve traceability to the supplied document. The optional report helper currently produces Persian report text; agents can write English reports using the English template.

General requirements were extracted from a populated document; previous product answers and selections were excluded. The original Word document and company project data are not included. The source's authenticity and current official status have not been independently verified. See [source notes](afta-security/references/source-notes.md) for provenance, the source fingerprint, and unresolved ambiguities.

This skill provides engineering assistance, not certification or a guarantee of security.

## Validation

The Bash and PowerShell 7 installers were tested on Linux. Direct execution on Windows and end-to-end agent behavior in all four products have not been tested.
