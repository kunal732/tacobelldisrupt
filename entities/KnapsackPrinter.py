class KnapsackPrinter(object):
    '''
    Constructor. This takes in details days in the conference.
    '''
    def __init__(self, listOfItemsChosen):
        self.listOfChosenItems = listOfItemsChosen
        # Use an empty list if none to avoid unnecessary exceptions ;-).
        if self.listOfChosenItems == None:
            self.listOfChosenItems = []
    '''
    Print Items.
    '''
    def printItemsChosen(self):
        body= """TacoBell Items to Purchase.<br>
              ----------------------------------------<br>
              | Name | Cost | Calories|<br><br>"""
        weightAccumulated = 0
        caloriesAccumulated = 0
        for item in self.listOfChosenItems:        
            body = body + item.getName() + ' | ' + str(item.getWeight()) + ' | ' + str(item.getValue()) + ' |<br>'
            weightAccumulated = weightAccumulated + item.getWeight()
            caloriesAccumulated = caloriesAccumulated + item.getValue()
        body= body+  '<br><br>Total Cost for Max Calories within your Budget: <br>' + str(weightAccumulated)
        body = body + '----------------------------------------<br>'+ 'Total Calories for your Budget:'+str(caloriesAccumulated)
        print body 
        return body
#--------------------------------------------------------------------------------------
