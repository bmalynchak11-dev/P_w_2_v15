"""Автоматична перевірка варіанта 14."""
import pytest
from conftest import load
from kits import p02

V = load(14)
CASES = [{'id': 'без SSL відхилено',
  'public': True,
  'kind': 'hba',
  'conn': 'host',
  'db': 'estate',
  'user': 'shift_a',
  'ip': '10.77.8.15',
  'ssl': False,
  'expect': 'reject'},
 {'id': 'копія, сума і ротація до однієї',
  'public': True,
  'kind': 'backup',
  'args': ['estate', 'bak', '1'],
  'env': {'STAMP': 's2'},
  'files': {'bak/estate_s1.dump': {'text': 'x', 'age_days': 2},
            'bak/estate_s1.dump.sha256': {'text': 'x', 'age_days': 2}},
  'stdout': 'Створено: bak/estate_s2.dump\nВидалено: bak/estate_s1.dump\nЗалишено: 1\n',
  'code': 0,
  'listing': {'bak': ['estate_s2.dump', 'estate_s2.dump.sha256']}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_variant_14(case):
    p02.check(V, case)
