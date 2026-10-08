"""Службовий файл варіанта 24. Не змінюйте його: ви редагуєте файли в папці variant_24/."""
from pathlib import Path

DIR = Path(__file__).resolve().parent / "variant_24"
FILES = ['backup.sh', 'init.sql', 'pg_hba.conf']
for _name in FILES:
    if "TODO: реалізуйте" in (DIR / _name).read_text(encoding="utf-8"):
        raise NotImplementedError(f"Файл {_name} (варіанта 24) ще не реалізовано: виконайте завдання за карткою і приберіть позначку TODO")
