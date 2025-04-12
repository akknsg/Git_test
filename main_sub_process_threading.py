# main_sub_process_threading.py
import time

def task():
    for i in range(5):
        print(f"Worker task running... {i}")
        time.sleep(1)

if __name__ == "__main__":
    task()