

class ArrayItem:
    def __init__(self, pos, prior, itemType, item, incomeExpression):
        self.position = pos
        self.priority = prior
        self.type = itemType
        self.item = item
        self.expression = incomeExpression



def aggregateExpressionStr(frase, result, storage):
    #rint('Clases> agrExprStr:', storage)
    if '('+frase+')' in storage:
        #print('Clases> agrExprStr-IF:', '('+frase+')')
    #x = storage.replace('('+frase+')', str(result))
        return storage.replace('('+frase+')', str(result))
    else:
        #print('Clases> agrExprStr-ELSE:', frase)
        return storage.replace(frase, str(result))

def aggregateExpression(income, storage):
    storage.append([income.priority, income.type, income.item])


def aggregateArray(pos, quantity, result, storage):
    storage[pos-1][2] = result
    for i in range(quantity):
        storage.pop(pos)
    return storage

         
'''
def aggregateExpression2(pos, quantity, result, storage):
    storage[pos-1][2] = result
    for i in range(quantity):
        storage.pop(pos)
    return storage
'''