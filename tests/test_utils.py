import json
from pathlib import Path

from src.utils import load_transactions


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
