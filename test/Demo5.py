from multiprocessing import Process
import time


class Test(Process):
    def run(self):
        while True:
            print("1" * 50)
            time.sleep(1)



if __name__ == '__main__':
    for i in range(5):
        t = Test()
        t.start()
