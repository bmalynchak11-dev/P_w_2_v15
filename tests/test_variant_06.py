"""Автоматична перевірка варіанта 06."""
import pytest
from conftest import load
from kits import p02

V = load(6)
CASES = [{'id': 'резервна роль з адреси сервера',
  'public': True,
  'kind': 'hba',
  'conn': 'host',
  'db': 'hotel_booking',
  'user': 'hb_backup',
  'ip': '10.24.7.15',
  'ssl': False,
  'expect': 'scram-sha-256'},
 {'id': 'перша копія з сумою',
  'public': True,
  'kind': 'backup',
  'args': ['bk', '3'],
  'env': {'PGDATABASE': 'hotel_booking'},
  'now': '3000-03-15 09:30:00',
  'stdout': 'Створено: hotel_booking_30000315.dump\nOK hotel_booking_30000315.dump\nЗбережено копій: 1\n',
  'code': 0,
  'listing': {'bk': ['hotel_booking_30000315.dump', 'hotel_booking_30000315.dump.sha256']}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_variant_06(case):
    p02.check(V, case)
