"""Автоматична перевірка варіанта 19."""
import pytest
from conftest import load
from kits import p02

V = load(19)
CASES = [{'id': 'застосунок з виділеної підмережі',
  'public': True,
  'kind': 'hba',
  'conn': 'host',
  'db': 'farmdb',
  'user': 'app_rw',
  'ip': '192.168.50.70',
  'expect': 'scram-sha-256'},
 {'id': 'копія й видалення старих',
  'public': True,
  'kind': 'backup',
  'args': [],
  'env': {'PGHOST': 'db.farm.local', 'PGUSER': 'backup', 'PGDATABASE': 'farmdb'},
  'now': '2031-03-05 14:30:00',
  'files': {'farm_copies/farmdb-0201-0300': {'text': 'DUMP', 'age_days': 30},
            'farm_copies/farmdb-0225-0300': {'text': 'DUMP', 'age_days': 22},
            'farm_copies/farmdb-0301-0300': {'text': 'DUMP', 'age_days': 4}},
  'stdout': 'Копію створено: farmdb-0305-1430\n'
            'Видалено: farmdb-0201-0300\n'
            'Видалено: farmdb-0225-0300\n'
            'Видалено копій: 2\n',
  'code': 0,
  'listing': {'farm_copies': ['farmdb-0301-0300', 'farmdb-0305-1430']}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_variant_19(case):
    p02.check(V, case)
