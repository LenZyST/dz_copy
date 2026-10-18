from src.logger_setup import setup_logger

logger = setup_logger("masks")


def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера карты"""
    logger.info("Маскировка номера карты")
    result = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    logger.info("Маскировка карты выполнена успешно")
    return result


def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера счета"""
    logger.info("Маскировка номера счета")
    result = f"**{account_number[-4:]}"
    logger.info("Маскировка счета выполнена успешно")
    return result
