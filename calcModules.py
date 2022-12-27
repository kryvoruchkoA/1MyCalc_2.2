import os
import calcCalculations
import calcCases
import calcClasses


def start():
    answer: str = 'y'
    while answer in ['y', 'Y']:
        #qwe =  # full Expression without spaces
        expression = definePriority(requestData())
        #expression = defineExpression(asd) # Expression to calculate (full or nested)
        print(expression)


##     Old Main part to refactor

        # expression is hardcoded in calcModules.requestData()
        # >>  expression = calcModules.requestData()
        # print(expression, '\n')

        # Read and determine the expression


##  End of Main

        answer = input('try again? (y/n)')
        os.system('cls')
        
#  #  #  #  #  #  #

def requestData():
    #incomeRequest = input('Enter expression: ')
    incomeRequest = "ctg45"
    #incomeRequest = "6- 10log(10000)"
    #incomeRequest = "0 .2 5 * (2.0+ 0. 2)*5-7/2 "
    #incomeRequest = "0 .2 5 * (2.0+ 0. 2)*5 "
    return spaceRemove(incomeRequest)


def parentheses(sentence):
    pos1 = None
    pos2 = None
    pos = 0
    for i in sentence:
        if i == '(':
            pos1 = pos
        elif i == ')':
            pos2 = pos
        pos += 1
    return ([pos1, pos2])


def definePriority(sentence):
    aaa = calcClasses.ArrayItem
    range = parentheses(sentence)
    if range == [None, None]:
        #aaa.pos = range[0]
        #aaa.item = range[1] - range[0] + 1
        aaa.expression = sentence  # < DEBUGING >
        return aaa
        #return sentence
    elif range[0] != None and range[1] != None:
        aaa.pos = range[0]
        aaa.item = range[1] - range[0] + 1
        aaa.expression = sentence[range[0]+1: range[1]] # < DEBUGING >
        return aaa
        #return sentence[range[0]+1: range[1]]
    else: return (syntErr(range, temp))


'''
def syntErr(range, sentence):
    if range[0] != None:
        print(sentence[range[0]])
        return ("Wrong syntacs: The parenthes '"+ sentence[pos[0]] + "' were not closed !")
    else:
        return ("Wrong syntacs: The parenthes '" + sentence[pos[1]] + "' were not opened !")
'''

def defineExpression(expression):
    subItemPosition = 0
    aggregatedExpressionSUB = []
    leng = len(expression)  # < DEBUGING >
    newVar = calcClasses.ArrayItem

    while subItemPosition < len(expression):
        finalExpression = ''
        item = expression[subItemPosition]  # < DEBUGING >
        if detectNumber(subItemPosition, expression[subItemPosition]): # == True:
            subItemPosition = saveNumber(subItemPosition, expression, aggregatedExpressionSUB)
        else:
            #newVar = calcCases.symbolRecognizer(expression[subItemPosition]) - ver 2.0
            newVar = calcCases.symbolRecognizer(expression, subItemPosition) # ver 2.2
            if newVar.item != '':
                finalExpression = getFinal(expression, subItemPosition, newVar.position)
                # finalExpression += expression[subItemPosition]  ver 2.0  # has to be redisigned for long func like SIN, LOG
                calcClasses.aggregateExpression(newVar, aggregatedExpressionSUB)
                subItemPosition += len(finalExpression)

            else:
                # print(expression[itemPosition], '  Incorrect syntax')
                break

    #print('cM Defined Expression:', aggregatedExpression)
    return aggregatedExpressionSUB
    #print()

def getFinal(expression, pos, lenght):
    final = ''
    i = 0
    for i in range(lenght):
        final = final + expression[pos + i]
    return final

###   Old work modules section  #################################################

         # # #


##  Request a string with a expression


def spaceRemove(spacesString):
    if spacesString.isspace():
        return ' '
    else:
        return spacesString.replace(' ', '')


def detectNumber(itemPosition, incomeData):
    if itemPosition == 0 and incomeData in ['-', '+']: return True
    try:
        data = float(incomeData)
        # print('CALC > ', incomeData, '=> Passed. What is next?') # < DEBUGING >
        return True
    except ValueError:
        #print('DNu : Ups, exception') # < DEBUGING >
        return False
        

def gatherNumber(itemPositionLocal, expression):
    gatheredNumber = ''
    #leng = len(expression) # < DEBUGING >
    try:
        while detectNumber(itemPositionLocal, gatheredNumber + expression[itemPositionLocal]) == True: # to be refactored
            gatheredNumber = gatheredNumber + expression[itemPositionLocal]
            itemPositionLocal += 1
   # < DEBUG >
   # is EXCEPT needed exept debuging ?
    except IndexError:
        pass
        #print('GN-exeption: Sorry, end of expression', itemPositionLocal + 1, '>', len(expression))
    return gatheredNumber


def symbolRecognizerShort(incomeData):
    if incomeData in ('+', '-', '*', '/', '^', 'l', 's'):
        return True
    else: False
    
    
def logging(logs, file='logs.html'):
    with open('logs.html', w) as log:
        log.write(syr(logs))
        close('logs.html')

def saveNumber(itemPosition, expression, aggregatedExpression):
    newVar = calcClasses.ArrayItem
    newVar.priority = 0
    newVar.type = 'num'
    newVar.item = gatherNumber(itemPosition, expression)
    itemPosition += len(newVar.item)
    calcClasses.aggregateExpression(newVar, aggregatedExpression)
    return itemPosition





#############
#
#   Temporary section
#
#############
