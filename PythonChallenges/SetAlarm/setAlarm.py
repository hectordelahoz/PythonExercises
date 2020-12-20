import time
import winsound

def setAlarm(setTime,message):
    print(f'your alarm is set to play on {setTime - time.time()}s')
    while (setTime - time.time()) > 0:
        continue
    else:
        winsound.Beep(240,1000)
        print(message)

def main():
    setAlarm(time.time()+2,'WakeUp!')

if __name__== "__main__":
    main()