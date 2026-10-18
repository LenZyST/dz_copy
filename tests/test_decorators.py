from pathlib import Path

import pytest

from src.decorators import log


def test_log_success_console(capsys: pytest.CaptureFixture[str]) -> None:
    @log()
    def add(x: int, y: int) -> int:
        return x + y

    assert add(1, 2) == 3
    captured = capsys.readouterr()
    assert captured.out.strip() == "add ok"


def test_log_success_file(tmp_path: Path) -> None:
    log_file = tmp_path / "mylog.txt"

    @log(filename=str(log_file))
    def add(x: int, y: int) -> int:
        return x + y

    add(1, 2)
    assert log_file.read_text(encoding="utf-8").strip() == "add ok"


def test_log_error_console(capsys: pytest.CaptureFixture[str]) -> None:
    @log()
    def broken(x: int, y: int) -> int:
        return x + y

    with pytest.raises(TypeError):
        broken(1, "a")  # type: ignore[arg-type]

    captured = capsys.readouterr()
    assert "broken error: TypeError" in captured.out
    assert "Inputs: (1, 'a'), {}" in captured.out


def test_log_error_file(tmp_path: Path) -> None:
    log_file = tmp_path / "mylog.txt"

    @log(filename=str(log_file))
    def broken(x: int, y: int) -> int:
        return x + y

    with pytest.raises(TypeError):
        broken(1, "a")  # type: ignore[arg-type]

    content = log_file.read_text(encoding="utf-8")
    assert "broken error: TypeError" in content
