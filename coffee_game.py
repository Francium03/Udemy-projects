menu = {
    "espresso":
        {
            "ingredient":
                {
                    "water": 50,
                    "coffee": 18,
                    "milk": 0
                },
            "cost": 1.5
        },
    "latte":
        {
            "ingredients":
                {
                    "water": 200,
                    "coffee": 24,
                    "milk": 150},
            "cost": 2.5
        },
    "cappuccino":
        {
            "ingredients":
                {
                   "water": 250,
                   "coffee": 24,
                   "milk": 100
                },
            "cost": 3.0
          }
      }
money_bank = 0
resources = {
    "water": 600,
    "coffee": 500,
    "milk": 400
            }


def is_transaction_successful(amount_paid, amount_should_paid):
    if amount_paid >= amount_should_paid:
        change = round(amount_paid - amount_should_paid, 2)
        print(f"Here is ${change} in change. ")
        global money_bank
        money_bank += amount_should_paid
        return True
    else:
        print(f"Sorry that's not enough money. Money refunded. ")
        return False


def coin():
    print("Please insert coins:")
    quarters = int(input("How many quarters?: "))*0.25
    dimes = int(input("How many dimes?: "))*0.10
    nickles = int(input("How many nickles?: "))*0.05
    pennies = int(input("How many pennies?: "))*0.01
    total_money = quarters+dimes+nickles+pennies
    return total_money


def make_coffee(coffee_drink, coffee_drink_ingredients):
    for item in coffee_drink_ingredients:
        resources[item] -= coffee_drink_ingredients[item]
    print(f"Here is your {coffee_drink}")


def is_enough_ingredients(drink_ingredients):
    for item in drink_ingredients:
        if drink_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}. ")
            return False
    return True


game = True
while game:
    choice = input("What would you like?: (espresso/latte/cappuccino): ")
    if choice == "off":
        game = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Milk: {resources['milk']}ml ")
        print(f"Money: ${money_bank}")
    else:
        drink = menu[choice]
        if is_enough_ingredients(drink["ingredients"]):
            payment = coin()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
