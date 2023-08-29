from Data_store import FileWriter, FileHandler
from functions import menu, balance, account_balance_note, sell, buy, list_overview, inventory_overview, history_overview, inventory_correction, bad_response

run = True
load_data = FileHandler("history.txt", "balance.txt", "inventory.json")
history = load_data.history
account_balance = load_data.account_balance
inventory = load_data.inventory
while run:
    command_check = True
    while command_check:
        menu()
        try:
            command = int(input(": "))
            if command == 1:
                account_balance += balance(history)
                account_balance_note(account_balance)
                command_check = False
            elif command == 2:
                account_balance += sell(history, inventory)
                account_balance_note(account_balance)
                command_check = False
            elif command == 3:
                account_balance -= buy(account_balance, history, inventory)
                account_balance_note(account_balance)
                command_check = False
            elif command == 4:
                account_balance_note(account_balance)
                command_check = False
            elif command == 5:
                list_overview(inventory)
                command_check = False
            elif command == 6:
                inventory_overview(inventory)
                command_check = False
            elif command == 7:
                history_overview(history)
                command_check = False
            elif command == 8:
                inventory_correction(history, inventory)
                command_check = False
            elif command == 9:
                command_check = False
                run = False
                save_data = FileWriter(
                    "history.txt", "balance.txt", "inventory.json")
                save_data.save_history(history)
                save_data.save_balance(account_balance)
                save_data.save_inventory(inventory)
            else:
                bad_response()
        except ValueError:
            bad_response()
