from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info_string: str) -> str:
    """Функция маскировки карты или счета"""
    parts = info_string.split()

    number = parts[-1]
    name = " ".join(parts[:-1])

    if name.lower() == "счет":
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    return f"{name} {masked_number}"


def get_date(date_string: str) -> str:
    """Функция преобразования даты в формат ДД.ММ.ГГГГ"""
    year = date_string[:4]
    month = date_string[5:7]
    day = date_string[8:10]

    return f"{day}.{month}.{year}"
