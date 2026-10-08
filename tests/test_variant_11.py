"""Автоматична перевірка варіанта 11."""
import pytest
from conftest import load
from kits import p02

V = load(11)
CASES = [{'id': 'зламаний термінал',
  'public': True,
  'kind': 'hba',
  'conn': 'host',
  'db': 'ticketing',
  'user': 'tk_report',
  'ip': '10.30.17.99',
  'ssl': False,
  'groups': {'cashiers': ['cashier_anna', 'cashier_ivan']},
  'expect': 'reject'},
 {'id': 'копія та ротація за замовчуванням',
  'public': True,
  'kind': 'backup',
  'args': ['bak'],
  'env': {'PGDATABASE': 'ticketing', 'STAMP': 's1'},
  'files': {'bak/ticketing_old1': {'text': 'x', 'age_days': 20},
            'bak/ticketing_old2': {'text': 'x', 'age_days': 5}},
  'stdout': 'Створено: bak/ticketing_s1\nВидалено: bak/ticketing_old1\nВидалено копій: 1\n',
  'code': 0,
  'listing': {'bak': ['ticketing_old2', 'ticketing_s1']}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_variant_11(case):
    p02.check(V, case)
