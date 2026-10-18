import pytest

from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)


@pytest.mark.parametrize(
    "currency, expected_count",
    [
        ("USD", 2),
        ("RUB", 2),
        ("EUR", 0),
    ],
)
def test_filter_by_currency(
    sample_transactions: list[dict[str, object]],
    currency: str,
    expected_count: int,
) -> None:
    result = list(filter_by_currency(sample_transactions, currency))
    assert len(result) == expected_count
    for item in result:
        assert item["operationAmount"]["currency"]["code"] == currency


def test_filter_by_currency_iterator(
    sample_transactions: list[dict[str, object]],
) -> None:
    result = filter_by_currency(sample_transactions, "USD")
    assert next(result)["id"] == 1
    assert next(result)["id"] == 2
    with pytest.raises(StopIteration):
        next(result)


def test_transaction_descriptions(
    sample_transactions: list[dict[str, object]],
) -> None:
    result = list(transaction_descriptions(sample_transactions))
    assert result == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод с карты на счет",
        "Открытие вклада",
    ]


@pytest.mark.parametrize(
    "start, end, expected",
    [
        (1, 3, [
            "0000 0000 0000 0001",
            "0000 0000 0000 0002",
            "0000 0000 0000 0003",
        ]),
        (9999999999999998, 9999999999999999, [
            "9999 9999 9999 9998",
            "9999 9999 9999 9999",
        ]),
    ],
)
def test_card_number_generator(
    start: int,
    end: int,
    expected: list[str],
) -> None:
    assert list(card_number_generator(start, end)) == expected
