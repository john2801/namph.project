MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 15000,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 20000,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 25000,
    },
}

profit = 0
resources = {"water": 300, "milk": 200, "coffee": 100, "money": 0}


def check_resources(flavor):
    for i in resources:
        if MENU[flavor]["ingredients"][i] > resources[i]:
            print(f"Sorry there is not enough {i}.")
            return False
        else:
            return True


def check_money(flavor, money):
    flavor_money = MENU[flavor]["cost"]
    if flavor_money > money:
        print("Sorry that's not enough money. Money refunded.")
    else:
        print(f"Here is {money-flavor_money} VND in change. ")
        return True


def make_coffee(flavor):
    for i in resources:
        if i != "money":
            resources[i] = resources[i] - MENU[flavor]["ingredients"][i]


def command():
    request = input(f"what would you like? (espresso/latte/cappuccino): ")
    if request == "report":
        print(resources)
    elif request == "off":
        return "off"
    else:
        if check_resources(request):
            get_money = int(input("Please insert money: "))
            if check_money(request, get_money):
                if get_money >= MENU[request]["cost"]:
                    make_coffee(request)
                    resources["money"] = resources["money"] + MENU[request]["cost"]
                    print(f"Here is your {request} ☕")


is_on = True
while is_on:
    if command() == "off":
        is_on = False
    else:
        command()
