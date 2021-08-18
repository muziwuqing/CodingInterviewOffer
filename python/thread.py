import threading
import time


def task(name):
    print("这是任务" + str(name))
    time.sleep(5)


t1 = threading.Thread(name='任务线程', target=task, args=(1,))
t1.start()
t2 = threading.Thread(name='任务线程', target=task, args=(2,))
t2.start()
time.sleep(6)
print('主线程结束')
