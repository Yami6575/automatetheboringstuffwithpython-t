import random
numberofstreaks=0

a=[]
for i in range(10000):
    b=random.randint(0,1)
    a.append(b)
streak=0
for i in range(len(a)-1):
    if a[i]==a[i+1]:
        streak+=1
    else :
        continue
    if streak==6:
        numberofstreaks+=1
        streak=0
print('chance of streak:',numberofstreaks/100)