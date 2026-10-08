"""Автоматична перевірка варіанта 13."""
import pytest
from conftest import load
from kits import p02

V = load(13)
CASES = [{'id': 'app_rw без SSL відхилено',
  'public': True,
  'kind': 'hba',
  'conn': 'host',
  'db': 'gymdb',
  'user': 'app_rw',
  'ip': '172.16.40.5',
  'ssl': False,
  'expect': 'reject'},
 {'id': 'щоденна копія з ротацією',
  'public': True,
  'kind': 'backup',
  'args': ['daily'],
  'env': {'DIR': 'bak', 'PGDATABASE': 'gymdb', 'STAMP': 'd3', 'KEEP_DAILY': '2'},
  'files': {'bak/daily_gymdb_d1.dump': {'text': 'x', 'age_days': 3},
            'bak/daily_gymdb_d2.dump': {'text': 'x', 'age_days': 1},
            'bak/weekly_gymdb_w1.sql': {'text': 'x', 'age_days': 30}},
  'stdout': 'OK daily bak/daily_gymdb_d3.dump\nDEL bak/daily_gymdb_d1.dump\nЗалишено: 2\n',
  'code': 0,
  'listing': {'bak': ['daily_gymdb_d2.dump', 'daily_gymdb_d3.dump', 'weekly_gymdb_w1.sql']}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_variant_13(case):
    p02.check(V, case)
