import threading ,time
exitFlag = 0
#下面这行代码要作为全局变量,要是作为局部变量,不会得到预期效果
threadLock = threading.Lock()

class myThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print('start thread:' + self.name)
        threadLock.acquire()
        print_time(self.name,self.counter,5)
        threadLock.release()
        print('exit thread:' + self.name)
def print_time(threadName,delay,counter):
        while counter:
            time.sleep(delay)
            print('{0}:{1}'.format(threadName, time.ctime(time.time())))
            counter -= 1

threads = []

thread1 = myThread(1,'thread-1',1)
thread2 = myThread(2,'thread-2',2)

thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

for i in threads:
    i.join()
print('exit main thread')
