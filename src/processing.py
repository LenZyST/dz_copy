from typing import Any


def filter_by_state(
    data: list[dict[str, Any]],
    state: str = "EXECUTED",
) -> list[dict[str, Any]]:
    """Функция фильтрации операций по статусу"""
    return [item for item in data if item.get("state") == state]


def sort_by_date(
    data: list[dict[str, Any]],
    reverse: bool = True,
) -> list[dict[str, Any]]:
    """Функция сортировки операций по дате"""
    return sorted(data, key=lambda item: str(item["date"]), reverse=reverse)
