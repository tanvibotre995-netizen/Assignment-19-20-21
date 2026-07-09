import threading

def SumEvenFactor(No):
    Sum = 0

    for i in range(1, No + 1):
        if No % i == 0 and i % 2 == 0:
            Sum = Sum + i

    print("Sum of even factors:", Sum)


def SumOddFactor(No):
    Sum = 0

    for i in range(1, No + 1):
        if No % i == 0 and i % 2 != 0:
            Sum = Sum + i

    print("Sum of odd factors:", Sum)


def main():
    No = int(input("Enter a number: "))

    t1 = threading.Thread(target=SumEvenFactor, args=(No,))
    t2 = threading.Thread(target=SumOddFactor, args=(No,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()
