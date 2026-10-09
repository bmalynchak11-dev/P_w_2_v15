#!/usr/bin/env bash

# Перевірка кількості аргументів (правило 10)
if [ "$#" -lt 2 ]; then
    echo "Використання: backup.sh КАТАЛОГ БАЗА [БАЗА...]" >&2
    exit 100
fi

DIR="$1"
shift
DATABASES=("$@")

# Перевірка каталогу (правило 11)
if [ ! -d "$DIR" ]; then
    echo "Помилка: каталог не існує" >&2
    exit 101
fi

# Мітка часу STAMP (правило 12)
if [ -z "$STAMP" ]; then
    STAMP=$(date +%Y%m%d_%H%M%S)
fi

failures=0

# Обробка кожної бази зі списку (правила 12-17)
for db in "${DATABASES[@]}"; do
    target_file="${DIR}/${db}_${STAMP}.dump"

    # Якщо файл уже існує (правило 13)
    if [ -e "$target_file" ]; then
        echo "FAIL $db"
        echo "Помилка: $db: файл копії вже існує" >&2
        failures=$((failures + 1))
        continue
    fi

    # Виконання pg_dump (правило 14)
    if ! pg_dump -Fc -f "$target_file" "$db" >/dev/null 2>&1; then
        rm -f "$target_file"
        echo "FAIL $db"
        echo "Помилка: $db: pg_dump завершився з помилкою" >&2
        failures=$((failures + 1))
        continue
    fi

    # Перевірка через pg_restore -l (правило 15)
    if ! pg_restore -l "$target_file" >/dev/null 2>&1; then
        rm -f "$target_file"
        echo "FAIL $db"
        echo "Помилка: $db: копія не пройшла перевірку" >&2
        failures=$((failures + 1))
        continue
    fi

    # Успішне створення та перевірка (правило 16)
    echo "OK $db"
done

# Підсумок (правило 18)
echo "Невдач: $failures"
exit "$failures"