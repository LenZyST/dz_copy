from src.services import process_bank_operations, process_bank_search


def test_process_bank_search() -> None:
    data = [
        {"description": "Перевод организации"},
        {"description": "Открытие вклада"},
        {"description": "перевод с карты на карту"},
    ]
    result = process_bank_search(data, "перевод")
    assert len(result) == 2


def test_process_bank_search_empty() -> None:
    data = [{"description": "Открытие вклада"}]
    assert process_bank_search(data, "перевод") == []


def test_process_bank_operations() -> None:
    data = [
        {"description": "Перевод организации"},
        {"description": "Открытие вклада"},
        {"description": "Перевод организации"},
    ]
    result = process_bank_operations(
        data,
        ["Перевод организации", "Открытие вклада", "Перевод с карты"],
    )
    assert result["Перевод организации"] == 2
    assert result["Открытие вклада"] == 1
    assert result["Перевод с карты"] == 0
