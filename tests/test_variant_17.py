"""Автоматична перевірка варіанта 17."""
import pytest
from conftest import load
from kits import p02

V = load(17)
CASES = [{'id': 'учасниця форуму з мережі учасників',
  'public': True,
  'kind': 'hba',
  'conn': 'host',
  'db': 'forum',
  'user': 'anna',
  'ip': '10.20.9.15',
  'groups': {'forumers': ['anna', 'borys']},
  'expect': 'scram-sha-256'},
 {'id': 'успішна копія з журналом',
  'public': True,
  'kind': 'backup',
  'args': [],
  'env': {'PGHOST': 'db.forum.local', 'PGUSER': 'backup', 'PGDATABASE': 'forum'},
  'now': '2031-05-07 08:09:10',
  'shims': {'pg_isready': '@pg_isready', 'sleep': '@sleep'},
  'stdout': '[07.05 08:09:10] Початок: forum\n'
            '[07.05 08:09:10] Сервер доступний\n'
            '[07.05 08:09:10] Копію збережено: forum.dump\n',
  'code': 0,
  'out_files': {'dumps/backup.log': '[07.05 08:09:10] Початок: forum\n'
                                    '[07.05 08:09:10] Сервер доступний\n'
                                    '[07.05 08:09:10] Копію збережено: forum.dump\n'},
  'listing': {'dumps': ['backup.log', 'forum.dump']}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_variant_17(case):
    p02.check(V, case)
