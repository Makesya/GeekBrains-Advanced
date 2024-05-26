import sys

custom_int = 312
custom_float = 12.32
custom_string = "String hello"
custom_tuple = (3, 1, 2, 3, 1, 1)

print(f"""
      {custom_int.__class__.__name__} = {type(custom_int)}
      {custom_float.__class__.__name__} = {type(custom_float)}
      {custom_string.__class__.__name__} = {type(custom_string)}
      {custom_tuple.__class__.__name__} = {type(custom_tuple)}
      """)

# =======================================

data = [1, 3, 2, 'hello world', False, 3, 2]

for i, v in enumerate(data, start=1):
    checkInt = "This is integer" if isinstance(v, int) else ""
    checkStr = "This is string" if isinstance(v, str) else ""

    print(f"""
          Index: {i}
          Value: {v}
          ID: {id(v)}
          Hash: {hash(v)}
          System Size: {sys.getsizeof(v)}
          Size: {v.__sizeof__()}
          This type: {checkInt}{checkStr}
          """)
