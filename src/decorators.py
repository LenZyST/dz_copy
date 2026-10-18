import functools
from collections.abc import Callable
from typing import Any


def log(filename: str | None = None) -> Callable[..., Any]:
    """Декоратор для логирования работы функции"""

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
            except Exception as error:
                message = (
                    f"{func.__name__} error: {type(error).__name__}. "
                    f"Inputs: {args}, {kwargs}"
                )
                _write_log(message, filename)
                raise
            else:
                message = f"{func.__name__} ok"
                _write_log(message, filename)
                return result

        return wrapper

    return decorator


def _write_log(message: str, filename: str | None) -> None:
    """Записывает лог в файл или выводит в консоль"""
    if filename:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(message + "\n")
    else:
        print(message)
