def menu():
    print("*" * 100)
    print("WYBIERZ AKCJE:")
    print("Saldo: 1")
    print("Sprzedaż: 2")
    print("Zakup: 3")
    print("Konto: 4")
    print("Lista: 5")
    print("Magazyn: 6")
    print("Przeglad: 7")
    print("Korekty w magazynie: 8")
    print("Koniec: 9")
    print("*" * 100)


def account_balance_note(account_balance):
    print(f"Obecny stan konta: {round(account_balance,2)} PLN")


def bad_response():
    print("*" * 10)
    print("Blad.")
    print("Sprobuj ponownie.")
    print("*" * 10)


def confirm(user_input):
    user_confirm = True
    while user_confirm:
        print(f"Czy podana wartosc: \"{user_input}\" jest poprawna?")
        print("Tak: Y")
        print("Nie: N")
        confirm_input = (input(": ")).upper()
        if confirm_input == "Y":
            user_confirm = False
            return True
        elif confirm_input == "N":
            user_confirm = True
            return False
        else:
            bad_response()
            user_confirm = True


def history_overview(history):
    if len(history) == 0:
        print("Nie wykonano żadnych operacji.")
    else:
        start = None
        while not isinstance(start, int):
            try:
                print("Podaj początkowy krok przeglądu.")
                print("Wprowadz 0 aby wyswietlić od początku.")
                start = int(input(": "))
                if start < 0:
                    bad_response()
                    start = None
                elif start > len(history):
                    print(
                        f"Bład. Dotychczasowa liczba wykonanych kroków: {len(history)}")
                    start = None
            except ValueError:
                bad_response()
                start = None
        stop = None
        while not isinstance(stop, int):
            try:
                print("Podaj końcowy krok przeglądu.")
                print("Wprowadz 0 aby wyswietlić do końca.")
                stop = int(input(": "))
                if stop < 0:
                    bad_response()
                    stop = None
                elif stop == 0:
                    stop = len(history)
                elif stop < start:
                    print(
                        "Błąd. Krok końcowy nie może być mniejszy niż krok początkowy.")
                    stop = None
                elif stop > len(history):
                    print(
                        f"Bład. Dotychczasowa liczba wykonanych kroków: {len(history)}")
                    stop = None
            except ValueError:
                bad_response()
        if start >= 1:
            start -= 1
        if stop == 0:
            stop = None
        print("*" * 10 + " HISTORIA " + "*" * 10)
        for step, message in enumerate(history[start:stop]):
            print(f"{step + start + 1}.: {message}")
        print("*" * 30)


def decimal_count_check(number, message):
    decimal_count = 3
    while decimal_count > 2:
        number = float(
            input(message).replace(",", "."))
        decimal_count = len(str(number).split(".")[1])
        if decimal_count > 2:
            bad_response()
        else:
            return number


def check_if_number_positive(confirmation_status, number, message):
    if confirmation_status == False:
        return None
    else:
        if number <= 0:
            print(message)
            return None
        else:
            return number


def item_not_in_inventory():
    print("Nie ma takiego przedmiotu w magazynie.")
    print("Czy spróbować ponownie?")
    print("Tak: Y")
    print("Nie: N")
    user_confirm = str(input(": ")).upper()
    if user_confirm == "N":
        return False
    elif user_confirm == "Y":
        return True
    else:
        bad_response()


def continue_request():
    print("Czy chcesz kontynuować edycje przedmiotów?")
    print("Tak: Y")
    print("Nie: N")
    user_confirm = str(input(": ")).upper()
    if user_confirm == "N":
        return False
    elif user_confirm == "Y":
        return True
    else:
        bad_response()


def break_point():
    print("Czy chcesz przerwać?")
    print("Tak: Y")
    print("Nie: N")
    user_confirm = str(input(": ")).upper()
    if user_confirm == "N":
        return False
    elif user_confirm == "Y":
        return True
    else:
        bad_response()


