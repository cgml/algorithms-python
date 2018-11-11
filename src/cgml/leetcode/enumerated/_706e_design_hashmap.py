import threading

class HashMap:
    def __init__(self):
        with self.lock:
            print('test')