"""Автоматична перевірка варіанта 02."""
import pytest
from conftest import load
from kits import p02

V = load(2)
CASES = [{'id': 'TLS з підмережі',
  'public': True,
  'kind': 'hba',
  'conn': 'host',
  'db': 'gradebook',
  'user': 'shift_a',
  'ip': '192.168.30.15',
  'ssl': True,
  'expect': 'scram-sha-256'},
 {'id': 'блокування від паралельного запуску',
  'public': True,
  'kind': 'backup',
  'args': ['copies', 'may'],
  'files': {'copies/backup.lock': {'text': '777\n'}},
  'stdout': '',
  'code': 5,
  'stderr_contains': 'Помилка: копіювання вже виконується',
  'out_files': {'copies/backup.lock': '777\n'},
  'listing': {'copies': ['backup.lock']}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_variant_02(case):
    p02.check(V, case)
