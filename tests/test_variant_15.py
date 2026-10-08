"""Автоматична перевірка варіанта 15."""
import pytest
from conftest import load
from kits import p02

V = load(15)
CASES = [{'id': 'синхронізація: сусідня адреса',
  'public': True,
  'kind': 'hba',
  'conn': 'host',
  'db': 'rental',
  'user': 'fleet_sync',
  'ip': '172.20.9.41',
  'ssl': False,
  'groups': {'staff': ['agent_lena', 'analyst']},
  'expect': 'reject'},
 {'id': 'одна копія вже існує',
  'public': True,
  'kind': 'backup',
  'args': ['bak', 'rental', 'rental_archive'],
  'env': {'STAMP': 's1'},
  'files': {'bak/rental_s1.dump': {'text': 'OLD', 'age_days': 1}},
  'stdout': 'FAIL rental\nOK rental_archive\nНевдач: 1\n',
  'code': 1,
  'stderr_contains': 'Помилка: rental: файл копії вже існує',
  'listing': {'bak': ['rental_archive_s1.dump', 'rental_s1.dump']}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_variant_15(case):
    p02.check(V, case)
