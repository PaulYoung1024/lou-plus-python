import threading

def hello(name):
    print('this is child thread, thread ID:{}'.format(threading.get_ident()))
    print('Hello '+name)

def main():
    print('this is parent thread, thread ID:{}'.format(threading.get_ident()))
    print('-------------------------')
    t=threading.Thread(target=hello,args=('shiyanlou',))
    t.start()
    t.join()
    print('-------------------------')
    print('this is parent thread, thread ID:{}'.format(threading.get_ident()))

if __name__=='__main__':
    main()
