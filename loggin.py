# import logging

# logging.basicConfig(level=logging.DEBUG)
# logging.info("info")
# logging.debug("debug")
# logging.warning("warning")
# logging.error("error")
# logging.critical("criptical")


# x = 4
# y = 5
# logging.info(f"The vslues of x and y are {x} and {y}")
# try:
#     result = x/y
#     logging.info(f"x/y successful with result {result}")
# except Exception as e:
#     logging.error("Exception", exc_info=True)
#
# x_elen = [2, 3, 4, 6, 10]
# y_elen =[5, 7, 12, 0, 1]
#
# for x_e, y_e in zip(x_elen, y_elen):
#     x, y = x_e, y_e
#     logging.info(f"The values of x and y are {x} and {y}")
#     try:
#         result = x/y
#         logging.info(f"x/y successful with result {result}")
#     except ZeroDivisionError as e:
#         logging.exception("ZeroDivisionError")
#
#
#  a = zip(x_elen, y_elen)
#
#  print(tuple(a))
assert 2 + 2 == 5
def adder(*args, **kwargs):
    result = 0
    for arg in args:
        result += arg
    for value in kwargs.values():
        result += value
    return result