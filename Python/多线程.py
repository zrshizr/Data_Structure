# import threading
# import time
# from threading import current_thread 
# def thread_job():
#     print('T1_stra\n')
#     for i in range(10):
#         print(i)
#         time.sleep(0.1)
#     print('T1 finisha\n')
# def T2_job():
#     print('T2_staret\n')
#     print('T2 finish\n')
# def main():
#     add_thread = threading.Thread(target=thread_job,name='T1')
#     T2_add = threading.Thread(target=T2_job,name='T2')
#     add_thread.start()#开始运算
#     T2_add.start()
#     add_thread.join()
#     print('all done\n')
#     # print((threading.active_count()))
#     # print(threading.enumerate())
#     # print(threading.current_thread())

# if __name__ == '__main__':
#     main()
import threading
import time
from queue import Queue

def job(l,q):
    for i in range(len(l)):
        l[i] = l[i]**2
    q.put(l) 
def multithreading(data):#data =[[1,2,3],[4,5,6],[4,4,4],[5,5,5]]
    q = Queue() #放入计算出来返回值
    threads = [] # 线程放这里面 
    for i in range(4):#object
        t = threading.Thread(target=job,args=(data[i],q)) #传入data和q
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    result =[]
    for _ in range(4):
        result.append(q.get())
    print(result)

if __name__ == '__main__':
    l =[[1,2,3],[4,5,6],[4,4,4],[5,5,5]]
    multithreading(l)
  