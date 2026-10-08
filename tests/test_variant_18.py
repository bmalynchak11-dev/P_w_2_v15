"""Автоматична перевірка варіанта 18."""
import pytest
from conftest import load
from kits import p02

V = load(18)
CASES = [{'id': 'роль копіювання з сервера резервного копіювання',
  'public': True,
  'kind': 'hba',
  'conn': 'host',
  'db': 'wms',
  'user': 'wms_backup',
  'ip': '172.20.4.15',
  'groups': {'staff': ['keeper', 'loader']},
  'expect': 'scram-sha-256'},
 {'id': 'успішна копія без блокування',
  'public': True,
  'kind': 'backup',
  'args': [],
  'env': {'PGHOST': 'db.wms.local', 'PGUSER': 'wms_backup', 'PGDATABASE': 'wms'},
  'now': '2031-06-10 22:00:00',
  'stdout': 'Копію збережено: wms.dump\n',
  'code': 0,
  'listing': {'dumps': ['wms.dump']}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_variant_18(case):
    p02.check(V, case)
