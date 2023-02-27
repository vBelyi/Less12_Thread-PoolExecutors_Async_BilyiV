import math
import concurrent.futures
import time


def factorial(n):
    return math.factorial(n)
    # num = 1
    # for i in range(2, n+1):
    #     num *=i
    # return num

numbers = [50, 70, 20, 100, 3, 17, 5, 11, 16]

def thread_executor():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(factorial, numbers))
        return results

def process_executor():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = list(executor.map(factorial, numbers))
        return results

if __name__ == '__main__':
    start_time = time.time()
    thread_results = thread_executor()
    end_time = time.time()
    thread_time = end_time-start_time
    print('TPEtime: ',thread_time)

    start_time = time.time()
    process_results = process_executor()
    end_time = time.time()
    process_time = end_time - start_time
    print('PPEtime: ', process_time)

    if thread_time > process_time:
        print(process_executor(), '\nFactorials using ProcessPoolExecutor is faster!')
    elif thread_time < process_time:
        print(thread_executor(), '\nFactorials using ThreadPoolExecutor is faster!')



