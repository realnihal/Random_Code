def calculateAnswer(lhs,rhs,operator):
    if(operator == "+"):
        return lhs + rhs
    if(operator == "-"):
        return lhs - rhs
    if(operator == "*"):
        return lhs * rhs
    if(operator == "/"):
        return lhs / rhs
    if(operator == "^"):
        return lhs ** rhs
    raise Exception("Unknown operator")

from random import randint
import time

def generateQuestion(lowerbound,upperbound):
    ops = "/*-+"
    opindex = randint(0,len(ops)-1)
    operator = ops[opindex]
    lhs = randint(lowerbound,upperbound)
    rhs = randint(lowerbound,upperbound)
    while(rhs == 0 and operator == "/"):
        rhs = randint(lowerbound,upperbound)
    return lhs,rhs,operator


def isAccurateEnoughAnswer(givenAnswer, correctAnswer ,tolerance = 0.01):
    difference = abs(float(givenAnswer) - float(correctAnswer))
    return difference <= tolerance

print("This is a Math quiz game to test your arithmetic abilty, you can set the lower and upper values. The tolerance is set to 0.01")
time.sleep(2)
lb = int(input("enter the lower bound of values : "))
ub = int(input("enter the upper bound of values : "))
totalQuestions = int(input("enter no of questions you want to attempt : "))
print("Welcome to the Math quiz \nPress q as an answer to exit immediately\n")

count = 0
correct = 0
while(count <+ totalQuestions):
    question = generateQuestion(lb,ub)
    playerAnswer = input("{0}{2}{1} = ".format(question[0],question[1],question[2]))
    if(playerAnswer == "q"):
        break
    correctAnswer = calculateAnswer(question[0],question[1],question[2])
    if(isAccurateEnoughAnswer(correctAnswer,playerAnswer)):
        print("Correct!")
        correct += 1
    else:
        print("wrong")
    count += 1
percent = (correct/totalQuestions)*100
print("you scored {0} correct out of {1}. Or achieved {2}% accuracy".format(correct,totalQuestions,percent))
te = input()
