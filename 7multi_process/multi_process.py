import time 
from multiprocessing import Process

def io_task():
    time.sleep(1)
def main():
    start_time=time.time()
    '''
    for i in range(5):
        io_task()
    '''
    #child task list
    process_list=[]
    for i in range(5):
        process_list.append(Process(target=io_task))
    #start all child process
    for process in process_list:
        process.start()

    for process in process_list:
        process.join()
    end_time=time.time()
    print("program run time:{:.2f}".format(end_time-start_time))
if __name__=='__main__':
    main()
