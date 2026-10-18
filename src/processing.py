def filter_by_state(
    data: list[dict[str, int | str]],
    state: str = "EXECUTED",
) -> list[dict[str, int | str]]:
    """Функция фильтрации операций по статусу"""
    return [item for item in data if item.get("state") == state]


def sort_by_date(
    data: list[dict[str, int | str]],
    reverse: bool = True,
) -> list[dict[str, int | str]]:
    """Функция сортировки операций по дате"""
    return sorted(data, key=lambda item: item["date"], reverse=reverse)
