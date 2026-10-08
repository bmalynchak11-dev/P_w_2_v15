"""Автоматична перевірка варіанта 23."""
import pytest
from conftest import load
from kits import p02

V = load(23)
CASES = [{'id': 'сайт зі своєї підмережі',
  'public': True,
  'kind': 'hba',
  'conn': 'host',
  'db': 'donations',
  'user': 'charity_web',
  'ip': '10.60.10.15',
  'ssl': False,
  'expect': 'scram-sha-256'},
 {'id': 'частковий збій через недопустиму назву',
  'public': True,
  'kind': 'backup',
  'args': ['backups', 'dbs.txt'],
  'env': {'PGHOST': 'db.fund.lan', 'PGUSER': 'charity_backup'},
  'files': {'dbs.txt': '# основні бази\ndonations\n\nBad-Name\ndonations_archive\n'},
  'stdout': 'OK donations\nFAIL Bad-Name\nOK donations_archive\nНевдач: 1\n',
  'code': 1,
  'stderr_contains': 'Помилка: недопустима назва бази: Bad-Name',
  'listing': {'backups': ['donations.dump', 'donations_archive.dump']}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_variant_23(case):
    p02.check(V, case)
