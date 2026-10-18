from collections.abc import Iterator
from typing import Any


def filter_by_currency(
    transactions: list[dict[str, Any]],
    currency: str,
) -> Iterator[dict[str, Any]]:
    """Генератор транзакций по заданной валюте"""
    for transaction in transactions:
        try:
            code = transaction["operationAmount"]["currency"]["code"]
        except (KeyError, TypeError):
            continue
        if code == currency:
            yield transaction


def transaction_descriptions(
    transactions: list[dict[str, Any]],
) -> Iterator[str]:
    """Генератор описаний транзакций"""
    for transaction in transactions:
        yield str(transaction.get("description", ""))


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """Генератор номеров карт в формате XXXX XXXX XXXX XXXX"""
    for number in range(start, end + 1):
        card = f"{number:016d}"
        yield f"{card[:4]} {card[4:8]} {card[8:12]} {card[12:]}"
