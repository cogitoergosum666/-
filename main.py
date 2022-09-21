import threading

global rcount,wcount
rcount = 0
wcount = 0

rmutex = threading.Semaphore(value=1)
wmutex = threading.Semaphore(value=1)
S = threading.Semaphore(value=1)
mutex = threading.Semaphore(value=1)


def reader():
    global rcount
    while True:
        S.acquire()
        rmutex.acquire()
        if rcount == 0:
            wmutex.acquire()
        rcount = rcount + 1
        rmutex.release()
        S.release()
        """
        临界区操作
        """
        print("hi,i am a reader \n")
        rmutex.acquire()
        rcount = rcount - 1
        if rcount == 0:
            wmutex.release()
        rmutex.release()

def writer():
    global wcount
    while True:
        mutex.acquire()
        if wcount == 0:
            S.acquire()
        wcount = wcount + 1
        mutex.release()

        wmutex.acquire()
        """
        临界区操作
        """
        wmutex.release()

        mutex.acquire()
        wcount = wcount - 1
        if wcount == 0:
            S.release()
        mutex.release()

if __name__ == '__main__':

    p1 = threading.Thread(target=reader)
    p2 = threading.Thread(target=writer)
    p1.start()
    p2.start()