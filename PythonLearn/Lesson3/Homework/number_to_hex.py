num = 255
nnum = num

hex_str = ""
while num > 0:
    digit = num % 16
    if digit < 10:
        hex_str = chr(ord('0') + digit) + hex_str
    else:
        hex_str = chr(ord('a'.capitalize()) + digit - 10) + hex_str
    num //= 16

testnum = num

res = (f"""
Шестнадцатеричное представление числа: {hex_str}
Проверка результата: 0x{hex_str.lower()}""")

if nnum == 0:
    res += "0"

print(res)
