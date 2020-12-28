import time
import threading

thread_list = []


def MyThread(value):
    time.sleep(0.01 * pow(1.1, float(value)))
    print(value)


def main():
    n = int(input('n : '))
    for i in range(n):
        thread_list.append(
            threading.Thread(target=MyThread,
                             args=input('data[%d] : ' % (i + 1))))
    start = time.perf_counter()
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()
    end = time.perf_counter()
    print('time : %f s' % (end - start))


if __name__ == "__main__":
    main()