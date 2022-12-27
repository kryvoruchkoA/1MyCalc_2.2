import calcCalculations
import calcClasses
import calcModules


## Move START to main program code:

#calcModules.start()

#   " .28 3 * (2.0+ 0. 2)*5-7*2 "

answer: str = 'y' # -- setting the parameter to skip user enter --

# -- Read user's expression --
while answer in ['y', 'Y']:


    #expression is hardcoded in calcModules.requestData()
    fullExpression = calcModules.requestData()
    full = fullExpression
    #print('main:', full)

    itemPosition = 0
    #while itemPosition < len(full):
    while not calcModules.detectNumber(1, full):

        internalExpression = calcModules.definePriority(full)
        # here must be defined nested expression as STRING

        aggregatedExpression = calcModules.defineExpression(internalExpression.expression)
        # here expression must be converted to [ [] [] [] ]
        #print('main_ Defined Expression:', aggregatedExpression)  # < DEBUGING >

        if aggregatedExpression != []:
            intermediateResult = calcCalculations.calculate(aggregatedExpression)
            #here intermediateResult is a Result of nested expression - STRING
            #print('main> calculated: intermediateResult = ', intermediateResult)

        else:
            #print('main> Incorrect syntax: Undefined symbol < ', internalExpression.expression[itemPosition], ' > is used.')
            answer = 'n'

        full = calcClasses.aggregateExpressionStr(internalExpression.expression, intermediateResult, full)

    print()
    print(' # # #')
    print(fullExpression, '=', full)
    #answer = input('try again? (y/n) ')
    answer = 'n' # <DEBUG>

    # # #

#   O L D    section

    # # #

'''    
    # Read and determine the expression
    itemPosition = 0
    #finalExpression = ''
    aggregatedExpression = []
    leng = len(expression) # < DEBUGING >
    newVar = calcClasses.ArrayItem

    while itemPosition < len(expression):
        finalExpression = ''
        item = expression[itemPosition] # < DEBUGING >
        if calcModules.detectNumber(itemPosition, expression[itemPosition]) == True:
            itemPosition = calcModules.saveNumber(itemPosition, expression, aggregatedExpression)
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
'''
