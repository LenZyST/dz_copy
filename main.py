from typing import Any

from src.processing import filter_by_state, sort_by_date
from src.services import process_bank_search
from src.utils import (
    load_transactions,
    load_transactions_csv,
    load_transactions_excel,
)
from src.widget import get_date, mask_account_card


def _ask_yes_no(question: str) -> bool:
    while True:
        answer = input(question).strip().lower()
        if answer in ("да", "нет"):
            return answer == "да"
        print("Пожалуйста, введите Да или Нет")


def _get_amount(transaction: dict[str, Any]) -> str:
    if "operationAmount" in transaction:
        amount = transaction["operationAmount"]["amount"]
        code = transaction["operationAmount"]["currency"]["code"]
        if code == "RUB":
            return f"{amount} руб."
        return f"{amount} {code}"

    amount = transaction.get("amount", "")
    code = transaction.get("currency_code", "")
    if code == "RUB":
        return f"{amount} руб."
    return f"{amount} {code}".strip()


def _print_transaction(transaction: dict[str, Any]) -> None:
    date = get_date(str(transaction.get("date", "")))
    description = transaction.get("description", "")
    print(f"{date} {description}")

    from_value = transaction.get("from")
    to_value = transaction.get("to")
    if from_value and to_value:
        print(
            f"{mask_account_card(str(from_value))} -> "
            f"{mask_account_card(str(to_value))}"
        )
    elif to_value:
        print(mask_account_card(str(to_value)))

    print(f"Сумма: {_get_amount(transaction)}")
    print()


def _load_by_choice(choice: str) -> list[dict[str, Any]]:
    if choice == "1":
        print("Для обработки выбран JSON-файл.")
        return load_transactions("data/operations.json")
    if choice == "2":
        print("Для обработки выбран CSV-файл.")
        return load_transactions_csv("data/transactions.csv")
    if choice == "3":
        print("Для обработки выбран XLSX-файл.")
        return load_transactions_excel("data/transactions_excel.xlsx")
    return []


def main() -> None:  # noqa: C901
    """Основная логика работы с банковскими транзакциями"""
    print("Привет! Добро пожаловать в программу работы")
    print("с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    while True:
        choice = input().strip()
        if choice in ("1", "2", "3"):
            break
        print("Выберите пункт меню: 1, 2 или 3")

    transactions = _load_by_choice(choice)
    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши")
        print("условия фильтрации")
        return

    available_states = {"EXECUTED", "CANCELED", "PENDING"}
    while True:
        print(
            "Введите статус, по которому необходимо выполнить фильтрацию."
        )
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        state = input().strip().upper()
        if state in available_states:
            print(f'Операции отфильтрованы по статусу "{state}"')
            break
        print(f'Статус операции "{state}" недоступен.')

    transactions = filter_by_state(transactions, state)

    if _ask_yes_no("Отсортировать операции по дате? Да/Нет\n"):
        order = input(
            "Отсортировать по возрастанию или по убыванию?\n"
        ).strip().lower()
        reverse = order != "по возрастанию"
        transactions = sort_by_date(transactions, reverse=reverse)

    if _ask_yes_no("Выводить только рублевые транзакции? Да/Нет\n"):
        filtered = []
        for item in transactions:
            if "operationAmount" in item:
                code = item["operationAmount"]["currency"]["code"]
            else:
                code = str(item.get("currency_code", ""))
            if code == "RUB":
                filtered.append(item)
        transactions = filtered

    if _ask_yes_no(
        "Отфильтровать список транзакций по определенному слову "
        "в описании? Да/Нет\n"
    ):
        search = input("Введите слово для поиска:\n").strip()
        transactions = process_bank_search(transactions, search)

    print("Распечатываю итоговый список транзакций...")
    print()

    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши")
        print("условия фильтрации")
        return

    print(f"Всего банковских операций в выборке: {len(transactions)}")
    print()
    for transaction in transactions:
        _print_transaction(transaction)


if __name__ == "__main__":
    main()