def buy(account_balance, history, inventory):
    item_name = None
    while not isinstance(item_name, str):
        item_name = str(input("Podaj nazwe przedmiotu: "))
        item_name_confirm = confirm(item_name)
        if item_name_confirm == False:
            item_name = None
    balance_check = False
    while not balance_check:
        item_quantity = None
        while not isinstance(item_quantity, int):
            try:
                item_quantity = int(
                    input("Podaj liczbe zakupionych przedmiotów: "))
                item_quantity_confirm = confirm(item_quantity)
                item_quantity = check_if_number_positive(
                    item_quantity_confirm, item_quantity, "Bład. Liczba kupowanych sztuk nie może być mniejsza lub równa 0.")
            except ValueError:
                bad_response()
        cost_price = None
        while not isinstance(cost_price, float):
            try:
                cost_message = "Podaj cenę zakupu dla jednej sztuki towaru: "
                cost_price = decimal_count_check(cost_price, cost_message)
                cost_confirm = confirm(cost_price)
                cost_price = check_if_number_positive(
                    cost_confirm, cost_price, "Bład. Cena zakupu nie może być mniejsza lub równa 0.")
            except ValueError:
                bad_response()
        purchase_price = item_quantity * cost_price
        if account_balance - purchase_price < 0:
            print(
                f"Błąd. Nie można zakupić przedmiotu \"{item_name}\" w ilości: {item_quantity}, ponieważ saldo konta nie może być ujemne")
            print("Spróbuj ponownie.")
            stop_request = break_point()
            if stop_request:
                purchase_price = 0
                return purchase_price
            cost_price = None
            item_quantity = None
            balance_check = False
        else:
            balance_check = True
    list_price = None
    while not isinstance(list_price, float):
        try:
            list_message = "Podaj docelową cene sprzedaży 1 sztuki towaru: "
            list_price = decimal_count_check(list_price, list_message)
            list_price_confirm = confirm(list_price)
            list_price = check_if_number_positive(
                list_price_confirm, list_price, "Bład. Cena sprzedaży nie może być mniejsza lub równa 0.")
        except ValueError:
            bad_response()
    history_message = f"Zakupiono przedmiot: \"{item_name}\", w ilości: {item_quantity}. Cena za sztuke: {round(cost_price, 2)} PLN. Łączna cena za zamówienie: {round(purchase_price, 2)} PLN. Cene sprzedaży produktu ustalono na: {round(list_price, 2)} PLN."
    history.append(history_message)
    print(history_message)
    if item_name.upper() not in inventory:
        inventory[item_name.upper()] = {
            "item_name": item_name,
            "list_price": list_price,
            "quantity": item_quantity
        }
    else:
        inventory[item_name.upper()]["list_price"] = list_price
        inventory[item_name.upper()]["quantity"] += item_quantity
    available_item_quantity = inventory.get(
        item_name.upper(), {}).get("quantity")
    print(
        f"Dostępna ilość przedmiotu \"{item_name}\": {available_item_quantity}")
    return purchase_price


def balance(history):
    amount = None
    while not isinstance(amount, float):
        try:
            balance_message = "Podaj kwote do dodania/odjecia z konta: "
            amount = decimal_count_check(amount, balance_message)
            amount_confirm = confirm(amount)
            if amount_confirm == True:
                if amount > 0:
                    history_message = f"Do konta dodano: {amount} PLN."
                    history.append(history_message)
                elif amount < 0:
                    history_message = f"Z konta odjęto: {amount} PLN."
                    history.append(history_message)
                return amount
            if amount_confirm == False:
                amount = None
        except ValueError:
            bad_response()


def list_overview(inventory):
    print("*" * 30)
    print("PEŁEN WYKAZ MAGAZYNU")
    print("*" * 10)
    for item_name in inventory:
        name = inventory.get(item_name, {}).get("item_name")
        quantity = inventory.get(item_name, {}).get("quantity")
        list_price = inventory.get(item_name, {}).get("list_price")
        print("*" * 10)
        print(f"Przedmiot: {name}")
        print(f"Liczba dostępnych sztuk: {quantity}")
        print(f"Cena: {round(list_price, 2)} PLN")
    print("*" * 30)


def inventory_overview(inventory):
    item = None
    while not item:
        item = str(input("Podaj nazwe przedmiotu: ")).upper()
        if item not in inventory:
            user_confirm = item_not_in_inventory()
            if not user_confirm:
                break
            else:
                item = None
        else:
            quantity = inventory[item]["quantity"]
            name = inventory.get(item, {}).get("item_name")
            print(f"Stan magazynu dla przedmiotu \"{name}\": {quantity}.")


