"""Автоматична перевірка варіанта 12."""
import pytest
from conftest import load
from kits import p02

V = load(12)
CASES = [{'id': 'сервер бекапів до своєї бази',
  'public': True,
  'kind': 'hba',
  'conn': 'host',
  'db': 'bistro',
  'user': 'rest_backup',
  'ip': '192.168.50.14',
  'ssl': False,
  'expect': 'scram-sha-256'},
 {'id': 'ротація до двох копій',
  'public': True,
  'kind': 'backup',
  'args': [],
  'env': {'DIR': 'bak', 'PGDATABASE': 'bistro', 'KEEP': '2', 'STAMP': 'n1'},
  'files': {'bak/bistro_a1.sql.gz': {'text': 'x', 'age_days': 3},
            'bak/bistro_a2.sql.gz': {'text': 'x', 'age_days': 1}},
  'stdout': 'Створено: bak/bistro_n1.sql.gz\nВидалено: bak/bistro_a1.sql.gz\nЗалишено копій: 2\n',
  'code': 0,
  'listing': {'bak': ['bistro_a2.sql.gz', 'bistro_n1.sql.gz']}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_variant_12(case):
    p02.check(V, case)
