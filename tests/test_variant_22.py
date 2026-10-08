"""Автоматична перевірка варіанта 22."""
import pytest
from conftest import load
from kits import p02

V = load(22)
CASES = [{'id': 'гостьова мережа попри збіг назв',
  'public': True,
  'kind': 'hba',
  'conn': 'host',
  'db': 'branch_lviv',
  'user': 'branch_lviv',
  'ip': '10.50.99.20',
  'ssl': False,
  'expect': 'reject'},
 {'id': 'ротація копій із контрольними сумами',
  'public': True,
  'kind': 'backup',
  'args': [],
  'env': {'PGHOST': 'db.kino.lan', 'PGUSER': 'kino_backup', 'PGDATABASE': 'cinema', 'KEEP': '2'},
  'now': '2031-03-14 21:00:00',
  'files': {'dumps/cinema-20310312-210000.dump': 'DUMP\n',
            'dumps/cinema-20310312-210000.dump.sha256': 'sum\n',
            'dumps/cinema-20310313-210000.dump': 'DUMP\n',
            'dumps/cinema-20310313-210000.dump.sha256': 'sum\n'},
  'stdout': 'Створено: dumps/cinema-20310314-210000.dump\n'
            'Контрольна сума: dumps/cinema-20310314-210000.dump.sha256\n'
            'Видалено: dumps/cinema-20310312-210000.dump\n'
            'Залишено: 2\n',
  'code': 0,
  'listing': {'dumps': ['cinema-20310313-210000.dump',
                        'cinema-20310313-210000.dump.sha256',
                        'cinema-20310314-210000.dump',
                        'cinema-20310314-210000.dump.sha256']}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_variant_22(case):
    p02.check(V, case)
