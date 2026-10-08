"""Автоматична перевірка варіанта 25."""
import pytest
from conftest import load
from kits import p02

V = load(25)
CASES = [{'id': 'застосунок із підмережі',
  'public': True,
  'kind': 'hba',
  'conn': 'host',
  'db': 'pharmdb',
  'user': 'pharm_app',
  'ip': '10.70.5.70',
  'ssl': False,
  'expect': 'scram-sha-256'},
 {'id': 'сервер недоступний: повтори й журнал',
  'public': True,
  'kind': 'backup',
  'args': [],
  'env': {'PGHOST': 'db.apteka.lan',
          'PGUSER': 'pharm_backup',
          'PGDATABASE': 'pharmdb',
          'DB_DOWN': '1',
          'TRIES': '2',
          'DELAY': '1'},
  'now': '2031-03-14 02:00:00',
  'shims': {'pg_isready': '@pg_isready', 'sleep': '@sleep'},
  'stdout': '20310314-020000 Перевірка сервера: спроба 1 з 2\n'
            '20310314-020000 Сервер недоступний, повтор через 1 с\n'
            '20310314-020000 Перевірка сервера: спроба 2 з 2\n',
  'code': 5,
  'stderr_contains': '20310314-020000 Помилка: сервер недоступний після 2 спроб',
  'out_files': {'copies/backup.log': '20310314-020000 Перевірка сервера: спроба 1 з 2\n'
                                     '20310314-020000 Сервер недоступний, повтор через 1 с\n'
                                     '20310314-020000 Перевірка сервера: спроба 2 з 2\n'
                                     '20310314-020000 Помилка: сервер недоступний після 2 спроб\n'},
  'listing': {'copies': ['backup.log']}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_variant_25(case):
    p02.check(V, case)
