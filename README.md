# Проект для маскировки карт и сортировки операций

## Описание

Проект для домашней работы: маскировка номеров карт и счетов,
преобразование даты, фильтрация и сортировка операций.

## Установка

```bash
poetry install --with lint,dev
```

## Запуск тестов

Тесты написаны с помощью pytest.
Используются фикстуры и параметризация.

```bash
poetry run pytest
```

Проверка покрытия кода тестами:

```bash
poetry run pytest --cov=src --cov-report=term-missing
```

Покрытие должно быть не менее 80%.

## Структура

- `src/masks.py` — маскировка карты и счета
- `src/widget.py` — маскировка строки и формат даты
- `src/processing.py` — фильтр и сортировка операций
- `src/generators.py` — генераторы для работы с транзакциями
- `tests/` — тесты для всех функций

## Модуль generators

```python
from src.generators import (
    filter_by_currency,
    transaction_descriptions,
    card_number_generator,
)

transactions = [
    {
        "id": 1,
        "operationAmount": {
            "amount": "100.00",
            "currency": {"code": "USD"},
        },
        "description": "Перевод организации",
    }
]

for item in filter_by_currency(transactions, "USD"):
    print(item)

for description in transaction_descriptions(transactions):
    print(description)

for number in card_number_generator(1, 3):
    print(number)
```
