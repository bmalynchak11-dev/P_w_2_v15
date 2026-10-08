"""Автоматична перевірка варіанта 03."""
import pytest
from conftest import load
from kits import p02

V = load(3)
CASES = [{'id': 'копія і видалення старих',
  'public': True,
  'kind': 'backup',
  'args': ['dumps', '14', '000004'],
  'files': {'dumps/lib_000001': {'text': 'DUMP', 'age_days': 20},
            'dumps/lib_000002': {'text': 'DUMP', 'age_days': 30},
            'dumps/lib_000003': {'text': 'DUMP', 'age_days': 3}},
  'stdout': 'Копію створено: dumps/lib_000004\n'
            'Видалено: lib_000001\n'
            'Видалено: lib_000002\n'
            'Видалено копій: 2\n',
  'code': 0,
  'listing': {'dumps': ['lib_000003', 'lib_000004']}},
 {'id': 'аналітик з єдиної адреси',
  'public': True,
  'kind': 'hba',
  'conn': 'host',
  'db': 'reports_db',
  'user': 'lib_analyst',
  'ip': '172.16.40.7',
  'ssl': False,
  'expect': 'scram-sha-256'}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_variant_03(case):
    p02.check(V, case)
