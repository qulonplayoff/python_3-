import timeit

def test_timeit_decorator():
    def test_function():
        for i in range(1000000):
            pass
    test_function()

    def test_function2():
        return sum(range(1000000))
    test_function2()

    def test_function3():
        return "hello world"
    test_function3()

test_timeit_decorator()




