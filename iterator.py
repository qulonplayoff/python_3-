# В Python итератор (iterator) - это объект, который реализует методы iter() и next(),
# позволяющие последовательно получать следующий элемент из некоторой коллекции или последовательности.

# a = [2, 3 ,4 ,5]
#
# iterator = iter(a)
#
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# class Couter:
#     def __init__(self):
#         self.i = 0
#         self.max_number = max_number
#
#     def __iter__(self):
#         return self
#
#     def __iter__(self):
#         self.i += 1
#         if self.i > self.max.number:
#             raise StopIteration
#         return self.i
#
#
# count = Couter(5)
#
# # for i in count:
# #     print(i)
#
# print(count.__iter__())
# print(count.__iter__())
# print(next(count))

# def generator(number, max_degree):
#     i = 0
#     for _ in range(max_degree):
#         yield number**i
#         i += 1
#
# res = generator(124, 100)
# print(res)
# for i in res:
#     print(i


#
# def generator(number):
#     i = 0
#     while True:
#         yield number ** i
#         i += 1
#
# res = generator(12345)
# for i in res:
#     print(i)


def decorator(func):
    def wrapper(*args, **kwargs)
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            print(f"We have problem {e}")
        else:
            print(f"No problem {result}")
    return wrapper

@decorator
def calculate(expression):
    result eval(expression)

calculate("2 + 2")