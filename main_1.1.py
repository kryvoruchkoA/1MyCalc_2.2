import calcCalculations
import calcCases
import calcClasses
import calcModules
import logging


## Move START to main program code:

# def start():
answer: str = 'y' # -- setting the parameter to skip user enter --

# -- Read user's expression --
while answer in ['y', 'Y']:

    #expression is hardcoded in calcModules.requestData()
    expression = calcModules.requestData()
    #print(expression, '\n')

    # Read and determine the expression
    itemPosition = 0
    #finalExpression = ''
    aggregatedExpression = []
    leng = len(expression) # < DEBUGING >
    newVar = calcClasses.ArrayItem

    while itemPosition < len(expression):
        finalExpression = ''
        item = expression[itemPosition] # < DEBUGING >
        if calcModules.detectNumber(itemPosition, expression[itemPosition]) == True: itemPosition = calcModules.saveNumber(itemPosition, expression, aggregatedExpression)
        else:
            newVar = calcCases.symbolRecognizer(expression[itemPosition])
            if newVar.item != '':
                finalExpression += expression[itemPosition] # has to be redisigned for long func like SIN, LOG
                
                calcClasses.aggregateExpression(newVar, aggregatedExpression)
                itemPosition += len(finalExpression)
                
            else:
                #print(expression[itemPosition], '  Incorrect syntax')
                break
                

    print('main', aggregatedExpression)
    print()
    if aggregatedExpression != []:
        print('main:', expression, '=', calcCalculations.calculate(aggregatedExpression))
    else:
          print(expression)
          print('Incorrect syntax: Undefined symbol < ', expression[itemPosition], ' > is used.')
          answer = 'n'
    
    # CALCULATION
    
        
    
    #answer = input('try again? (y/n) ')
    #answer = 'n' # <DEBUG





