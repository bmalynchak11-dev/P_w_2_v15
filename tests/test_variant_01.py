"""Автоматична перевірка варіанта 01."""
import pytest
from conftest import load
from kits import p02

V = load(1)
CASES = [{'id': 'остання адреса підмережі',
  'public': True,
  'kind': 'hba',
  'conn': 'host',
  'db': 'shopdb',
  'user': 'shop_ro',
  'ip': '10.40.8.63',
  'ssl': False,
  'expect': 'scram-sha-256'},
 {'id': 'успішна копія',
  'public': True,
  'kind': 'backup',
  'args': [],
  'env': {'PGHOST': 'db.shop.local', 'PGUSER': 'shop_backup', 'PGDATABASE': 'shopdb', 'STAMP': '02:00:00'},
  'shims': {'pg_isready': '@pg_isready', 'sleep': '@sleep'},
  'stdout': '[02:00:00] Початок: shopdb\n'
            '[02:00:00] Копію створено: backups/shopdb.dump\n'
            '[02:00:00] Перевірку пройдено\n',
  'code': 0,
  'out_files': {'backups/backup.log': '[02:00:00] Початок: shopdb\n'
                                      '[02:00:00] Копію створено: backups/shopdb.dump\n'
                                      '[02:00:00] Перевірку пройдено\n'},
  'listing': {'backups': ['backup.log', 'shopdb.dump']}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_variant_01(case):
    p02.check(V, case)
