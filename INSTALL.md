# Install and use the AFTA Security Skill

Package version: **1.1.0**. Source checklist version: **1.9**.

A shared skill for **Claude Code, GitHub Copilot, Cursor, and Codex**, with 79 main requirements and 307 detail and option rows. Previous product answers and selections are excluded.

## Quick installation for all agents

Clone the repository or download and fully extract its ZIP. Open a terminal in the directory containing `install.sh`, `install.ps1`, and the `afta-security` folder.

```bash
git clone https://github.com/OmidHaqi/afta-security.git
cd afta-security
```

After obtaining the files, installation is offline. The installers do not require Git, Node, Python, or administrator access.

### Bash on Linux, macOS, or Git Bash

Install for all projects belonging to the current user:

```bash
bash ./install.sh --agent all --scope user
```

Install in a project to share the skill with a team. Replace the example path:

```bash
bash ./install.sh --agent all --scope project --project "/path/to/project"
```

If your terminal is already in the target project, use the installer's full path:

```bash
bash "/path/to/extracted-package/install.sh" --agent all --scope project
```

### Windows PowerShell

Install for the current user with Windows PowerShell 5.1:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Agent all -Scope user
```

Install in a project. Replace the example path:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Agent all -Scope project -Project "C:\work\my-project"
```

`ExecutionPolicy Bypass` applies only to this installer process; it does not change the machine's permanent policy. Organization policies may still apply.

### PowerShell 7 on Windows, Linux, or macOS

```powershell
pwsh -NoProfile -File ./install.ps1 -Agent all -Scope user
```

For a project:

```powershell
pwsh -NoProfile -File ./install.ps1 -Agent all -Scope project -Project "/path/to/project"
```

Use a Windows path for `-Project` when running on Windows. Start a new agent session after installation. The host must support Agent Skills; for Copilot, use agent mode or another skill-enabled surface. These scripts install the skill files, not the AI applications themselves.

## Install for an individual agent

Replace `all` with one of the following names. These examples use user scope; use project scope for a team repository.

| Agent | Bash | PowerShell parameters |
|---|---|---|
| Claude Code | `bash ./install.sh --agent claude-code --scope user` | `-Agent claude-code -Scope user` |
| GitHub Copilot | `bash ./install.sh --agent copilot --scope user` | `-Agent copilot -Scope user` |
| Cursor | `bash ./install.sh --agent cursor --scope user` | `-Agent cursor -Scope user` |
| Codex | `bash ./install.sh --agent codex --scope user` | `-Agent codex -Scope user` |

A complete Windows command for Claude Code:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Agent claude-code -Scope user
```

## Installation locations

`~` denotes the current user's home directory, usually `UserProfile` on Windows. Project paths are relative to the selected project directory.

| Selection | User installation | Project installation |
|---|---|---|
| `codex` | `~/.agents/skills/afta-security` | `.agents/skills/afta-security` |
| `claude-code` | `~/.claude/skills/afta-security` | `.claude/skills/afta-security` |
| `cursor` | `~/.cursor/skills/afta-security` | `.cursor/skills/afta-security` |
| `copilot` | `~/.copilot/skills/afta-security` | `.github/skills/afta-security` |

`all` installs identical copies under `.agents/skills` and `.claude/skills`. Codex, Cursor, and Copilot recognize the shared agents directory; Claude Code uses the claude directory. Within a scope, choose either `all` or individual-agent installation. Combining them can create duplicate discoverable copies because some agents recognize several compatible directories.

If version 1.0.0 is installed under `~/.codex/skills/afta-security`, preserve any local edits, then move the old copy outside skill discovery directories. The installer does not remove or migrate that legacy location. Installing the same skill name at both user and project scope can also make version selection ambiguous.

In WSL, Bash installs into the Linux environment. Windows and WSL user installations are separate. The project directory must already exist. Project installation adds the skill directories; commit them to your project repository to share them with teammates. User installation does not automatically make the skill available on other machines or in cloud environments.

## Preview and update

Preview destinations without writing files:

```bash
bash ./install.sh --agent all --scope project --project "/path/to/project" --dry-run
```

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Agent all -Scope project -Project "C:\work\my-project" -DryRun
```

