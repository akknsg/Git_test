import threading
import time

# Function to be executed in a thread
def print_numbers(name, count):
    for i in range(1, count + 1):
        print(f"{name}: {i}")
        time.sleep(1)  # Simulate some work with a delay

# Create threads
thread1 = threading.Thread(target=print_numbers, args=("Thread-1", 6))
thread2 = threading.Thread(target=print_numbers, args=("Thread-2", 6))

# Start threads
thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()

print("All threads have finished.")