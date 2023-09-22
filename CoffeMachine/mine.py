from data import MENU,resources


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
menu=MENU.copy()
moneySave=0

def printResource():
    global resources
    water=resources['water']
    milk=resources['milk']
    coffee=resources['coffee']
    print(f'our stock today\nwater: {water} ml\nCoffee: {coffee} gr\nMilk: {milk}\nand our save is {moneySave}$')
    askForPlay=input('do you won open the Coffee, type y for yes ?')
    if  askForPlay == "y":
        playCoffee()
        
    
def printMenu(menu):
    print('hallo we have:')
    items=list(menu.keys())
    for idx,item in enumerate(items):
        print(f'{idx} for {item}')
    choice=int(input('which number do you wont ? '))

    return menu[items[choice]]

def userPayment():
    """Returns the total calculated from coins inserted."""

    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total
def paymentSystem(price):
    userMoney= userPayment()
    if price > userMoney:
        print('its not enough')
        paymentSystem(price-userMoney)
    else:
        print(f'its your change\n{userMoney-price}')
    askForPlay=input('do you wont check our resource,type y ? ')
    if askForPlay=='y':
        printResource()

def makeTheOrder(coffeeIng):
    global resources
    resources['water']-=coffeeIng['water'] 
    resources['milk']-=coffeeIng['milk'] 
    resources['coffee']-=coffeeIng['coffee'] 
    
def playCoffee():
    global menu,moneySave
    userChose=printMenu(menu)
    makeTheOrder(userChose['ingredients'])
    price=(userChose['cost'])
    moneySave+=price
    paymentSystem(price)



playCoffee()
