"""Автоматична перевірка варіанта 07."""
import pytest
from conftest import load
from kits import p02

V = load(7)
CASES = [{'id': 'застосунок rw з підмережі',
  'public': True,
  'kind': 'hba',
  'conn': 'host',
  'db': 'bank_demo',
  'user': 'bank_rw',
  'ip': '10.60.4.10',
  'ssl': False,
  'expect': 'scram-sha-256'},
 {'id': 'дві бази зі списку',
  'public': True,
  'kind': 'backup',
  'args': ['bk', 'bank_demo', 'bank_audit'],
  'stdout': 'OK bank_demo\nOK bank_audit\nНевдач: 0\n',
  'code': 0,
  'listing': {'bk': ['bank_audit.dump', 'bank_demo.dump']}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_variant_07(case):
    p02.check(V, case)
