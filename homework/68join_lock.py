# 主线程和子线程
# 1主线程结束,子线程可以正常运行         默认
# 2主线程和子线程同时结束(守护线程)      开启线程前 setDaemon()
# 3子线程都结束后,主线程才结束           开启线程后 join()



# 互斥锁




# 主线程与子线程：
# 当程序启动时,一个线程立刻运行,该线程就是主线程（MainThread）
import threading 
# current_thread()获取当前线程
# print('当前线程的名字是',threading.current_thread().name)

# 主线程产生其他子线程
import threading
import time
def run():
    time.sleep(2)
    print('当前线程的名字是',threading.current_thread().name)
    time.sleep(2)
# print('主线程开始:',threading.current_thread().name)
# t1=threading.Thread(target=run)
# t1.start()
# t2=threading.Thread(target=run)
# t2.start()


# 主线程结束,其他线程可以正常运行(默认)
import threading
import time
def run():
    time.sleep(2)
    print('当前线程的名字是',threading.current_thread().name)
    time.sleep(2)
# print('主线程开始:',threading.current_thread().name)
# start_time=time.time()
# threadlist=[]
# for i in range(5):#创建5个线程
#     t=threading.Thread(target=run)
#     threadlist.append(t)
# for t in threadlist:#依次开启五个线程
#     t.start()
# print('主线程结束:',threading.current_thread().name,"用时:",time.time()-start_time)


# 守护线程
# 作用：守护线程会跟随主线程一起结束
# 设置：在线程开启前setDaemon(True)
# #[ˈdiːmən]

# 主线程和子线程同时结束(守护线程)
import threading
import time
def run():
    time.sleep(2)
    print('当前线程的名字是',threading.current_thread().name)
    time.sleep(2)
# print('主线程开始:',threading.current_thread().name)
# start_time=time.time()
# threadlist=[]
# for i in range(5):
#     t=threading.Thread(target=run)
#     threadlist.append(t)
# for t in threadlist:
#     t.setDaemon(True)
#     t.start()
# print('主线程结束:',threading.current_thread().name,"用时:",time.time()-start_time)



# join()
# 作用：子线程都结束后,主线程才结束
# 设置：开启线程后使用 

# 子线程都结束后,主线程才结束(join)
import threading
import time
def run():
    time.sleep(2)
    print('当前线程的名字是',threading.current_thread().name)
    time.sleep(2)
# print('主线程开始:',threading.current_thread().name)
# start_time=time.time()
# threadlist=[]
# for i in range(5):
#     t=threading.Thread(target=run)
#     threadlist.append(t)
# for t in threadlist:
#     t.start()
# for t in threadlist:
#     t.join()
# print('主线程结束:',threading.current_thread().name,"用时:",time.time()-start_time)







# 多个线程共享全局变量
# import threading
# import time
# def work1(nums):
#     nums.append(44)
#     print("---work1--",nums)
# def work2(nums):
#     time.sleep(1)#延时一会,保证t1线程中的事情做完
#     print("---work2--",nums)
# g_nums=[11,22,33]
# t1=threading.Thread(target=work1,args=(g_nums,))
# t2=threading.Thread(target=work2,args=(g_nums,))
# t2.start()
# t1.start()
# 线程1对全局的列表g_num修改,通过线程2可以去访问,
# 说明多个线程可以共享全局变量




# 多线程弊端:线程安全问题
# 多线程之间共享数据, 如果没有控制,可能会影响数据安全,导致结果不可预期

# import threading
# my_num=0 #定义全局变量
# def sum1(): #循环给全局变量每次加上1
#     global my_num
#     for i in range(1000000):
#         my_num+=1
#     print("sum1:",my_num)
# def sum2():
#     global my_num
#     for i in range(1000000):
#         my_num+=1
#     print("sum2:",my_num)
# sum1()
# sum2()

# first_thread=threading.Thread(target=sum1)
# second_thread=threading.Thread(target=sum2)
# first_thread.start()
# second_thread.start()



# 希望的结果：sum1和sum2都执行100万次+1,最终输出200万
# 不可预期结果的原因：两个线程同时操作
# 当两个线程同时获取my_num时,各自对他进行+1操作,此时my_num只是+1而不是+2


# 互斥锁
# 作用：保证多线程共享数据的安全性
# 原理：保证同一时刻只有一个线程执行上锁的代码
    # 互斥锁为资源引入2个状态：锁定/非锁定
    # 某线程要更改共享数据时,先将其加锁,加锁后其他线程不能修改 
    # 直到该线程释放锁,其他线程才能再次锁定该资源 
# 缺点：把多线程变成单线程执行, 执行效率下降


import threading
my_num=0 #定义全局变量
lock = threading.Lock()# 创建互斥锁
def sum1(): #循环给全局变量每次加上1
    lock.acquire()# 获取锁
    global my_num
    for i in range(1000000):
        my_num+=1
    print("sum1:",my_num)
    lock.release()# 释放锁
def sum2():
    lock.acquire()# 获取锁
    global my_num
    for i in range(1000000):
        my_num+=1
    print("sum2:",my_num)
    lock.release()# 释放锁
# first_thread=threading.Thread(target=sum1)
# second_thread=threading.Thread(target=sum2)
# first_thread.start()
# second_thread.start()



# 课后作业
# 互斥锁的作用及如何在程序中使用