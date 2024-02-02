from check_function import check
from resources import *
def order_espresso():
    print("accepted currency : Rs 10, Rs 20, Rs 50")
    insert_money = int(input("insert money : "))
    if insert_money < espresso["money"]:
        print("not enough money..")
    elif insert_money == espresso["money"]:
        print("your espresso is ready")
    else:
        print(f"your espresso is ready and here is your change of {insert_money-espresso['money']} rupees")