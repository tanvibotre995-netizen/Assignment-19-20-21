import threading

def Display1():
    print("Thread1:")
    for i in range(1, 51):
        print(i)

def Display2():
    print("Thread2:")
    for i in range(50, 0, -1):
        print(i)

def main():
    t1 = threading.Thread(target=Display1, name="Thread1")
    t2 = threading.Thread(target=Display2, name="Thread2")

    t1.start()
    t1.join()      

    t2.start()
    t2.join()

if __name__ == "__main__":
    main()
