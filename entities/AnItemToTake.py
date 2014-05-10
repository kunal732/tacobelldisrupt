class AnItemToTake(object):
    def __init__(self, name, weight = 0, value = 0):
        self.name = name
    
        if (value == 0):
            self.value = float(1)
        else:
            self.value = float(value)
        
        if(weight == 0):
            weight = 1
        else:
            self.weight = float(weight)
    
    '''
    Returns the weight of the item.
    '''
    def getWeight(self):
        return self.weight
    '''
    Returns the Value of the item.
    '''
    def getValue(self):
        return self.value
    '''
    Returns the Name of the item.
    '''
    def getName(self):
        return self.name
    '''
    Overridden String function. Analogous to toString() of Java.
    '''
    def __str__(self):
        result = '|' + self.getName() + ' | ' + str(self.getWeight()) + '|'
        return result
#-----------------------------------------------------------------------------
