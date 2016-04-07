import threading
import time


class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True
        self.paused = True
        self.state = threading.Condition()

    def run(self):
    #    while True:
        print('foi')
        time.sleep(1)

    def stop(self):
        with self.state:
            self.stop =True

    def pause(self):
        with self.state:
            self.pause =True
            print('pausei')

    def resume(self):
        with self.state:
            print('voltei')
            self.pause =False


th = MyThread()
th.start()
time.sleep(5)

th.pause()
time.sleep(1)
print('to pausado')
time.sleep(1)
th.resume()
time.sleep(5)

th.stop()
