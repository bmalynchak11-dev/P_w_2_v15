"""Автоматична перевірка варіанта 04."""
import pytest
from conftest import load
from kits import p02

V = load(4)
CASES = [{'id': 'ротація при N=3',
  'public': True,
  'kind': 'backup',
  'args': ['arch', '3'],
  'files': {'arch/clinic_db.sql.gz': {'text': 'OLDA'}, 'arch/clinic_db.sql.1.gz': {'text': 'OLDB'}},
  'stdout': 'Створено: arch/clinic_db.sql.gz\n',
  'code': 0,
  'out_files': {'arch/clinic_db.sql.1.gz': 'OLDA', 'arch/clinic_db.sql.2.gz': 'OLDB'},
  'listing': {'arch': ['clinic_db.sql.1.gz', 'clinic_db.sql.2.gz', 'clinic_db.sql.gz']}},
 {'id': 'права reception на appointments',
  'public': True,
  'kind': 'sql',
  'checks': [('table_priv', 'reception', 'clinic_db', 'appointments', 'select', True),
             ('table_priv', 'reception', 'clinic_db', 'appointments', 'insert', False)]}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_variant_04(case):
    p02.check(V, case)
