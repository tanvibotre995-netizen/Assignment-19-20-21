import time
import threading
def Sumeven(No):
    Sum = 0

    for i in range(2,No,2):
        Sum = Sum + i
    print("summation of even:",Sum)



def Sumodd(No):
    Sum = 0

    for i in range(1,No,2):
        Sum = Sum + i
    print("summation of odd:",Sum)


def main():
    start_time = time.perf_counter()

    t1 = threading.Thread(target = Sumeven, args=(1000000,))
    t2 = threading.Thread(target = Sumodd, args=(1000000,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end_time = time.perf_counter()

    print(f"time required is:{end_time - start_time:.4f}")
    

if __name__ == "__main__":
    main()


