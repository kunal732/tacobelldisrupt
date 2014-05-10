
'''
Function just gets the inverse of weight. We use this as the sort key function to sort
a list of items in the increasing order of weights.
'''        
def weightInverse(item):
    return 1 / item.getWeight()
'''
The reverse order values of items as sort key Function.
'''
def valueInverse(item):
    return 1 / item.getValue()
'''
Core Kanpsack solution finder. Uses a dictionary of solved sub-problems (Memoization)
to cut on recurssion.
'''    
def findSolutionToKnapsack(toConsider, avail, memozation = None):
    #First call?
    if(memozation == None):
        memozation = {}
    # Is the combination of (number of items to take, weight left) already solved?
    # If so use it
    if (len(toConsider), avail) in memozation:
        return memozation[(len(toConsider), avail)]
    elif toConsider == [] or avail == 0:
        #We don't have any more items or weight to go with.
        result =  (0, ())
    elif toConsider[0].getWeight() > avail:
        # The first one on the list is not suitable for the available weight? (we sorted)
        result = findSolutionToKnapsack(toConsider[1:], avail, memozation)
    else:
        #First item seems ok as far as weight is concerned.
        item = toConsider[0]
        #If we use it what is the value and items to take? 
        withVal, withToTake = findSolutionToKnapsack(toConsider[1:], avail - item.getWeight(), memozation) 
        #Store that value to the current one.
        withVal += item.getValue()
        #If we had not chosen that value what would be the result? For comparison on which
        #path on the solution tree to take.
        withoutVal, withoutToTak = findSolutionToKnapsack(toConsider[1:], avail, memozation)
        #Choose the best path.
        if withVal > withoutVal:
            result = (withVal, withToTake + (item,))
        else:
            result = (withoutVal, withoutToTak)
    #We have a result with accrued value and items to take. Store it.
    memozation[(len(toConsider), avail)] = result
    return result
