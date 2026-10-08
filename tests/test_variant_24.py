"""Автоматична перевірка варіанта 24."""
import pytest
from conftest import load
from kits import p02

V = load(24)
CASES = [{'id': 'сервер копіювання зі своєї адреси',
  'public': True,
  'kind': 'hba',
  'conn': 'host',
  'db': 'eventsdb',
  'user': 'events_backup',
  'ip': '192.168.40.15',
  'ssl': False,
  'expect': 'scram-sha-256'},
 {'id': 'ротація за іменем із чужими файлами',
  'public': True,
  'kind': 'backup',
  'args': ['copies', '3'],
  'env': {'PGHOST': 'db.events.lan', 'PGUSER': 'events_backup', 'PGDATABASE': 'eventsdb'},
  'now': '2031-03-14 18:45:00',
  'files': {'copies/crm-20310301-0000.dump': 'DUMP\n',
            'copies/eventsdb-20310312-1845.dump': 'DUMP\n',
            'copies/eventsdb-20310313-1845.dump': 'DUMP\n',
            'copies/eventsdb-20310314-0300.dump': 'DUMP\n',
            'copies/eventsdb-latest.dump': 'DUMP\n'},
  'stdout': 'Збережено: copies/eventsdb-20310314-1845.dump\n'
            'Видалено: copies/eventsdb-20310312-1845.dump\n'
            'Усього копій: 3\n',
  'code': 0,
  'listing': {'copies': ['crm-20310301-0000.dump',
                         'eventsdb-20310313-1845.dump',
                         'eventsdb-20310314-0300.dump',
                         'eventsdb-20310314-1845.dump',
                         'eventsdb-latest.dump']}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_variant_24(case):
    p02.check(V, case)
