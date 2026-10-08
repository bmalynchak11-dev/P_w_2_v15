"""Автоматична перевірка варіанта 10."""
import pytest
from conftest import load
from kits import p02

V = load(10)
CASES = [{'id': 'роль до власної бази',
  'public': True,
  'kind': 'hba',
  'conn': 'host',
  'db': 'lms_ann',
  'user': 'lms_ann',
  'ip': '10.90.12.5',
  'ssl': False,
  'expect': 'scram-sha-256'},
 {'id': 'блокування вже є',
  'public': True,
  'kind': 'backup',
  'args': ['bk'],
  'env': {'PGDATABASE': 'lms_courses'},
  'files': {'bk/backup.lock': {'text': '4242\n'}},
  'stdout': '',
  'code': 4,
  'stderr_contains': 'Помилка: резервне копіювання вже виконується',
  'listing': {'bk': ['backup.lock']}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_variant_10(case):
    p02.check(V, case)
