"""Автоматична перевірка варіанта 09."""
import pytest
from conftest import load
from kits import p02

V = load(9)
CASES = [{'id': 'застосунок із підмережі персоналу',
  'public': True,
  'kind': 'hba',
  'conn': 'host',
  'db': 'hr_core',
  'user': 'hr_app',
  'ip': '10.80.5.7',
  'ssl': False,
  'groups': {'hr_staff': ['hr_app', 'hr_clerk']},
  'expect': 'scram-sha-256'},
 {'id': 'доступний сервер: копія й журнал',
  'public': True,
  'kind': 'backup',
  'args': ['bk'],
  'env': {'PGDATABASE': 'hr_core'},
  'now': '3000-03-15 09:30:00',
  'shims': {'pg_isready': '@pg_isready', 'sleep': '@sleep'},
  'stdout': '[3000-03-15 09:30:00] ПЕРЕВІРКА 1 з 3: доступний\n'
            '[3000-03-15 09:30:00] КОПІЮВАННЯ hr_core\n'
            '[3000-03-15 09:30:00] ГОТОВО hr_core.dump\n',
  'code': 0,
  'listing': {'bk': ['backup.log', 'hr_core.dump']}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_variant_09(case):
    p02.check(V, case)
