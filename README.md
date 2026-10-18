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
- `src/decorators.py` — декоратор логирования
- `src/utils.py` — загрузка транзакций из JSON
- `src/external_api.py` — конвертация валют через API
- `src/logger_setup.py` — настройка логирования
- `data/operations.json` — данные о транзакциях (JSON)
- `data/transactions.csv` — данные о транзакциях (CSV)
- `data/transactions_excel.xlsx` — данные о транзакциях (XLSX)
- `logs/` — файлы логов (masks.log, utils.log)
- `tests/` — тесты для всех функций

## Чтение CSV и XLSX

```python
from src.utils import load_transactions_csv, load_transactions_excel

csv_data = load_transactions_csv("data/transactions.csv")
xlsx_data = load_transactions_excel("data/transactions_excel.xlsx")
```

## Логирование

Модули `masks` и `utils` пишут логи в папку `logs/`.
При каждом запуске файлы логов перезаписываются.

## Настройка API

Скопируйте `.env.example` в `.env` и укажите ключ:

```bash
cp .env.example .env
```

Ключ можно получить на https://apilayer.com/exchangerates_data-api

## Модуль decorators

```python
from src.decorators import log

@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)
```

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
