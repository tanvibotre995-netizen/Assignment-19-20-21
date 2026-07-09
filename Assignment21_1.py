import threading

def CheckPrime(no):
    if no < 2:
        return False

    for i in range(2, no):
        if no % i == 0:
            return False
    return True

def Prime(data):
    print("Prime Numbers:")
    for i in data:
        if CheckPrime(i):
            print(i)

def NonPrime(data):
    print("Non Prime Numbers:")
    for i in data:
        if not CheckPrime(i):
            print(i)

def main():
    n = int(input("Enter number of elements: "))

    data = []

    for i in range(n):
        data.append(int(input()))

    t1 = threading.Thread(target=Prime, args=(data,), name="Prime")
    t2 = threading.Thread(target=NonPrime, args=(data,), name="NonPrime")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
