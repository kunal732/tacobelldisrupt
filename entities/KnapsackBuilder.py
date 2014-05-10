
from entities.utilities import findSolutionToKnapsack

class KnapsackBuilder(object):
    def __init__(self, sortedSetOfItems):
        self.ssetOfItems = sortedSetOfItems
        #Always use empty list to avoid Null Pointer Exception / None Exception ;-)
        self.chosenItems = []
        self.value = 0
    
    def packKnapSack(self, totalWeightLimit = 100):
        #Have we run out of Items.
        if(len(self.ssetOfItems) <= 0):
            return None
        self.val, self.chosenItems = findSolutionToKnapsack(self.ssetOfItems, totalWeightLimit)
    '''
    Get the items we short listed.
    '''
    def getListOfItemsToTake(self):
        return self.chosenItems
    '''
    Get the accumlated value of items we short listed.
    '''
    def getAccumulatedValue(self):
        return self.value
#----------------------------------------------------------------------------------
