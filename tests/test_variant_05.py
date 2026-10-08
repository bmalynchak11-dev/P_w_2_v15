"""Автоматична перевірка варіанта 05."""
import pytest
from conftest import load
from kits import p02

V = load(5)
CASES = [{'id': 'щоденна ротація: шоста копія',
  'public': True,
  'kind': 'backup',
  'args': ['daily', 'arch'],
  'env': {'STAMP': 'd06'},
  'files': {'arch/daily_d01.dump': {'text': 'D'},
            'arch/daily_d02.dump': {'text': 'D'},
            'arch/daily_d03.dump': {'text': 'D'},
            'arch/daily_d04.dump': {'text': 'D'},
            'arch/daily_d05.dump': {'text': 'D'}},
  'stdout': 'Створено: arch/daily_d06.dump\nВидалено: daily_d01.dump\nЗбережено: 5\n',
  'code': 0,
  'listing': {'arch': ['daily_d02.dump',
                       'daily_d03.dump',
                       'daily_d04.dump',
                       'daily_d05.dump',
                       'daily_d06.dump']}},
 {'id': 'адміністратор з мережі',
  'public': True,
  'kind': 'hba',
  'conn': 'host',
  'db': 'logistics_db',
  'user': 'logi_admin',
  'ip': '10.80.10.5',
  'ssl': False,
  'expect': 'reject'}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_variant_05(case):
    p02.check(V, case)
