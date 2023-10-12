import threading
import time


def thread_one():
    for i in range(5):
        print("Thread 1: Executando passo", i)
        time.sleep(1)


def thread_two():
    for i in range(5):
        print("Thread 2: Executando passo", i)
        time.sleep(1)


t1 = threading.Thread(target=thread_one)
t2 = threading.Thread(target=thread_two)

t1.start()
t2.start()



t1.join()
t2.join()

print("Todas as threads terminaram.")
