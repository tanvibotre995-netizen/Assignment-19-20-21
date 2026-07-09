import threading

def CountSmall(String):
    count = 0
    for ch in String:
        if ch.islower():
            count += 1

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Number of lowercase characters :", count)
    print()


def CountCapital(String):
    count = 0
    for ch in String:
        if ch.isupper():
            count += 1

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Number of uppercase characters :", count)
    print()


def CountDigits(String):
    count = 0
    for ch in String:
        if ch.isdigit():
            count += 1

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Number of digits :", count)
    print()


def main():
    String = input("Enter a string : ")

    t1 = threading.Thread(target=CountSmall, args=(String,), name="Small Thread")
    t2 = threading.Thread(target=CountCapital, args=(String,), name="Capital Thread")
    t3 = threading.Thread(target=CountDigits, args=(String,), name="Digit Thread")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("Exit from main")


if __name__ == "__main__":
    main()
