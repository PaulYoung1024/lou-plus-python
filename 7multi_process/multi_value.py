import time
from multiprocessing import Process,Value,Lock

def func(val,lock):
    for i in range(50):
        time.sleep(0.01)
        lock.acquire()
        val.value+=1
        lock.release()

if __name__=='__main__':
    val=Value('i',0)
    lock=Lock()
    procs=[Process(target=func,args=(val,lock)) for i in range(10)]
    for p in procs:
        p.start()
    for p in procs:
        p.join()
    print(val.value)
