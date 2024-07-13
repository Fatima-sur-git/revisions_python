import datetime
from customer import*

def menu_transactions():
     
     print("""
           
        Gestion des transactions
                
        1- Afficher toutes les transactions
        2- Afficher les transactions d'un client
        3- Ajouter la transaction entre deux clients
        4- Modifier le solde d'un client
                
""")

class Transaction:

    transactions = []

    transactions_num = 0
    
    def __init__(self,ref_paiement,code_emmeteur,code_recepteur,date_transaction,montant,canal):

        self.ref = ref_paiement
        self.issuer_id = code_emmeteur
        self.recipient_id = code_recepteur
        self.transaction_date = date_transaction
        self.amount = montant
        self.method = canal

    def display_transactions(transactions):

        if len(transactions)!= 0 :
            print("***Liste des transactions***")
            for transaction in transactions:
                print(f""" 
                    Référence de paiement : {transaction["ref"]}
                    Code émmeteur : {transaction["issuer_id"]}
                    Code récepteur : {transaction["recipient_id"]}
                    Date de la transaction : {transaction["transaction_date"]}
                    Montant : {transaction["amount"]} F CFA
                    Canal : {transaction["method"]}
                     """)
        else : 
            print("Il n'y a aucune transaction!")


    def customer_transactions(transactions):
        
        customer = input("Veuillez svp entrer le code du client dont vous aimeriez afficher les transactions : ")
        while not customer.isdigit():
            print("le code ne doit contenir que des chiffres!")
            customer = input("Veuillez svp entrer le code du client dont vous aimeriez afficher les transactions : ")

        for transaction in transactions:
            
            if customer == transaction["issuer_id"]:
                print(f""" 
                    Référence de paiement : {transaction["ref"]}
                    Code émmeteur : {transaction["issuer_id"]}
                    Code récepteur : {transaction["recipient_id"]}
                    Date de la transaction : {transaction["transaction_date"]}
                    Montant : {transaction["amount"]}
                    Canal : {transaction["method"]}
                     """)
                
        else:
            print("Client inexistant!")

    def add_transaction():
        
        transac_ref = f"00{Transaction.transactions_num}"

        code_emmeteur = input("Veuillez svp entrer le code de l'emmeteur de la transaction : ")

        while not code_emmeteur in Customer.customers:
            print("Ce client n'existe pas!")
            code_emmeteur = input("Veuillez svp entrer le code de l'emmeteur de la transaction : ")

        code_recepteur = input("Veuillez svp entrer le code du recepteur de la transaction : ")
        while not code_recepteur in Customer.customers:
            print("Ce client n'existe pas!")
            code_recepteur = input("Veuillez svp entrer le code du recepteur de la transaction : ")

        date_transaction = datetime.datetime.now()

        montant = input("Veuillez svp entrer le montant de la transaction")
        while not montant.isdigit():
            montant = input("Veuillez svp entrer le montant de la transaction")

        print("""
                *Listes des canaux*
              
                1- Orange Money
                2- Wave
                3- Free Money
                4- Virement bancaire
            """)
        
        num = input("Veuillez svp entrer le numero correspondant à votre canal : ")
        while not (num.isdigit() and 1 <=int(num)< 5) :
            print("Veuillez svp entrer un chiffre entre 1 et 4 !")
            num = input("Veuillez svp entrer le numero correspondant à votre canal : ")

        if int(num) == 1:
            canal = "Orange Money" 
        elif int(num) == 2:
            canal = "Wave"
        elif int(num) == 3:
            canal = "Free Money"
        else:
            canal = "Virement bancaire"

        new_transaction = {

            "ref" : transac_ref,
            "issuer_id" : code_emmeteur,
            "recipient_id" : code_recepteur,
            "transaction_date" : date_transaction,
            "amount" : montant,
            "method" : canal  

        }

        for customer in Customer.customers :
            if code_emmeteur == customer["id"]:
                customer["balance"] -= montant
                break

        for customer in Customer.customers :
            if code_recepteur == customer["id"]:
                customer["balance"] += montant
                break


        Transaction.transactions.append(new_transaction)

        Transaction.transactions_num +=1

        print(f"Transaction {new_transaction["ref"]} ajoutée !")

    def change_balance():

        the_customer = input("Veuillez svp entrer le code du client dont vous voulez modifier le solde : ")

        for customer in Customer.customers:
            if the_customer == customer["id"] :
                print(f"""
                        Code : {customer["id"]}
                        Nom : {customer["name"]}
                        Solde : {customer["balance"]}
                        """)
                new_solde = input("Veuillez svp entrer le nouveau solde : ")
                customer["balance"] = new_solde

                print(f"""
                        Code : {customer["id"]}
                        Nom : {customer["name"]}
                        Solde : {customer["balance"]}
                        """)
                
                print("**Solde modifié!**")
                
        else:
            print("Client inexistant!")





        
