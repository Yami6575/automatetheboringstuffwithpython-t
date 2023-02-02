import re,sys

Data=''
regex=re.compile(r'([0-3]\d)/([01]\d)/([1-2]\d{3})')
RegexDate=regex.findall(Data)
for day,month,year in RegexDate:
    day=int(day)
    month=int(month)
    year=int(year)

    if (month==4 or month==6 or month==9 or month==11):
        if day==31:
            print('wrong date')
    elif month==2:
        if year%4==0:
            if not day in range(1,30):
                print('wrong date')
        else:
            if not day in range(1,29):
                print('wrong date')
    print('wrong format')
    
    


