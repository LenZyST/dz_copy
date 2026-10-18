import json
from typing import Any

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
