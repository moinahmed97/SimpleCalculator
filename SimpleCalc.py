import random
level = int(input("Enter difficulty level(1 or 2):"))

 
def n(level):
    if level == 1:
        return(random.randrange(10),random.randrange(10))
    if level == 2:
        return(random.randrange(10,100),random.randrange(10,100))
        

def response():
    responses = {'correct':['Very good!','Nice work!','Keep up the good work!'],
                 'wrong':['No,please keep trying!.','Wrong,Try once more.','No,Keep trying.']}
    return responses


def operators():


    print('addition        = 1')
    print('subtraction     = 2')
    print('divide          = 3')
    print('multiplaction   = 4')
    print('mixed operators = 5')
    print('')
    oper = int(input("Enter an operation from(1 to 5):"))
    return oper

   
    

oper = operators()
x1 = n(level)[0]
x2 = n(level)[1]

x3 = n(level)[0]
x4 = n(level)[1]

x5 = n(level)[0]
x6 = n(level)[1]

x7 = n(level)[0]
x8 = n(level)[1]


m = x1 * x2
d = (x3 // x4)
if x4 == 0:
    x4 == 1
a = x5 + x6
if int(x7) < int(x8):
    s = x8 - x7
else:
    s = x7 - x8




correct = 0
incorrect = 0
while True:
    if oper == 4 or oper == 5:
        print('how much is', x1,'*', x2, '?')
        ques = int(input("Enter your answer(-1 to exit):"))
        if ques == -1:
            print("")
            print("number of correct answers:",correct)
            print("number of incorrect answers:",incorrect)
            print("Thanks for Playing!!")
            break
        if int(m) == ques:
            print(response()['correct'][random.randrange(3)])
            correct+=1
            oper = operators()
        elif int(m) != ques:
            incorrect+=1
            print(response()['wrong'][random.randrange(3)])
            print('')
            continue
        
    if oper == 3 or oper == 5:
        print('how much is', x3,'//', x4, '?')
        ques = float(input("Enter your answer(-1 to exit):"))
        if ques == -1:
            print("")
            print("number of correct answers:",correct)
            print("number of incorrect answers:",incorrect)
            print("Thanks for Playing!!")
            break
        
        if d == ques:
            print(response()['correct'][random.randrange(3)])
            correct+=1
            oper = operators()
        elif d != ques:
            incorrect+=1
            print(response()['wrong'][random.randrange(3)])
            print('')
            continue
     
            
    if oper == 1 or oper == 5:
        print('how much is', x5,'+', x6, '?')
        ques = int(input("Enter your answer(-1 to exit):"))
        if ques == -1:
            print("")
            print("number of correct answers:",correct)
            print("number of incorrect answers:",incorrect)
            print("Thanks for Playing!!")
            break
        if int(a) == ques or n == 1:
            correct+=1
            print(response()['correct'][random.randrange(3)])
            oper = operators()
        elif int(a) != ques:
            incorrect+=1
            print(response()['wrong'][random.randrange(3)])
            print('')
            continue


        
    if oper == 2 or oper == 5:
        if int(x7) < int(x8):
            print('how much is', x8,'-', x7, '?')
            ques = int(input("Enter your answer(-1 to exit):"))
            if ques == -1:
                print("")
                print("number of correct answers:",correct)
                print("number of incorrect answers:",incorrect)
                print("Thanks for Playing!!")
                break
        
            if int(s) == ques or n == 2:
                correct+=1
                print(response()['correct'][random.randrange(3)])
                print('')
                oper = operators()
            elif s != ques:
                incorrect+=1
                print(response()['wrong'][random.randrange(3)])
                print('')
                continue

        else:
            print('how much is', x7,'-', x8, '?')
            ques = int(input("Enter your answer(-1 to exit):"))
            if ques == -1:
                print("")
                print("number of correct answers:",correct)
                print("number of incorrect answers:",incorrect)
                print("Thanks for Playing!!")
                break
        
            if int(s) == ques or n == 2:
                correct+=1
                print(response()['correct'][random.randrange(3)])
                print('')
                oper = operators()
            elif s != ques:
                incorrect+=1
                print(response()['wrong'][random.randrange(3)])
                print('')
                continue

                           
                
            


        
    
    
    


        


