def _is_leap_year(year: int) -> bool:
    """Проверяет год на високосность

    Args:
        year (int): Проверяемый год

    Returns:
        bool: Возвращает True если год високосный и False если нет
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def is_valid_date(date: str) -> bool:
    """Проверяет дату на валидность

    Args:
        date (str): Дата в формате "dd.mm.yyyy"

    Returns:
        bool: Возвращает True если дата валидна и False если нет
    """
    day, month, year = map(int, date.split("."))
    if 1 <= year <= 9999 and 1 <= month <= 12 and 1 <= day <= 31:
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 1 <= day <= 31
        elif month == 2:
            return 1 <= day <= 29 if _is_leap_year(year) else 1 <= day <= 28
        else:
            return 1 <= day <= 30
    return False


print(is_valid_date("28.02.12"))
