"""Автоматична перевірка варіанта 21."""
import pytest
from conftest import load
from kits import p02

V = load(21)
CASES = [{'id': 'каса зі своєї підмережі',
  'public': True,
  'kind': 'hba',
  'conn': 'host',
  'db': 'parkdb',
  'user': 'cashier_anna',
  'ip': '10.20.30.7',
  'ssl': False,
  'groups': {'parking_staff': ['cashier_anna', 'cashier_ivan']},
  'expect': 'scram-sha-256'},
 {'id': 'ротація щоденних копій',
  'public': True,
  'kind': 'backup',
  'args': ['daily'],
  'env': {'PGHOST': 'db.park.lan', 'PGUSER': 'park_backup', 'PGDATABASE': 'parkdb', 'KEEP_DAILY': '3'},
  'now': '2031-03-14 03:00:00',
  'files': {'backups/parkdb-daily-20310311.dump': 'DUMP\n',
            'backups/parkdb-daily-20310312.dump': 'DUMP\n',
            'backups/parkdb-daily-20310313.dump': 'DUMP\n',
            'backups/parkdb-weekly-20310309.sql': 'SCHEMA\n'},
  'stdout': 'Створено: backups/parkdb-daily-20310314.dump\n'
            'Видалено: backups/parkdb-daily-20310311.dump\n'
            'Залишено: 3\n',
  'code': 0,
  'listing': {'backups': ['parkdb-daily-20310312.dump',
                          'parkdb-daily-20310313.dump',
                          'parkdb-daily-20310314.dump',
                          'parkdb-weekly-20310309.sql']}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_variant_21(case):
    p02.check(V, case)
