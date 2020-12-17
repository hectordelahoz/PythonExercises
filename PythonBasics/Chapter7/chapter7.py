#-------Funciton Example---------
print('-------Funciton Example---------')
def setName():
    name = None
    while name == None:
        name = input('Please set your event name: ')        
    return name

def setTime(name):
    print(f'OK. Now lets set {name} Time')
    hour = None
    while hour == None:
        hour = input('Please set an Hour: ')
    return hour
        
def setPeriod(name):
    print(f'OK. Now lets set {name} Period')
    period = None
    while period == None:
        period = input('Please set event period: ')
    return period

def printEventSetting(name, hour, period):
    print(f'Your event: {name} is set to {hour} every {period} a week')

def main():
    print('Welcome to Alarm setting')
    eventName = setName()
    alarmTime = setTime(eventName)
    alarmPeriod = setPeriod(eventName)
    printEventSetting(eventName,alarmTime,alarmPeriod)
    reminder(alarmPeriod)
    remider = [1]
    changeReminder(remider)       
    printEventSetting(eventName,alarmTime,alarmPeriod)
    settings = [[eventName, alarmTime, alarmPeriod, remider[0]], [eventName, alarmTime, alarmPeriod, remider[0]]]
    printAllEvents(*settings)
    details = {'Name':eventName, 'Data':alarmTime, 'Period':alarmPeriod, 'Remider':remider[0]}
    pritWithDetails(**details)

#-------Passing by Value Example---------
print('-------Passing by Value Example---------')
def reminder(per):
    message = per + ' week remining'
    print(f'please remember your event: {message}')

#-------Passing by Ref Example---------
print('-------Passing by Ref Example---------')
def changeReminder(ref):
    ref[0] += 5 
    print(f'changing your reminder to : {ref[0]}')

#-------Passing by Ref Example---------
print('-------Passing by Ref Example---------')
def printAllEvents(*args):
    if len(args):
        for param in args:
            print(f'{param}')

#-------Passing kwargs Example---------
print('-------Passing by kwargs Example---------')
def pritWithDetails(**kargs):
    index = 0
    for k in kargs:
        print(f'{index} param name {k}, param value {kargs[k]}')
        index += 1

if __name__ == "__main__":
    main()    
