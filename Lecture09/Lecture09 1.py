from time import time


def timer(func):
    def funk(*args):
        start_time=time()
        func(*args)
        stop_time=time()
        print("Это заняло", stop_time-start_time, "секунд")
    return funk


@timer
def AnyFunction(t):
    import time
    time.sleep(t)

AnyFunction(5)
