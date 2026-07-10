"""Packaging / consistency regression tests.

Guards against the two defect classes that previously slipped past the smoke
test: (1) shipped "Code"/dashboard links pointing at a wrong GitHub owner or a
mismatched repo slug (a reader clicking "Code" would hit a 404), and (2) the
registry.csv losing its documented column contract.
"""

import csv
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

# The canonical repository identity (matches the origin remote:
# https://github.com/mahmood726-cyber/worldipd-private.git).
EXPECTED_OWNER = 'mahmood726-cyber'
EXPECTED_REPO = 'worldipd-private'

REGISTRY_COLUMNS = [
    'id', 'domain', 'source', 'source_url',
    'license', 'citation', 'notes', 'access',
]

# Files that carry outward-facing GitHub / Pages links for the submission.
LINK_FILES = [
    'e156-submission/config.json',
    'e156-submission/paper.json',
    'e156-submission/index.html',
    'e156-submission/assets/dashboard.html',
    'docs/protocol.md',
    'paper/manuscript.md',
]

GITHUB_RE = re.compile(r'https?://github\.com/([A-Za-z0-9._-]+)/([A-Za-z0-9._-]+?)(?:\.git)?(?=["\'\s<)/]|$)')
PAGES_RE = re.compile(r'https?://([A-Za-z0-9._-]+)\.github\.io/([A-Za-z0-9._-]+)')


def test_registry_header_contract():
    registry = ROOT / 'inst' / 'registry' / 'registry.csv'
    assert registry.exists(), 'inst/registry/registry.csv is missing'
    with registry.open(encoding='utf-8', newline='') as fh:
        header = next(csv.reader(fh))
    assert header == REGISTRY_COLUMNS, header


def test_extdata_dir_resolves():
    # README.md documents inst/extdata/<id>.csv as the dataset location.
    assert (ROOT / 'inst' / 'extdata').is_dir()


def test_shipped_links_are_consistent_and_resolvable():
    seen = 0
    for rel in LINK_FILES:
        path = ROOT / rel
        if not path.exists():
            continue
        text = path.read_text(encoding='utf-8')
        for owner, repo in GITHUB_RE.findall(text):
            seen += 1
            assert owner == EXPECTED_OWNER, f'{rel}: wrong github owner {owner!r}'
            assert repo == EXPECTED_REPO, f'{rel}: wrong github repo slug {repo!r}'
        for user, repo in PAGES_RE.findall(text):
            seen += 1
            assert user == EXPECTED_OWNER, f'{rel}: wrong pages user {user!r}'
            assert repo == EXPECTED_REPO, f'{rel}: wrong pages repo slug {repo!r}'
    assert seen > 0, 'no GitHub/Pages links found to validate'


def test_no_stray_wrong_owner_or_scaffold_url():
    # Belt-and-braces: the specific past URL mistakes must not reappear anywhere
    # in the submission bundle or push helper. Only URL contexts are checked --
    # the config.json "slug" field is an internal submission identifier, not a
    # repository link, so it is intentionally out of scope here.
    scaffold_url_re = re.compile(
        r'(?:github\.com/[A-Za-z0-9._-]+|[A-Za-z0-9._-]+\.github\.io)/worldipd-private-scaffold'
    )
    targets = list((ROOT / 'e156-submission').rglob('*'))
    targets += [ROOT / 'docs' / 'protocol.md', ROOT / 'paper' / 'manuscript.md', ROOT / 'push.sh']
    for path in targets:
        if not path.is_file():
            continue
        try:
            text = path.read_text(encoding='utf-8')
        except (UnicodeDecodeError, OSError):
            continue
        assert 'mahmood789' not in text, f'{path}: stray wrong owner mahmood789'
        assert not scaffold_url_re.search(text), f'{path}: stray scaffold-suffixed repo URL'
