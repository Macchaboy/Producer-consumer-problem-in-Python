import threading,queue,time,random

def product():
    global eventp,eventc,lock,data,datapt,flag
    while flag :
        delaytime = random.randint(0,5)
        time.sleep(delaytime)
        if eventp.wait():
            lock.acquire()
            if not(eventp.isSet()):
                lock.release()
                break
            nu = random.randint(0,10)
            data.put(nu)
            datapt.append(nu)
            print('生產{}'.format(datapt))
            if data.full() :
                eventp.clear()
                eventc.set()
            lock.release()

def customer():
    global eventp,eventc,lock,data,datapt,flag
    while flag :
        delaytime = random.randint(0,5)
        time.sleep(delaytime)
        if eventc.wait():
            lock.acquire()
            if not(eventc.isSet()):
                lock.release()
                break
            data.get()
            datapt.pop(0)
            print('消費{}'.format(datapt))
            if data.empty() :
                eventp.set()
                eventc.clear()
            lock.release()
def process():
    global eventp,eventc,lock,data,datapt,flag
    data = queue.Queue(5)
    datapt=[]
    lock = threading.Lock()
    eventp = threading.Event()
    eventc = threading.Event()
    eventp.set()
    eventc.clear()
    flag =True
    pin = int(input('輸入生產者數量 : '))
    cin = int(input('輸入消費者數量 : '))
    tin = int(input('輸入時間 : ')) 
    threadlist=[]
    for i in range(pin):
        p = threading.Thread(target=product)
        threadlist.append(p)
        p.setDaemon(True)
        p.start()
    for i in range(cin):
        c = threading.Thread(target=customer)
        threadlist.append(c)
        c.setDaemon(True)
        c.start()
    time.sleep(tin)
    flag = False
    print('End'+'*'*20)
    exit(0)
    for i in threadlist:
        i.join()
if __name__ == "__main__":
    process()
