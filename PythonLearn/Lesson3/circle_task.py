from math import pi
import decimal

decimal.getcontext().prec = 43

d: int = int(input("Enter diametr: "))

print(f"""
          Radius: {d / 2}
          Area: {pi * ((d/2) ** 2)}
          Lenght: {pi * d}
      """)
