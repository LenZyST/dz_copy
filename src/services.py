import re
from collections import Counter
from typing import Any


def process_bank_search(
    data: list[dict[str, Any]],
    search: str,
) -> list[dict[str, Any]]:
    """Ищет операции по строке в описании"""
    pattern = re.compile(re.escape(search), re.IGNORECASE)
    return [
        item
        for item in data
        if pattern.search(str(item.get("description", "")))
    ]


def process_bank_operations(
    data: list[dict[str, Any]],
    categories: list[str],
) -> dict[str, int]:
    """Считает количество операций по категориям"""
    descriptions = [
        str(item.get("description", "")).lower() for item in data
    ]
    counter = Counter(descriptions)
    result: dict[str, int] = {}
    for category in categories:
        result[category] = counter.get(category.lower(), 0)
    return result
