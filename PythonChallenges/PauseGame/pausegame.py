import random
import datetime

def pauseGame():
    target = random.randint(2,4)
    print(f'Your target is {target} seconds')
    input('---Press Enter to Begin---')
    start = datetime.datetime.now()
    input(f'...Press Enter again after {target} seconds...')
    elapseTime = datetime.datetime.now() - start
    print(f'Elapse Time {elapseTime.total_seconds():.3f} seconds.')
    diff = elapseTime.total_seconds() - target
    if diff > 0:
        print(f'({diff:.3f} seconds too slow)')
    elif diff < 0:
        print(f'({diff:.3f} seconds too fast)')
    else:
        print(f'({diff} right on targe!)')

def main():
    pauseGame()

if __name__ == "__main__":
    main()