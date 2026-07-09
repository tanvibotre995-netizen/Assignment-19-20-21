from functools import reduce

CheckEven = lambda No:(No % 2 == 0)

Square = lambda n:n*n

Addition = lambda No1,No2:No1+No2

def main():
    Data = [5,2,3,4,3,4,1,2,8,10]

    print("Input data is :",Data)

    FData = list(filter(CheckEven,Data))

    print("Data after filter:",FData)


    MData = list(map(Square,FData))

    print("Data after filter:",MData)

    RData=reduce(Addition,MData)

    print("Data after filter:",RData)


if __name__ == "__main__":
    main()
