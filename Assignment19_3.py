from functools import reduce

Number=lambda n:(n>=70 and n<=90)

Increase=lambda No:No+10

Product=lambda a,b:a*b

def main():
    data=[4,34,36,76,68,24,89,23,86,90,45,70]

    print("Input is",data)

    fdata=list(filter(Number,data))

    print("list after filter",fdata)

    mdata=list(map(Increase,fdata))

    print("list after map",mdata)

    rdata=reduce(Product,mdata)

    print("output of reduce",rdata)

if __name__ == "__main__":
    main()
