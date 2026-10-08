"""Автоматична перевірка варіанта 08."""
import pytest
from conftest import load
from kits import p02

V = load(8)
CASES = [{'id': 'зміна вдень з SSL',
  'public': True,
  'kind': 'hba',
  'conn': 'host',
  'db': 'iot_telemetry',
  'user': 'shift_day',
  'ip': '172.20.9.50',
  'ssl': True,
  'expect': 'scram-sha-256'},
 {'id': 'перша копія',
  'public': True,
  'kind': 'backup',
  'args': [],
  'env': {'PGDATABASE': 'iot_telemetry', 'DIR': 'snap', 'KEEP': '3'},
  'now': '3000-03-15 09:30:00',
  'stdout': 'Створено: iot_telemetry-30000315-0930.dump\nЗбережено: 1\n',
  'code': 0,
  'listing': {'snap': ['iot_telemetry-30000315-0930.dump']}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_variant_08(case):
    p02.check(V, case)
