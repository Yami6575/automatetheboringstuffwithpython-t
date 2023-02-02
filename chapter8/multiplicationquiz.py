
import random, time

numberOfQuestions = 10
correctAnswers = 0
for questionNumber in range(numberOfQuestions):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)
    attempts = 0
    
    t1 = int(time.time())
    while attempts < 3:
        attempts+=1
        answer = int(input(prompt))
        t2 = int(time.time())

        if t2-t1>=8:
            print('Out of time')
            break
        
        if attempts == 3:
            print("Out of tries")
            break            
                
        elif answer == num1*num2:
            print("Correct")
            correctAnswers+=1
            break

print('correctAnswers:', correctAnswers)