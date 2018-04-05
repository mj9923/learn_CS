import random
import math

def rollDie():
    """returns a random into between 1 to 6"""
    return random.choice([1,2,3,4,5,6])

def testRoll(n):
    result =""
    for i in range(n):
        result = result+str(rollDie())
    print(result)

def runSim(goal, numTrials):
    total = 0
    for i in range(numTrials):
        result=''
        for j in range(len(goal)):
            result += str(rollDie())
        if result == goal:
            total+=1
    print('Actual probability of', goal, '=', round((1/6**len(goal)),8))
    estProbability = round((total/numTrials), 8)
    print('Estimated Probability of', goal, '=', round(estProbability, 8))

runSim('11111', 10)

def sameDate(numPeople, numSame):
    possibleDates = 4*list(range(0,57))+[58]+4*list(range(59,366))+4*list(range(180,270))
    birthdays = [0]*366
    for p in range(numPeople):
        birthDate=random.choice(possibleDates)
        birthdays[birthDate] +=1
    return max(birthdays) >= numSame

def birthdayProb(numPeople, numSame, numTrials):
    numHits = 0
    for t in range(numTrials):
        if sameDate(numPeople, numSame):
            numHits +=1
    return numHits/numTrials

for numPeople in [10, 20, 40, 100]:
    print('For', numPeople, 'estimated probability of a shared birthday is', birthdayProb(numPeople, 2, 100000))
    numerator = math.factorial(366)
    denom = (366**numPeople)*math.factorial(366-numPeople)
    print('Actual probability for N=100=', 1-numerator/denom)
