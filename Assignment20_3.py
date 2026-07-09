import threading

def SumEven(EvenList):
    Sum = 0
    for no in EvenList:
        Sum = Sum + no
    print("Even List :", EvenList)
    print("Sum of Even List :", Sum)


def SumOdd(OddList):
    Sum = 0
    for no in OddList:
        Sum = Sum + no
    print("Odd List :", OddList)
    print("Sum of Odd List :", Sum)


def main():
    n = int(input("Enter number of elements : "))

    Data = []

    for i in range(n):
        no = int(input("Enter number : "))
        Data.append(no)

    print("Input List :", Data)

    EvenList = []
    OddList = []

    for no in Data:
        if no % 2 == 0:
            EvenList.append(no)
        else:
            OddList.append(no)

    t1 = threading.Thread(target=SumEven, args=(EvenList,))
    t2 = threading.Thread(target=SumOdd, args=(OddList,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()
