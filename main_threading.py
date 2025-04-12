# main.py
import threading
import subprocess

def run_subprocess():
    # Run the main_sub_process_threading.py file
    subprocess.run(["python", "main_sub_process_threading.py"])

if __name__ == "__main__":
    # Create a thread to run main_sub_process_threading.py
    worker_thread = threading.Thread(target=run_subprocess)
    worker_thread.start()

    # Main thread task
    for i in range(5):
        print(f"Main task running... {i}")