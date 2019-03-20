import os,time,random
from multiprocessing import Pool

def task(name):
    #print process pid
    print('task {} starting, pid:{}'.format(name,os.getpid()))
    start_time=time.time()
    time.sleep(random.random()*3)
    end_time=time.time()
    print('task {} ends, time consumed:{:.2f}'.format(name,end_time-start_time))

if __name__=='__main__':
    print('this is main process, pid:{}'.format(os.getpid()))
    print('--------------------------------')
    #create process pool
    p=Pool(4)
    for i in range(1,6):
        p.apply_async(task,args=(i,))
    p.close()
    print('child process starting...')
    p.join()
    print('--------------------------------')
    print('all child processes finished, now main process: pid{}'.format(os.getpid()))
