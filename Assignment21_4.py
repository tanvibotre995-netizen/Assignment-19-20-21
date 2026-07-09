import threading

Sum = 0
Product = 1

def Addition(data):
    global Sum

    for i in data:
        Sum += i

def Multiplication(data):
    global Product

    for i in data:
        Product *= i

def main():
    global Sum, Product

    n = int(input("Enter number of elements: "))

    data = []

    for i in range(n):
        data.append(int(input()))

    t1 = threading.Thread(target=Addition, args=(data,))
    t2 = threading.Thread(target=Multiplication, args=(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Sum:", Sum)
    print("Product:", Product)

if __name__ == "__main__":
    main()
