import threading
import time

def task1():
    for i in range(4):
        print(f"Task 1 - Step {i}")
        time.sleep(1)  # Simulating a delay

def task2():
    for i in range(4):
        print(f"Task 2 - Step {i}")
        time.sleep(1)  # Simulating a delay

# Main function
if __name__ == "__main__":
    print("Starting threads...")
    
    # Creating threads
    thread1 = threading.Thread(target=task1)
    thread2 = threading.Thread(target=task2)
    
    # Starting threads
    thread1.start()
    thread2.start()
    
    # Wait for threads to complete
    thread1.join()
    thread2.join()
    
    print("All threads have completed.")