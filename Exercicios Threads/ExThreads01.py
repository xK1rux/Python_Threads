import multiprocessing
import time

def threads(id):
    time.sleep(0.5)
    print(f"Thread #{id}")
    
def main():
    params: int = [0]*5
    
    for i in range(5):
        params[i] = i + 1
    
    with multiprocessing.Pool(processes=5) as threads:
        threads.map(threads, params)


if __name__ == "__main__":
    main()