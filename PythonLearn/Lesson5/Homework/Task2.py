names = ["Alice", "Bob", "Charlie"]
salary = [5000, 6000, 7000]
bonus = ["10%", "5%", "15%"]


result = {name: salary[i] * float(bonus[i].strip("%")) /
          100.0 for i, name in enumerate(names)}
print(result)
