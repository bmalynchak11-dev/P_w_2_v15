"""Автоматична перевірка варіанта 16."""
import pytest
from conftest import load
from kits import p02

V = load(16)
CASES = [{'id': 'дозвіл для учасника групи',
  'public': True,
  'kind': 'hba',
  'conn': 'host',
  'db': 'newsdesk',
  'user': 'reporter',
  'ip': '10.66.2.7',
  'groups': {'newsroom': ['reporter', 'editor']},
  'expect': 'scram-sha-256'},
 {'id': 'ротація видаляє найстаріші',
  'public': True,
  'kind': 'backup',
  'args': [],
  'env': {'PGHOST': 'db.news.local', 'PGUSER': 'backup', 'PGDATABASE': 'newsdesk'},
  'now': '2031-03-05 14:30:00',
  'files': {'copies/newsdesk-20310301-0200.dump': 'DUMP',
            'copies/newsdesk-20310302-0200.dump': 'DUMP',
            'copies/newsdesk-20310303-0200.dump': 'DUMP',
            'copies/newsdesk-20310304-0200.dump': 'DUMP'},
  'stdout': 'Копію створено: newsdesk-20310305-1430.dump\n'
            'Видалено: newsdesk-20310301-0200.dump\n'
            'Збережено: 4\n',
  'code': 0,
  'listing': {'copies': ['newsdesk-20310302-0200.dump',
                         'newsdesk-20310303-0200.dump',
                         'newsdesk-20310304-0200.dump',
                         'newsdesk-20310305-1430.dump']}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_variant_16(case):
    p02.check(V, case)
