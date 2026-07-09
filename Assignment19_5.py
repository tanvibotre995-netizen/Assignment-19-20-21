from functools import reduce

Prime =lambda n:n>1 and all(n % i != 0 for i in range(2,n))

Multiply=lambda n:n*2

Max=lambda a,b:a>b

def main():
    data =[2,70,11,10,17,23,31,77]

    print("input is",data)

    fdata=list(filter(Prime,data))

    print("list after filter",fdata)

    mdata=list(map(Multiply,fdata))

    print("list after map",mdata)

    rdata=reduce(max,mdata)

    print("output of reduce",rdata)

if __name__ == "__main__":
    main()