Identical installations are skipped. If a different copy exists, installation stops. To update it while preserving a backup, add Force:

```bash
bash ./install.sh --agent all --scope user --force
```

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Agent all -Scope user -Force
```

Previous copies are moved into `.afta-security-backups` in the project root or user home, outside skill discovery directories. The installer prints the backup location. Other skills are not modified. Each destination is updated separately: if a multi-destination install fails, completed destinations remain installed. Resolve the problem and rerun the command.

To uninstall, remove only the `afta-security` directories corresponding to your installation method. To restore a backup, move the current copy outside skill discovery and move the backup into its previous installation path.

## Usage

All agents can use a natural-language request:

```text
Use the afta-security skill to review this project against the AFTA v1.9 checklist.
For each requirement, report evidence, status, gaps, and the next action.
Mark items requiring runtime testing or a security owner's interpretation as needs_review.
```

In Claude Code and Cursor, use `/afta-security` or select it from the `/` menu. In Codex, mention `$afta-security`. In Copilot, mention the skill name in your agent request. Its instructions and resources must be available in the agent's execution environment.

For implementation:

```text
Use afta-security to implement login and session management against the relevant requirements.
Report requirement IDs, acceptance criteria, and verification results.
```

Documentation and the report template are in English. Original requirements and options remain in Persian for source fidelity. Agents should respond in the user's language. The optional report helper currently renders Persian report text.

## Structured reports and optional Python helper

Using the checklist and writing a report do not require Python. The optional JSON/Markdown helper requires Python 3.9 or later. Use `python3` on Linux/macOS, or `py -3` or `python` on Windows, depending on your installation.

Copy `assets/project-profile.json` from the installed skill into your project. Fill in the project name, revision or commit, environment, and scope. Leave unknown features as `null`; provide evidence for `true` or `false` values. See `references/workflow.md` for an example.

Bash with a shared user installation:

```bash
python3 "$HOME/.agents/skills/afta-security/scripts/afta.py" init --profile project-profile.json --out afta-report.json
python3 "$HOME/.agents/skills/afta-security/scripts/afta.py" validate afta-report.json
python3 "$HOME/.agents/skills/afta-security/scripts/afta.py" render afta-report.json --out afta-report.md
```

Windows PowerShell with a shared user installation:

```powershell
py -3 "$HOME/.agents/skills/afta-security/scripts/afta.py" init --profile project-profile.json --out afta-report.json
py -3 "$HOME/.agents/skills/afta-security/scripts/afta.py" validate afta-report.json
py -3 "$HOME/.agents/skills/afta-security/scripts/afta.py" render afta-report.json --out afta-report.md
```

For individual-agent or project installations, adjust the script path using the locations table. Every requirement starts as `needs_review`. The helper does not scan code. Validation checks report structure and required information; evidence accuracy and sufficiency require review. Existing report files are never overwritten.

## Baseline and maintenance

`references/catalog.json` is the shared requirements catalog. Keep original source text, company interpretations, and project decisions separate. The original Word document is not distributed; its fingerprint is recorded in the catalog. The source's authenticity and current official status have not been independently verified. TLS and certificate ambiguities are documented in `references/source-notes.md`. Agent review does not replace formal assessment or certification.

Installation paths were checked against the official documentation:

- [Claude Code Skills](https://code.claude.com/docs/en/skills)
- [GitHub Copilot Agent Skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills)
- [Cursor Agent Skills](https://prod.cursor.com/docs/skills)
- [Codex Skills](https://learn.chatgpt.com/docs/build-skills)

## Installer validation

Tests covered installation for all agents and each individual agent, paths containing spaces/Persian characters/brackets, previews without writes, identical reinstalls, refusal to overwrite without Force, backup preservation, and invalid destinations. Bash and PowerShell 7.7 were executed on Linux. Direct execution on Windows or Windows PowerShell 5.1, and end-to-end agent execution in all four products, have not been tested. The PowerShell installer uses features compatible with version 5.1. Supported paths were checked against official documentation.
