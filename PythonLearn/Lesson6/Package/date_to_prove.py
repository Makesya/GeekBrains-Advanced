date_to_prove = input("Введите дата: ")


def is_date_correct(date_to_prove):
    try:
        day, month, year = map(int, date_to_prove.split("."))
        if year < 0:
            return False
    except ValueError:
        return False
    if (month < 1 or month > 12) or (day < 1 or day > 31):
        return False
    if month in [4, 6, 9, 11] and day == 31:
        return False
    if month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            if day > 29:
                return False
        else:
            if day > 28:
                return False
    return True


if is_date_correct(date_to_prove):
    print(True)
else:
    print(False)
