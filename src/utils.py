import json
from pathlib import Path
from typing import Any

import pandas as pd

from src.logger_setup import setup_logger

logger = setup_logger("utils")


def load_transactions(file_path: str) -> list[dict[str, Any]]:
    """Загружает список транзакций из JSON-файла"""
    logger.info("Загрузка транзакций из файла %s", file_path)
    try:
        with open(file_path, encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        logger.error("Файл не найден: %s", file_path)
        return []
    except (json.JSONDecodeError, OSError) as error:
        logger.error("Ошибка чтения файла %s: %s", file_path, error)
        return []

    if not isinstance(data, list):
        logger.warning("Файл %s не содержит список", file_path)
        return []

    logger.info("Загружено транзакций: %s", len(data))
    return data


def load_transactions_csv(file_path: str) -> list[dict[str, Any]]:
    """Загружает список транзакций из CSV-файла"""
    logger.info("Загрузка транзакций из CSV: %s", file_path)
    if not Path(file_path).exists():
        logger.error("Файл не найден: %s", file_path)
        return []

    try:
        dataframe = pd.read_csv(file_path, sep=";")
        data = dataframe.to_dict(orient="records")
    except Exception as error:
        logger.error("Ошибка чтения CSV %s: %s", file_path, error)
        return []

    logger.info("Загружено из CSV: %s", len(data))
    return list(data)


def load_transactions_excel(file_path: str) -> list[dict[str, Any]]:
    """Загружает список транзакций из XLSX-файла"""
    logger.info("Загрузка транзакций из XLSX: %s", file_path)
    if not Path(file_path).exists():
        logger.error("Файл не найден: %s", file_path)
        return []

    try:
        dataframe = pd.read_excel(file_path)
        data = dataframe.to_dict(orient="records")
    except Exception as error:
        logger.error("Ошибка чтения XLSX %s: %s", file_path, error)
        return []

    logger.info("Загружено из XLSX: %s", len(data))
    return list(data)
