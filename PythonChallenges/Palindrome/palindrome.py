import re

def evaluatePalindrome(string):
    string = string.upper()
    string = re.split('[^a-zA-Z]',string)
    string = ''.join(string)
    revString = string[::-1]
    return string == revString

def main():
    print(evaluatePalindrome('Go Hang a SAlami - I\'m a lasagna hog.'))

if __name__ == "__main__":
    main()