from multiprocessing import Process,Pipe
conn1,conn2=Pipe()

def send():
    data_sent='hello shiyanlou'
    conn1.send(data_sent)
    print('Send Data:{}'.format(data_sent))

def recv():
    data_received=conn2.recv()
    print("Receive Data:{}".format(data_received))


def main():
    Process(target=send).start()
    Process(target=recv).start()

if __name__=='__main__':
    main()
