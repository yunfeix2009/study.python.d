import time

def clock(func):
    def clocked(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return  result
    return clocked
@clock
def test():
    print("excute...")
    time.sleep(5)
if __name__ == '__main__':
    test()