def inclusiveRange(*args):
    numParam = len(args)
    if numParam < 1:
        raise TypeError(f'at least 1 argument is expected')
    elif numParam == 1:
        result = list(range(args[0]))
        result.append(args[0])
        return result
    elif numParam == 2:
        result = list(range(args[0], args[1]))
        result.append(args[1])
        return result
    elif numParam == 3:
        result = list(range(args[0], args[1], args[2]))
        result.append(args[1])
        return result
    else:
        raise TypeError(f'no more than 3 arguments are expected')

def main():
    try:
        print(inclusiveRange(5))
        print(inclusiveRange(2,5))
        print(inclusiveRange(2,10,2))
        print(inclusiveRange())
    except TypeError as error:
        print(f'Error Name: {error}')

if __name__ == "__main__":
    main()