import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api.apilayer.com/exchangerates_data/convert"


def convert_to_rub(transaction: dict[str, Any]) -> float:
    """Возвращает сумму транзакции в рублях"""
    amount_info = transaction["operationAmount"]
    amount = float(amount_info["amount"])
    currency = amount_info["currency"]["code"]

    if currency == "RUB":
        return amount

    if currency in ("USD", "EUR"):
        api_key = os.getenv("EXCHANGE_RATES_API_KEY")
        if not api_key:
            raise ValueError("EXCHANGE_RATES_API_KEY не задан в .env")

        response = requests.get(
            API_URL,
            headers={"apikey": api_key},
            params={"from": currency, "to": "RUB", "amount": amount},
            timeout=10,
        )
        data = response.json()
        if not data.get("success"):
            raise ValueError("Ошибка API при конвертации валюты")
        return float(data["result"])

    raise ValueError(f"Неподдерживаемая валюта: {currency}")
