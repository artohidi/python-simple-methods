sumNumber = 1
if __name__ == '__main__':
    getNumber = int(input("enter a number here:"))
    while getNumber > 0:
        sumNumber = sumNumber * getNumber
        getNumber = getNumber - 1
    print(sumNumber)
