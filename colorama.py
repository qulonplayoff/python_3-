import colorama
import inspect

def my_func(a, b=5, *args, **kwargs):
    c = a + b
    print(f"c = {c}")

func_info = inspect.getfullargspec(my_func)

# print the function name
print(f"Function name: {my_func.__name__}")

print(f"Function arguments: {func_info.args}")

print(f"Function defaults: {func_info.defaults}")

print(f"Function variable arguments: {func_info.varargs}")

print(f"Function keyword arguments: {func_info.varkw}")

print(f"Function annotations: {my_func.__annotations__}")


colorama.init()

print(colorama.Fore.RED + "This text is red" + colorama.Style.RESET_ALL)
print(colorama.Fore.GREEN + "This text is green" + colorama.Style.RESET_ALL)