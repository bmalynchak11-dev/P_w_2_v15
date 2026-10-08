"""Автоматична перевірка варіанта 28."""
import pytest
from conftest import load
from kits import p02

V = load(28)
CASES = [{'id': 'sameuser у дозволеній мережі',
  'public': True,
  'kind': 'hba',
  'conn': 'host',
  'db': 'rating_api',
  'user': 'rating_api',
  'ip': '10.28.5.20',
  'ssl': False,
  'expect': 'scram-sha-256'},
 {'id': 'хто може входити',
  'public': True,
  'kind': 'sql',
  'checks': [('can_login', 'rating_owner', False),
             ('can_login', 'season_admin', True),
             ('can_login', 'match_loader', True),
             ('can_login', 'fan_reader', True)]}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_variant_28(case):
    p02.check(V, case)
