from transaction import *
import sys


def main_menu():

    print("""
          
          Menu

        1 - Gestion des clients
        2 - Gestion des transactions
        3 - Sortir
          
    """)

main_menu()
choice = input("Veuillez svp choisir une option : ")
while not (choice.isdigit() and 1 <= int(choice) <= 3):
    choice = input("Veuillez svp choisir une option : ")

while int(choice) != 3 :

    if int(choice) == 1 :

        menu_customers()
        customer_management_choice = input("Veuillez svp choisir une option : ")
        while not (customer_management_choice.isdigit() and 1 <= int(customer_management_choice) <= 5):
            customer_management_choice = input("Veuillez svp choisir une option : ")

        if int(customer_management_choice) == 1 :

            Customer.display_customers(Customer.customers)

        elif int(customer_management_choice) == 2 :

            Customer.add_customer()

        elif int(customer_management_choice) == 3 : 

            Customer.delete_customer()  

        elif int(customer_management_choice) == 4 :

            Customer.change_info() 

        else:
            Customer.customer_balance(Customer.customers)

        menu_customers()
        customer_management_choice = input("Veuillez svp choisir une option : ")
        while not (customer_management_choice.isdigit() and 1 <= int(customer_management_choice) <= 5):
            customer_management_choice = input("Veuillez svp choisir une option : ")

    elif int(choice) == 2 :

        menu_transactions()
        transactions_management_choice = input("Veuillez svp choisir une option : ")
        while not (transactions_management_choice.isdigit() and 1 <= int(transactions_management_choice) <= 4):
            transactions_management_choice = input("Veuillez svp choisir une option : ")        

        if int(transactions_management_choice) == 1 :

            Transaction.display_transactions(Transaction.transactions)

        elif int(transactions_management_choice) == 2 :

            Transaction.customer_transactions(Transaction.transactions)

        elif int(transactions_management_choice) == 3 :

            Transaction.add_transaction()

        else:
            Transaction.change_balance()
            
        menu_transactions()
        transactions_management_choice = input("Veuillez svp choisir une option : ")
        while not (transactions_management_choice.isdigit() and 1 <= int(transactions_management_choice) <= 4):
            transactions_management_choice = input("Veuillez svp choisir une option : ")  

    main_menu()
    choice = input("Veuillez svp choisir une option : ")
    while not (choice.isdigit() and 1 <= int(choice) <= 3):
        choice = input("Veuillez svp choisir une option : ")

else:
    sys.exit

