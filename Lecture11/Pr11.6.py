# coding: utf8

class Queue(object):
    def __init__(self):
        self.queue = []
        return

    def insert(self, x):
        self.queue.append(x)
        return

    def remove(self):
        try:
            ret = self.queue[0]
            del self.queue[0]
        except:
            raise ValueError
        return ret
