"""Автоматична перевірка варіанта 20."""
import pytest
from conftest import load
from kits import p02

V = load(20)
CASES = [{'id': 'зміна через SSL з підмережі',
  'public': True,
  'kind': 'hba',
  'conn': 'host',
  'db': 'admissions',
  'user': 'shift_a',
  'ip': '10.90.20.5',
  'ssl': True,
  'expect': 'scram-sha-256'},
 {'id': 'ротація стиснених копій',
  'public': True,
  'kind': 'backup',
  'args': [],
  'env': {'PGHOST': 'db.admissions.local', 'PGUSER': 'backup', 'PGDATABASE': 'admissions'},
  'now': '2031-09-02 03:15:00',
  'files': {'sql_copies/admissions-20310830.sql.gz': 'GZ',
            'sql_copies/admissions-20310831.sql.gz': 'GZ',
            'sql_copies/admissions-20310901.sql.gz': 'GZ'},
  'stdout': 'Копію створено: admissions-20310902.sql.gz\n'
            'Видалено: admissions-20310830.sql.gz\n'
            'Залишилось копій: 3\n',
  'code': 0,
  'listing': {'sql_copies': ['admissions-20310831.sql.gz',
                             'admissions-20310901.sql.gz',
                             'admissions-20310902.sql.gz']},
  'shim_calls': ['pg_dump -Fp']}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_variant_20(case):
    p02.check(V, case)
