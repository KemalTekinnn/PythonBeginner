print("Time you live")
age = int(input('Age; '))
month = int(input('Month(Number); '))
isinstance(month,int)
if month % 2 == 0:
    add = (month // 2) * 1
    add = 30 * month + add
else:
    add =round(month //2) * 1
    add = 30 * month + add

day = (age * 365) + add
hours = day * 24
minutes = hours * 60
seconds = minutes * 60
print('You lived \n{} Day \n{} Hours \n{} Minutes \n{} Seconds'.format(day,hours,minutes,seconds))
