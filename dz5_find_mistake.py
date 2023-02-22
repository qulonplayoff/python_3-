# result = []
# def divider(a, b):
#  if a < b:
#  raise ValueError
#  if b > 100:
#  raise IndexError
#  return a/b
# data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8 : 4}
# for key in data:
#  res = divider(key, data[kem])
#  result.append(res)
#
# print(result)

result = []

def divider(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    if b > 100:
        raise ValueError("Value of 'b' is too large")
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, "": 15, 8: 4}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")

print(result)