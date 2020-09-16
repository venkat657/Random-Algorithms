from queue import Queue
class MovingAverage:

    def __init__(self,average):
        self.Average=average
        self.queue=Queue(maxsize=self.Average)
        self.s=0
    def next(self,val):
        if(self.queue.qsize()<self.Average):
            self.queue.put(val)
            self.s+=val
            return self.s/self.Average if self.queue.qsize()>1 else 1
        else:
            self.s-=self.queue.get()
            self.queue.put(val)
            self.s+=val
            return self.s/self.Average

m = MovingAverage(3)
print(m.next(1))
print(m.next(10))
print(m.next(3))
print(m.next(5))