def sell(history, inventory):
    item_to_sell = None
    while not isinstance(item_to_sell, str):
        item_to_sell = str(
            input("Podaj nazwę sprzedawanego przedmiotu: ")).upper()
        if item_to_sell not in inventory:
            print("Podany produkt nie znajduje się w magazynie.")
            return 0
        else:
            item_name = inventory.get(item_to_sell, {}).get("item_name")
            list_price = inventory.get(item_to_sell, {}).get("list_price")
            quantity = inventory.get(item_to_sell, {}).get("quantity")
            selling_quantity = None
            while not isinstance(selling_quantity, int):
                try:
                    selling_quantity = int(
                        input("Podaj liczbe sprzedawanych przedmiotów: "))
                    confirm_selling_quantity = confirm(selling_quantity)
                    selling_quantity = check_if_number_positive(
                        confirm_selling_quantity, selling_quantity, "Błąd. Liczba sprzedawanych produktów nie może być mniejsza lub równa 0.")
                except ValueError:
                    bad_response()
                    selling_quantity = None
                if selling_quantity == None:
                    continue
                else:
                    available_quantity_left = quantity - selling_quantity
                    if available_quantity_left >= 0:
                        break
                    else:
                        print(
                            "Brak wystarczającej ilości dostępnych produktów do sprzedaży. Spróbuj sprzedać mniejszą ilość.")
                        stop_request = break_point()
                        if stop_request:
                            selling_price = 0
                            return selling_price
                        selling_quantity = None
            selling_price = selling_quantity * list_price
            message = f"Sprzedaż produktu \"{item_name}\". Ilość sprzedawanych sztuk: {selling_quantity}. Łączna cena sprzedaży: {round(selling_price, 2)} PLN"
            confirm_selling = confirm(message)
            if not confirm_selling:
                item_to_sell = None
            else:
                inventory[item_to_sell]["quantity"] = available_quantity_left
                history_message = f"Sprzedano \"{item_name}\" w ilość sztuk: {selling_quantity}. Cena sprzedaży: {round(selling_price, 2)} PLN."
                history.append(history_message)
                return selling_price


def inventory_correction(history, inventory):
    item = str(input("Wprowadź nazwę przedmiotu: "))
    if item.upper() not in inventory:
        print(f"W magazynie nie ma przedmiotu o nazwie: \"{item}\"")
    else:
        old_item_name = inventory.get(item.upper(), {}).get("item_name")
        old_list_price = inventory.get(item.upper(), {}).get("list_price")
        old_quantity = inventory.get(item.upper(), {}).get("quantity")
        print("*" * 10)
        print(
            f"Przedmiot: {old_item_name}, Cena: {round(old_list_price, 2)} PLN, Liczba dostępnych sztuk: {old_quantity}")
        print("*" * 10)
        history_message = f"Rozpoczeto edycje przedmiotu \"{item}\"."
        history.append(history_message)
        user_confirm = True
        while user_confirm:
            print("wprowadz komende do edycji")
            print("Zmiana nazwy przedmiotu: NAZWA")
            print("Zmiana ceny: CENA")
            print("Zmiana ilości dostępnych sztuk: LICZBA")
            print("Wyjdź: EXIT")
            command = str(input(": ")).upper()
            if command == "NAZWA":
                new_item_name = str(input("Wprowadź nową nazwę: "))
                item_data = inventory.pop(item.upper())
                item_data["item_name"] = new_item_name
                inventory[new_item_name.upper()] = item_data
                history_message = f"Ustawiono nową nazwę przedmiotu: \"{new_item_name}\"."
                history.append(history_message)
                print("Zmiana nazwy przedmiotu. Edycja zostaje zamknięta.")
                user_confirm = False
            elif command == "CENA":
                new_list_price = None
                while not isinstance(new_list_price, float):
                    try:
                        list_message = "Podaj nową cene sprzedaży 1 sztuki towaru: "
                        new_list_price = decimal_count_check(
                            new_list_price, list_message)
                        list_price_confirm = confirm(new_list_price)
                        new_list_price = check_if_number_positive(
                            list_price_confirm, new_list_price, "Bład. Cena sprzedaży nie może być mniejsza lub równa 0.")
                    except ValueError:
                        bad_response()
                inventory[item.upper()]["list_price"] = new_list_price
                history_message = f"Ustawiono nową cenę przedmiotu: {round(new_list_price, 2)} PLN."
                history.append(history_message)
                user_confirm = continue_request()
            elif command == "LICZBA":
                new_quantity = None
                while not isinstance(new_quantity, int):
                    try:
                        new_quantity = int(
                            input("Podaj liczbe dostępnych przedmiotów: "))
                        item_quantity_confirm = confirm(new_quantity)
                        new_quantity = check_if_number_positive(
                            item_quantity_confirm, new_quantity, "Bład. Liczba dostępnych sztuk nie może być mniejsza lub równa 0.")
                    except ValueError:
                        bad_response()
                inventory[item.upper()]["quantity"] = new_quantity
                history_message = f"Zmieniono liczbę dostepnych sztuk przedmiotu: {new_quantity}"
                history.append(history_message)
                user_confirm = continue_request()
            elif command == "EXIT":
                user_confirm = False
            else:
                bad_response()
        history_message = f"Zakończono edycje przedmiotu: \"{item}\""
        history.append(history_message)
