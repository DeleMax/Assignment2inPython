from threading import Thread, Lock, RLock, Semaphore
import threading
import time
import random
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s (%(threadName)-2s) %(message)s',
                    )

class ActivePool(object):
    def __init__(self):
        super(ActivePool, self).__init__()
        self.active = []
        self.lock = threading.Lock()
    def makeActive(self, name):
        with self.lock:
            self.active.append(name)
    def makeInactive(self, name):
        with self.lock:
            print("")
    def randomNumber(self):
        return random.randint(0,1)
    def busyCode(self):
        time.sleep(1)
    def nonCriticalCode(self):
            time.sleep(1)
    def criticalCode(self):
            time.sleep(1)
    def write(self):
        time.sleep(1)
        
def PrintSemaphore(self, activePool):
      randomNumber = random.randint(0,1)
      with self:
          name = threading.currentThread().getName()
      if randomNumber == 0:
          for i in range(0, 2):
              print(name + " has started reading the shared resource \n")
              activePool.nonCriticalCode()
              activePool.makeInactive(name)
              print(name + " has stopped reading the shared resource \n")
      else:
          for i in range(0, 2):
              print(name + " has started writing the shared resource \n")
              activePool.write()
              activePool.makeActive(name)
              print(name + " has stopped writing the shared resource \n")

activePool = ActivePool()
s = threading.Semaphore(1)
for i in range(7):
    t = threading.Thread(target=PrintSemaphore, args=(s, activePool))
    t.start()
