def sumNumbers(*args):
    n = len(args)
    result = 0
    if n == 0:
        raise TypeError(f'At least one argument is expected')
    else:
        for x in args:
            if isinstance(x,list):
                result += sum(x)
            elif isinstance(x,int) or isinstance(x,float):
                result += x
    return result

def main():
    print("this is my main")

if __name__ == "__main__":
    main()