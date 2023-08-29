from Data_store import FileWriter, FileHandler
from functions import menu, balance, account_balance_note, sell, buy, list_overview, inventory_overview, history_overview, inventory_correction, bad_response
from Manager import Manager

manager = Manager()


@manager.assign("balance")
def manage_balance(manager):
    account_balance += balance(history)
    account_balance_note(account_balance)


@manager.assign("sell")
def manage_sell(manager):
    account_balance += sell(history, inventory)
    account_balance_note(account_balance)


@manager.assign("buy")
def manage_buy(manager):
    account_balance -= buy(account_balance, history, inventory)
    account_balance_note(account_balance)


@manager.assign("account_balance")
def manage_account_balance(manager):
    account_balance_note(account_balance)


@manager.assign("list")
def manage_list_overview(manager):
    list_overview(inventory)


@manager.assign("inventory")
def manage_inventory_overview(manager):
    inventory_overview(inventory)


@manager.assign("history")
def manage_history_overview(manager):
    history_overview(history)


@manager.assign("inventory_correction")
def manage_inventory_correction(manager):
    inventory_correction(history, inventory)


@manager.assign("exit")
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
load_data = FileHandler("history.txt", "balance.txt", "inventory.json")
history = load_data.history
account_balance = load_data.account_balance
inventory = load_data.inventory
while run:
    menu()
    try:
        command = int(input(": "))
        manager.execute(command)
    except ValueError:
        bad_response()
