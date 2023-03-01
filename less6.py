import inspect
import requests


# взнаєм чим є наш обєкт
print(inspect.ismodule(requests))
print(inspect.isclass(requests))
print(inspect.isawaitable(requests))

#узнаем месторасположение библиотеки
print(inspect.getmodule(requests.get))
print(inspect.getmodule(list))

class Human:
    def __init__(self, age = 32, height = 170, name="Max", ):
        self.age = age
        self.name = name
        self.height = height
        self.secondname = "Bush"


sig = inspect.signature(Human)
for parameter in sig.parameters.values():
    print(parameter.name, parameter.default)

import sys

print(sys.executable)
print(sys.version)

print(sys.platform)
print(sys.argv)

for module_name, module_path in sig.modules.items():
    print(f"{module_name} - {module_path}")


for _ in dir(__builins__):
    print(_)