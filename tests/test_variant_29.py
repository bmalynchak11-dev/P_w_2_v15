"""Автоматична перевірка варіанта 29."""
import pytest
from conftest import load
from kits import p02

V = load(29)
CASES = [{'id': 'група кураторів',
  'public': True,
  'kind': 'sql',
  'checks': [('is_member', 'kur_anna', 'curators', True),
             ('is_member', 'kur_ivan', 'curators', True),
             ('is_member', 'museum_backup', 'curators', False),
             ('can_login', 'curators', False)]},
 {'id': 'куратор з підмережі',
  'public': True,
  'kind': 'hba',
  'conn': 'host',
  'db': 'museum',
  'user': 'kur_anna',
  'ip': '10.29.16.5',
  'ssl': False,
  'groups': {'curators': ['kur_anna', 'kur_ivan']},
  'expect': 'scram-sha-256'}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_variant_29(case):
    p02.check(V, case)
