def getReverseSentece(string, token):
    r = ' '.join(string.split(token)[::-1])
    return r

def getSplitString(string, token):
    return string.split(token)

def basedNumber(string, value, base):
    if base == 'o':
        return f'{string} {value:0>3o}'
    elif base == 'b':
        return f'{string} {value:0>8b}'
    elif base == 'x':
        return f'{string} {value:0>2x}'
    else:
        raise TypeError(f"""Expecting base:
        - octal (o),
        - binary (b),
        - hexa (x)""")

def decimalplaces(string,value):
    s = string + '{:.6f}'
    return s.format(value)

def fixedpadding(string, value):    
    s = string + '{:0>5}'
    return s.format(value)

def signedNumber(string, value, sign):
    if sign == '+':
        s = string + '{:+,}'
        return s.format(value)
    else:
        s = string + '{:-,}'
        return s.format(value)

def formatOrders(string, lst):
    s = string + '{} {} {} {}'
    return s.format(lst[3],lst[2],lst[1],lst[0])

def formattedNumber(string, value, point):
    s = string + '{:,}'
    if point == '.':
        return s.format(value).replace(',','.')
    return s.format(value)

def formatted(string, value):
    s = string + '{}'
    return s.format(value)

def concat(string1, string2):
    return string1 + ' ' + string2

def back(string):
    return string[::-1]

def title(string):
    return string.title()

def capitalize(string):
    return string.capitalize()
    
def swapcase(string):
    return string.swapcase()

def lower(string):
    return string.lower()

def upper(string):
    return string.upper()

def main():
    s = "this is string s"
    print(upper(s))
    print(lower(s))
    print(swapcase(s))
    print(capitalize(s))
    print(title(s))
    print(back(s))
    print(concat(s,title(s)))
    print(formatted(s,10))
    print(formattedNumber(s, 10000000, '.'))
    print(signedNumber(s, 10000000, '+'))
    print(signedNumber(s, 10000000, '-'))    
    print(formatOrders(s,[0, 1 , 2, 3]))
    print(fixedpadding(s,57))
    print(decimalplaces(s,57))
    print(basedNumber(s,10,'b'))
    print(basedNumber(s,10,'x'))
    print(basedNumber(s,10,'o'))
    try:
        print(basedNumber(s,10,'h'))
    except TypeError as e:
        print(f'This was the error: {e}')
    print(getSplitString(s,' '))
    print(getReverseSentece(s,' '))

if __name__ == "__main__":
    main()