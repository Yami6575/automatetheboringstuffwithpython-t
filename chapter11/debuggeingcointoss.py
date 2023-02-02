import random
guess = ''
a=0
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    if guess=='heads':
        a=0
        break
    elif guess=='tails':
        a=1
        break
        
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == a:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if guess=='heads':
        a=0
    elif guess=='tails':
        a=1
    if toss == a:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')