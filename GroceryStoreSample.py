#programmer: Harini S
#Date: 2/2/23
#Program:  Grocery Store
# menu, specials, deals, bundles
# groceryshelf = {"Tuna", 2.30 | "coffee" , 3.20}

import datetime 

done = False

fruitsByPound = ["Apples", "Bananas", "Oranges", "Guavas", "Cherries"]

fruitsByPoundPrice = [1, 2, 1, 3, 4]  # Array -- List

# 0, 1, 2

cart = []
quanity = []  # quanitity of all the items in the cart


def Inventory():
  print("Fruits in Stock: Price per pound")
  #Loop to print prices and names of fruits
  for x in range(len(fruitsByPound)):
    print(fruitsByPound[x] + " : $" + str(fruitsByPoundPrice[x]))


def actions():
  nextAction = input(
    "What do you want to do next?(Write: buy, remove or reciept) ")
  if (nextAction == "buy"):
    Shopping()
  elif (nextAction == "remove"):
    removeFunction()
  elif (nextAction == "reciept"):
    giveReciept()
  else:
    nextAction = input("Please choose one of the three above options")
    actions()


def removeFunction():
  itemToRemove = input("What would you like to remove? ")

  isInCart = False
  for x in range(len(cart)):
    if (cart[x] == itemToRemove):
      isInCart = True

  if (isInCart == False):
    print("Please choose an item in the Cart")
    removeFunction()

  cart.remove(itemToRemove)
  # cart.pop(2)
  print("Remove")
  printCart()
  actions()


def giveReciept():
  print(" ")
  print(" ")
  print(" ")
  print("-------Reciept-------")
  print("Harini's Grocery Store")
  print("123 First St")
  print("Village, IL")
  print("123-456-7890")
  print("Thursday March 2 2023")
  currentTime = datetime.datetime.now()
  formatted_time = currentTime.strftime("%H:%M:%S")
  print(formatted_time)
  print(" ")
  print("Items: ")
  subtotal = 0
  for x in range(len(cart)):
    print(cart[x] + " : $" + str(fruitsByPoundPrice[fruitsByPound.index(cart[x])] * quanity[x]))
    subtotal = subtotal + (fruitsByPoundPrice[fruitsByPound.index(cart[x])] *
                           quanity[x])
    
  print(" ")
  print("Subtotal: $" + str(subtotal))
  tax = subtotal * 0.4  #4% tax
  print("Tax: $" + str(round(tax, 2)))
  total = tax + subtotal
  print("Total: $" + str(round(total, 2)))
  done = True
  # do not circle back to another method. This is the end of the program

  # reset
  


def Shopping():
  item = input("What would you like to buy? ")
  isInList = False
  for x in range(len(fruitsByPound)):
    if (fruitsByPound[x] == item):
      isInList = True

  if (isInList == False):
    print("Please choose an item in the Inventory")
    Shopping()

  cart.append(item)
  #print("Currently this is your cart:")
  #print(cart)

  howMuch = input("How much of this product? ")
  quanity.append(int(howMuch))
  #print(quanity)
  printCart()


def printCart():
  print(" ")
  print("Here is what your cart currently looks like: ")
  for x in range(len(cart)):
    print(cart[x] + " : " + str(quanity[x]) + " - $" +
          str(fruitsByPoundPrice[fruitsByPound.index(cart[x])]) + " each")

  actions()


def main():
  if(done != True):
    print("Welcome!")
    customer = input("How may we help you? ")
  
    if (customer == "Suggest something"):
      print("Today's deal is buy 2 apples get 1 free!")
  
    Inventory()
    Shopping()


main()
