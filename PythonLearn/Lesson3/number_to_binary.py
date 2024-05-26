
divOct: int = 8
divBin: int = 2
divHex: int = 16


def convertTo(divider: int, number: int):
    result = ""
    print(f"{bin(number), oct(number), hex(number)}")
    while number:
        result = str(number % divider) + result
        number //= divider
    return result


print(convertTo(divOct, 82))
print(convertTo(divBin, 82))
