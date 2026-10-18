from unittest.mock import MagicMock, patch

import pytest

from src.external_api import convert_to_rub


def test_convert_rub() -> None:
    transaction = {
        "operationAmount": {
            "amount": "100.50",
            "currency": {"code": "RUB"},
        }
    }
    assert convert_to_rub(transaction) == 100.50


@patch("src.external_api.requests.get")
@patch.dict("os.environ", {"EXCHANGE_RATES_API_KEY": "test_key"})
def test_convert_usd(mock_get: MagicMock) -> None:
    mock_get.return_value.json.return_value = {
        "success": True,
        "result": 9000.0,
    }
    transaction = {
        "operationAmount": {
            "amount": "100.00",
            "currency": {"code": "USD"},
        }
    }
    assert convert_to_rub(transaction) == 9000.0


@patch.dict("os.environ", {}, clear=True)
def test_convert_without_api_key() -> None:
    transaction = {
        "operationAmount": {
            "amount": "100.00",
            "currency": {"code": "USD"},
        }
    }
    with pytest.raises(ValueError):
        convert_to_rub(transaction)
