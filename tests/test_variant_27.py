"""Автоматична перевірка варіанта 27."""
import pytest
from conftest import load
from kits import p02

V = load(27)
CASES = [{'id': 'застосунок бачить лише свою базу',
  'public': True,
  'kind': 'sql',
  'checks': [('can_connect', 'app_meter', 'energy_app', True),
             ('can_connect', 'app_meter', 'energy_dwh', False),
             ('can_connect', 'meter_analyst', 'energy_app', True),
             ('can_connect', 'meter_analyst', 'energy_dwh', True)]},
 {'id': 'копія і видалення старих',
  'public': True,
  'kind': 'backup',
  'args': ['bk', '7'],
  'env': {'PGHOST': 'db.local', 'PGUSER': 'backup', 'PGDATABASE': 'energy_app', 'STAMP': 's03'},
  'files': {'bk/energy_app_s01': {'text': 'A', 'age_days': 9},
            'bk/energy_app_s02': {'text': 'B', 'age_days': 3},
            'bk/energy_dwh_s01': {'text': 'C', 'age_days': 20}},
  'stdout': 'Команда: pg_dump -Fd -j 2 -f bk/energy_app_s03\n'
            'Копію створено: energy_app_s03\n'
            'Видалено: energy_app_s01\n'
            'Видалено старих: 1\n',
  'code': 0,
  'listing': {'bk': ['energy_app_s02', 'energy_app_s03', 'energy_dwh_s01']}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_variant_27(case):
    p02.check(V, case)
