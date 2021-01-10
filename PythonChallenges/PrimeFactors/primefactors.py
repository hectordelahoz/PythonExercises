def findPrimeFactor(number):
    while number != 1:
        for i in range(2,number+1):
            if number%i == 0:
                yield i
                number = int(number/i)
                break

def main():
    for x in findPrimeFactor(24):
        print(x)

if __name__ == "__main__":
    main()