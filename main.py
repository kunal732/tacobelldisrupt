# coding: utf-8
'''
TacoBell Disrupt
'''
#from utility.utilities import weightInverse, valueInverse
from entities.utilities import weightInverse, valueInverse
from entities.AnItemToTake import AnItemToTake
from entities.KnapsackBuilder import KnapsackBuilder
from entities.KnapsackPrinter import KnapsackPrinter
from flask import Flask,request
import sendgrid

sg = sendgrid.SendGridClient('api_user', 'api_key')

app = Flask(__name__)

def is_float_try(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

'''
Enter the items here as tuples. Entries are of the format (String name, weight, value)
This is a list of tuples.
'''
listOfItems = [('Crunchy Taco',0.99,170),
                   ('Crunchy Taco Supreme',1.39, 200), ('Chicken Soft Taco',1.79, 160), ('Grilled Steak Soft Taco',2.29, 200),
                   ('Double Decker Taco',2.29, 350), ('Doritos Locos Taco (Nacho Cheese)',1.39, 170),
                   ('Doritos Locos Taco (Fiery)',1.39, 170), ('Doritos Locos Taco (Cool Ranch)',1.39,  200), 
                   ('Bean Burrito',1.09, 370),('Black Bean Burrito', 1.79, 390),('Chicken Burrito', 1.59, 400), 
                   ('7-Layer Burrito', 2.29, 430),
                   ('Burrito Supreme – Beef',2.69,  410), 
                   ('Smothered Burrito (Beef)',2.99, 700),('Smothered Burrito (Shredded Chicken)',3.99, 650),
                   ('Smothered Burrito (Steak)',3.99, 670), ('XXL Grilled Stuft Burrito (Beef)',3.99, 870),
                   ('XXL Grilled Stuft Burrito (Chicken)',4.79, 820), ('XXL Grilled Stuft Burrito (Steak)',4.99, 840), 
                   ('Cheesy Nachos',.99,280), ('Nacho Supreme',2.29, 450), ('Nacho Bellgrande',3.29, 760), 
                   ('Cantina Bowl (Veggie)',4.79, 510), ('Cantina Bowl (Chicken)',4.79, 530), ('Cantina Bowl (Steak)',4.99, 550), 
                   ('Cantina Burrito (Veggie)',4.79, 720), ('Cantina Burrito (Chicken)',4.79, 730), 
                   ('Cantina Burrito (Steak)',4.99, 750)
                ]#End of List.
    #Build Initial Item List from the input.
items = []
for t in listOfItems:
   i = AnItemToTake(t[0], t[1], t[2])
   items.append(i)
        
#Sort on weight of items. Smaller items first.
sortedItems = sorted(items, key = valueInverse, reverse = True)
# you can also use weight order of items to choose from.
#sortedItems = sorted(items, key = weightInverse, reverse = True)
@app.route ('/email', methods =['POST'])
def form():    
   builder = KnapsackBuilder(sortedItems)
   subject = request.form['subject']
   newsub = subject.replace("$", "")
   newsub = newsub.replace("dollars", "")
   newsub = newsub.replace("cents", "")
   newsub = newsub.replace("and", ".")
   replyto = request.form['from']
   if is_float_try(newsub):
      weightLimit = float(newsub)
      builder.packKnapSack(weightLimit)   
      printer = KnapsackPrinter(builder.getListOfItemsToTake())
      body = printer.printItemsChosen()
   else:
      body = "Please enter a dollar value in the subject line ex: 5.28 or $4.32)"
   
   message = sendgrid.Mail(to=replyto, subject='Your Taco Bell menu is ready', html=body, text=body, from_email='tacobell@sendgrid.com')
   status, msg = sg.send(message)
   return "OK"

if __name__=='__main__':
   app.run(debug=True)
