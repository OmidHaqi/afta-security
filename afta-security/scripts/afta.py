#!/usr/bin/env python3
"""Offline checklist scaffolding; no code scanning, network calls or certification."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / 'references/catalog.json'
STATUSES = {'satisfied', 'not_satisfied', 'needs_review', 'not_applicable'}
KINDS = {'code', 'configuration', 'test', 'runtime', 'document', 'process'}


def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def write_new(path, data):
    with Path(path).open('x', encoding='utf-8') as f:
        f.write(data)


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def evidence_errors(value, label):
    if not isinstance(value, list) or not value:
        return [f'{label}: at least one evidence item required']
    errors = []
    for e in value:
        if not isinstance(e, dict) or e.get('kind') not in KINDS or not all(
            nonempty(e.get(k)) for k in ('reference', 'observation')
        ):
            errors.append(f'{label}: evidence needs kind, reference and observation')
    return errors


def profile_errors(profile, catalog):
    if not isinstance(profile, dict):
        return ['profile must be an object']
    errors = []
    for k in ('project', 'revision', 'environment', 'scope'):
        if not nonempty(profile.get(k)):
            errors.append(f'profile.{k}: required')
    features = profile.get('features')
    if not isinstance(features, dict) or set(features) != set(catalog['flags']):
        errors.append('profile.features: must contain exactly the catalog flags')
        return errors
    evidence = profile.get('feature_evidence', {})
    if not isinstance(evidence, dict):
        errors.append('profile.feature_evidence: must be an object')
        evidence = {}
    for flag, value in features.items():
        if value is not None and type(value) is not bool:
            errors.append(f'profile.features.{flag}: use true, false or null')
        elif value is not None:
            errors += evidence_errors(evidence.get(flag), f'profile.feature_evidence.{flag}')
    return errors


def applicability(req, profile):
    flags = req['applies_when_any']
    if not flags:
        return True
    values = [profile['features'][f] for f in flags]
    if any(v is True for v in values):
        return True
    return None if any(v is None for v in values) else False


def baseline(catalog):
    return {k: catalog[k] for k in ('package_version', 'source_version', 'source_sha256')} | {
        'catalog_sha256': hashlib.sha256(CATALOG_PATH.read_bytes()).hexdigest()
    }


def initialize(profile, catalog):
    rows = []
    for req in catalog['requirements']:
        applies = applicability(req, profile)
        rows.append({
            'id': req['id'], 'applicable': applies, 'status': 'needs_review',
            'rationale': ('کاربرد بند نیازمند تکمیل است.' if applies is None else
                          'شرط اولیه رد شده؛ دلیل و شاهد عدم کاربرد بررسی شود.' if applies is False else
                          'نیازمند بررسی شواهد و زیرموارد.'),
            'evidence': [], 'verification': 'not_run', 'verification_notes': '',
            'detail_decisions': {d['id']: '' for d in req['details']},
            'open_questions': [], 'next_action': 'بررسی الزام، گزینه‌ها و شواهد پروژه',
            'priority': 'unassigned', 'owner': '', 'due': ''
        })
    return {'schema_version': 1, 'baseline': baseline(catalog), 'profile': profile,
            'assessment_date': '', 'requirements': rows}


def validate(report, catalog):
    if not isinstance(report, dict):
        return ['report must be an object']
    errors = []
    if report.get('schema_version') != 1:
        errors.append('unsupported schema_version')
    if report.get('baseline') != baseline(catalog):
        errors.append('baseline/catalog fingerprint mismatch; migrate explicitly')
    errors += profile_errors(report.get('profile'), catalog)
    rows = report.get('requirements')
    if not isinstance(rows, list):
        return errors + ['requirements must be a list']
    expected = {r['id']: r for r in catalog['requirements']}
    ids = [r.get('id') if isinstance(r, dict) else None for r in rows]
    if len(ids) != len(expected) or set(x for x in ids if isinstance(x, str)) != set(expected):
        errors.append('requirements must contain every catalog ID exactly once')
    if len(set(x for x in ids if isinstance(x, str))) != len(ids):
        errors.append('duplicate or invalid requirement IDs')
    profile_ok = not profile_errors(report.get('profile'), catalog)
    for row in rows:
        if not isinstance(row, dict) or not isinstance(row.get('id'), str) or row['id'] not in expected:
            errors.append('invalid requirement row')
            continue
        key = row['id']; req = expected[key]; status = row.get('status')
        for field in ('verification_notes', 'next_action', 'priority', 'owner', 'due'):
            if not isinstance(row.get(field), str):
                errors.append(f'{key}: {field} must be a string')
        if not isinstance(row.get('evidence'), list):
            errors.append(f'{key}: evidence must be a list')
        if status not in STATUSES:
            errors.append(f'{key}: invalid status')
        applies = row.get('applicable')
        if applies is not None and type(applies) is not bool:
            errors.append(f'{key}: applicable must be true, false or null')
        if profile_ok and applies is not applicability(req, report['profile']):
            errors.append(f'{key}: applicability conflicts with profile; update project facts')
        if not nonempty(row.get('rationale')):
            errors.append(f'{key}: rationale required')
        if row.get('verification') not in {'not_run', 'static', 'tested', 'mixed'}:
            errors.append(f'{key}: invalid verification')
        details = row.get('detail_decisions')
        detail_ids = {d['id'] for d in req['details']}
        if not isinstance(details, dict) or set(details) != detail_ids:
            errors.append(f'{key}: all detail IDs required, with no extras')
        if status in {'satisfied', 'not_satisfied', 'not_applicable'}:
            errors += evidence_errors(row.get('evidence'), key)
        elif row.get('evidence'):
            errors += evidence_errors(row['evidence'], key)
        if status in {'satisfied', 'not_satisfied'} and applies is not True:
            errors.append(f'{key}: resolve applicability before assigning this status')
        if status == 'not_applicable' and applies is not False:
            errors.append(f'{key}: not_applicable requires false applicability')
        if status == 'satisfied':
            if not isinstance(details, dict) or not all(nonempty(details.get(d)) for d in detail_ids):
                errors.append(f'{key}: explain every detail/selection decision')
            if row.get('verification') == 'not_run' or not nonempty(row.get('verification_notes')):
                errors.append(f'{key}: verification method and notes required')
            if row.get('open_questions'):
                errors.append(f'{key}: unresolved questions prevent satisfied')
        if not isinstance(row.get('open_questions'), list) or not all(
            nonempty(x) for x in row.get('open_questions', [])
        ):
            errors.append(f'{key}: open_questions must be a list of nonempty strings')
        if status in {'needs_review', 'not_satisfied'} and not nonempty(row.get('next_action')):
            errors.append(f'{key}: next_action required')
    return errors


def md(value):
    return str(value).replace('|', '\\|').replace('\n', '<br>')


def render(report, catalog):
    counts = Counter(r['status'] for r in report['requirements'])
    p = report['profile']
    out = ['# گزارش بررسی الزامات امنیتی افتا', '',
           f"پروژه: {p['project']} — نسخه: {p['revision']} — محیط: {p['environment']}", '',
           f"دامنه: {p['scope']}", '', f"تاریخ بررسی: {report.get('assessment_date') or 'ثبت نشده'}", '',
           'نسخهٔ منبع: 1.9؛ نسخهٔ بسته: ' + catalog['package_version'], '',
           'این گزارش ارزیابی مهندسی در دامنهٔ مشخص‌شده است و گواهی یا تضمین امنیت نیست.', '',
           '## پوشش', '', f"کل بندها: {len(report['requirements'])}", '']
    labels = {'satisfied':'رعایت شده','not_satisfied':'رعایت نشده','needs_review':'نیازمند بررسی','not_applicable':'نامرتبط با دلیل'}
    out += [f'- {label}: {counts[status]}' for status,label in labels.items()]
    out += ['', '## وضعیت بندها', '', '| شناسه | وضعیت | دلیل | اقدام بعدی |', '|---|---|---|---|']
    for r in report['requirements']:
        out.append('| ' + ' | '.join(md(x) for x in (r['id'], labels[r['status']], r['rationale'], r['next_action'])) + ' |')
    out += ['', '## پروفایل پروژه', '', '```json', json.dumps(p, ensure_ascii=False, indent=2), '```', '', '## جزئیات و شواهد', '']
    reqs = {r['id']:r for r in catalog['requirements']}
    for r in report['requirements']:
        out += [f"### {r['id']}", '', reqs[r['id']]['text'], '',
                f"وضعیت: {labels[r['status']]}؛ کاربرد: {r['applicable']}", '', r['rationale'], '',
                f"روش بررسی: {r['verification']} — {r['verification_notes'] or 'ثبت نشده'}", '']
        for e in r['evidence']:
            out += [f"- {e['kind']} / {e['reference']}: {e['observation']}"]
        for d in reqs[r['id']]['details']:
            out += ['', f"- {d['id']}: {d['instruction']} {d['text']}",
                    '  تصمیم: ' + (r['detail_decisions'][d['id']] or 'نیازمند بررسی')]
        if r['open_questions']:
            out += ['', 'ابهام‌ها:'] + ['- '+q for q in r['open_questions']]
        out += ['', 'اقدام: '+r['next_action'], '',
                f"اولویت: {r['priority']}؛ مسئول: {r['owner'] or 'تعیین نشده'}؛ موعد: {r['due'] or 'تعیین نشده'}", '']
    return '\n'.join(out)+'\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    ls = sub.add_parser('list'); ls.add_argument('--section')
    init = sub.add_parser('init'); init.add_argument('--profile', required=True); init.add_argument('--out', required=True)
    val = sub.add_parser('validate'); val.add_argument('report')
    rend = sub.add_parser('render'); rend.add_argument('report'); rend.add_argument('--out', required=True)
    args = parser.parse_args(); catalog = read(CATALOG_PATH)
    if args.command == 'list':
        selected = [r for r in catalog['requirements'] if not args.section or r['section'] == args.section]
        if not selected:
            parser.error('unknown or empty section')
        for r in selected:
            print(f"{r['id']}\t{r['category']}\t{r['text']}")
        return
    if args.command == 'init':
        profile = read(args.profile); errors = profile_errors(profile, catalog)
        if errors:
            raise ValueError('\n'.join(errors))
        write_new(args.out, json.dumps(initialize(profile, catalog), ensure_ascii=False, indent=2)+'\n')
        print(f"Created {args.out}: {len(catalog['requirements'])} requirements, all needs_review.")
        return
    report = read(args.report); errors = validate(report, catalog)
    if errors:
        raise ValueError('\n'.join(errors))
    if args.command == 'render':
        write_new(args.out, render(report, catalog)); print(f'Created {args.out}')
    else:
        print('Valid structure and evidence fields. Evidence truth, sufficiency, and source interpretation require review.')


if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError, TypeError, KeyError) as exc:
        print(f'Error: {exc}', file=sys.stderr)
        sys.exit(1)
