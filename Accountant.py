from Data_store import FileWriter, FileHandler
from functions import menu, balance, account_balance_note, sell, buy, list_overview, inventory_overview, history_overview, inventory_correction, bad_response
from Manager import Manager

manager = Manager()

load_data = FileHandler("history.txt", "balance.txt", "inventory.json")
history = load_data.history
account_balance = load_data.account_balance
inventory = load_data.inventory

# Change balance


@manager.assign(1)
def manage_balance(manager):
    global account_balance
    account_balance += balance(history)
    account_balance_note(account_balance)


# Sell
@manager.assign(2)
def manage_sell(manager):
    global account_balance
    account_balance += sell(history, inventory)
    account_balance_note(account_balance)


# Buy
@manager.assign(3)
def manage_buy(manager):
    global account_balance
    account_balance -= buy(account_balance, history, inventory)
    account_balance_note(account_balance)


# Account balance
@manager.assign(4)
def manage_account_balance(manager):
    account_balance_note(account_balance)


# List
@manager.assign(5)
def manage_list_overview(manager):
    list_overview(inventory)


# Inventory
@manager.assign(6)
def manage_inventory_overview(manager):
    inventory_overview(inventory)


# History
@manager.assign(7)
def manage_history_overview(manager):
    history_overview(history)


# Inventory corrections
@manager.assign(8)
def manage_inventory_correction(manager):
    inventory_correction(history, inventory)


# Exit
@manager.assign(9)
def manage_exit(manager):
    global run
    run = False
    save_data = FileWriter(
        "history.txt", "balance.txt", "inventory.json")
    save_data.save_history(history)
    save_data.save_balance(account_balance)
    save_data.save_inventory(inventory)


# Run app
run = True
while run:
    menu()
    try:
        command = int(input(": "))
        manager.execute(command)
    except ValueError:
        print("Akcja niezdefiniowana")
