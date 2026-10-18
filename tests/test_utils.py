import json
from pathlib import Path

from src.utils import (
    load_transactions,
    load_transactions_csv,
    load_transactions_excel,
)


def test_load_transactions_ok(tmp_path: Path) -> None:
    file_path = tmp_path / "operations.json"
    file_path.write_text(
        json.dumps([{"id": 1}, {"id": 2}]),
        encoding="utf-8",
    )
    assert load_transactions(str(file_path)) == [{"id": 1}, {"id": 2}]


def test_load_transactions_empty_file(tmp_path: Path) -> None:
    file_path = tmp_path / "empty.json"
    file_path.write_text("", encoding="utf-8")
    assert load_transactions(str(file_path)) == []


def test_load_transactions_not_list(tmp_path: Path) -> None:
    file_path = tmp_path / "dict.json"
    file_path.write_text(json.dumps({"a": 1}), encoding="utf-8")
    assert load_transactions(str(file_path)) == []


def test_load_transactions_missing_file() -> None:
    assert load_transactions("no_such_file.json") == []


def test_load_transactions_csv() -> None:
    result = load_transactions_csv("data/transactions.csv")
    assert isinstance(result, list)
    assert len(result) > 0
    assert "description" in result[0]


def test_load_transactions_csv_missing() -> None:
    assert load_transactions_csv("data/no_file.csv") == []


def test_load_transactions_excel() -> None:
    result = load_transactions_excel("data/transactions_excel.xlsx")
    assert isinstance(result, list)
    assert len(result) > 0


def test_load_transactions_excel_missing() -> None:
    assert load_transactions_excel("data/no_file.xlsx") == []
