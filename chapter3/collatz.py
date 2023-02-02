def collatz(number):
    
    if number%2==0:
        a=number//2
        return a
    else :
        b=3*number+1
        return b
    
a=int(input("enter a number:"))
print(a)
while(a!=1):
    
    a=collatz(a)
    if a==1:
        break
    else:
        print(a)
print("1")

    