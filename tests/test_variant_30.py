"""Автоматична перевірка варіанта 30."""
import pytest
from conftest import load
from kits import p02

V = load(30)
CASES = [{'id': 'копія з контрольною сумою',
  'public': True,
  'kind': 'backup',
  'args': ['bk'],
  'env': {'PGHOST': 'db.local', 'PGUSER': 'backup', 'PGDATABASE': 'appeals', 'STAMP': 's01'},
  'files': {'bk/': ''},
  'stdout': 'Команда: pg_dump -Fc -f bk/appeals-s01.dump\n'
            'Копію створено: appeals-s01.dump\n'
            'Контрольну суму записано: appeals-s01.dump.sha256\n'
            'Залишено копій: 1\n',
  'code': 0,
  'listing': {'bk': ['appeals-s01.dump', 'appeals-s01.dump.sha256']}},
 {'id': 'доступ до бази appeals',
  'public': True,
  'kind': 'sql',
  'checks': [('can_connect', 'appeals_app', 'appeals', True),
             ('can_connect', 'appeals_auditor', 'appeals', True),
             ('can_connect', 'city_backup', 'appeals', True),
             ('can_connect', 'guest_clerk', 'appeals', False)]}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_variant_30(case):
    p02.check(V, case)
