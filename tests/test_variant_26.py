"""Автоматична перевірка варіанта 26."""
import pytest
from conftest import load
from kits import p02

V = load(26)
CASES = [{'id': 'ssl з підмережі',
  'public': True,
  'kind': 'hba',
  'conn': 'host',
  'db': 'ticketing',
  'user': 'shift_a',
  'ip': '172.20.26.15',
  'ssl': True,
  'expect': 'scram-sha-256'},
 {'id': 'успішна копія',
  'public': True,
  'kind': 'backup',
  'args': ['bk'],
  'env': {'PGHOST': 'db.local', 'PGUSER': 'backup', 'PGDATABASE': 'ticketing', 'STAMP': 's01'},
  'files': {'bk/': ''},
  'stdout': 'Команда: pg_dump -Fc -f bk/ticketing-s01.dump\nКопію створено: ticketing-s01.dump\n',
  'code': 0,
  'listing': {'bk': ['ticketing-s01.dump']},
  'absent': ['bk/backup.lock']}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_variant_26(case):
    p02.check(V, case)
