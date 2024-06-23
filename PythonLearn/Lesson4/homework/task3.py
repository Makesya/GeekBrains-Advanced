import decimal

# Кол-во знаков после запятой

MULTIPLICITY = 50
PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)
MIN_REMOVAL = decimal.Decimal(30)
MAX_REMOVAL = decimal.Decimal(600)
PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
COUNTER4PERCENTAGES = 3
RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_SUM = decimal.Decimal(10_000_000)

bank_account = decimal.Decimal(0)
count = 0
operations = []


def check_multiplicity(amount):
    if decimal.Decimal(amount) % MULTIPLICITY != 0:
        print(f"Сумма должна быть кратной {MULTIPLICITY} у.е.")
        return False
    return True


def deposit(amount):
    global bank_account
    if check_multiplicity(amount):
        bank_account += decimal.Decimal(amount)
        operations.append(
            f'Пополнение карты на {amount} у.е. Итого {bank_account} у.е.')
        return True


def withdraw(amount):
    global bank_account
    check_multiplicity(amount)
    percentWithdraw = (amount * PERCENT_REMOVAL).quantize(
        decimal.Decimal("0.00"))
    if percentWithdraw < MIN_REMOVAL:
        percentWithdraw = MIN_REMOVAL
    elif percentWithdraw > MAX_REMOVAL:
        percentWithdraw = MAX_REMOVAL
    if bank_account < amount + percentWithdraw:
        operations.append(
            f'Недостаточно средств. Сумма с комиссией {int(amount + percentWithdraw)} у.е. На карте {bank_account} у.е.')
        return False
    else:
        bank_account -= amount + percentWithdraw
        operations.append(
            f'Снятие с карты {amount} у.е. Процент за снятие {int(percentWithdraw)} у.е.. Итого {int(bank_account)} у.е.')


def exit():
    global bank_account
    if bank_account >= RICHNESS_SUM:
        per = bank_account * RICHNESS_PERCENT
        bank_account -= bank_account * RICHNESS_PERCENT
        operations.append(
            f"Вычтен налог на богатство {RICHNESS_PERCENT}% в сумме {float(per):.4f} у.е. Итого {float(bank_account):.4f} у.е.")
        if bank_account % 1 == 0:
            operations.append(f'Возьмите карту на которой {bank_account} у.е.')
        else:
            operations.append(
                f'Возьмите карту на которой {float(bank_account):.4f} у.е.')

        return True
    else:
        if bank_account % 1 == 0:
            operations.append(f'Возьмите карту на которой {bank_account} у.е.')
        else:
            operations.append(
                f'Возьмите карту на которой {float(bank_account):.4f} у.е.')
        return False


deposit(1000000000000000)
withdraw(200)
withdraw(300)
deposit(500)
withdraw(3000)
exit()

print(operations)
