class Customer:

    customers = []

    customers_num = 0

    def __init__(self,code,nom,telephone,adresse,email,solde=0):

        self.id = code
        self.name = nom
        self.phone = telephone
        self.adress = adresse
        self.mail = email
        self.balance = solde

    def display_customers(customers):

        if len(customers) != 0 :

            print("***Liste des clients***")

            for customer in customers :

                print(f"""
                    Code : {customer["id"]}
                    Nom : {customer["name"]}
                    Téléphone : {customer["phone"]}
                    Adresse : {customer["adress"]}
                    Email : {customer["mail"]}
                    Solde : {customer["balance"]}
                    """)
        else:
            print("Il n'y a aucun client!")

    
    def add_customer(self) :

        your_id = f"C0{Customer.customers_num}"

        your_name = input("Veuillez svp entrer le nom du client : ")

        while not your_name.isalpha():
            print("Mauvaise entrée !")
            your_name = input("Veuillez svp entrer votre nom : ")

        your_phone = input("Veuillez svp entrer le numero du client : ")

        while not (your_phone.isdigit() and len((your_phone)) == 9):
            print("Mauvaise entrée !")
            your_phone = input("Veuillez svp entrer le numero du client : ")

        your_adress = input("Veuillez svp entrer l'adresse du client : ")

        your_mail = input("Veuillez svp entrer l'email du client : ")

        new_customer = {
                    "id" : your_id,
                    "name" : your_name,
                    "phone" : your_phone,
                    "adress" : your_adress,
                    "mail" : your_mail,
                    "balance" : self.balance
        }

        Customer.customers.append(new_customer)

        Customer.customers_num += 1

        print(f"Client {your_id} ajouté avec succès !")

    @classmethod
    def delete_customer(cls) :

        to_delete = input("Veuillez svp entrer le code du client à supprimer : ")

        while not to_delete.isalnum():
            print("Mauvais code !")
            to_delete = input("Veuillez svp entrer le code du client à supprimer : ")

        for customer in cls.customers :

            if customer["id"] == to_delete :
                cls.customers.remove(customer)
                print(f"***Client {customer["id"]} supprimé !***")
                break

        else :
            print(f"***Client {to_delete} inexistant !***")

    @classmethod
    def change_info(cls):

        to_change = input("Veuillez svp entrer le code du client à modifier : ")

        for customer in cls.customers :

            if customer["id"] == to_change : 

                print("""
                    Quelle information voulez vous changer ?
                        1- le nom
                        2- le numero de téléphone
                        3- l'adresse
                        4- l'email
                    """)
                numero = input("Veuillez svp entrer le numero : ")

                while not (numero.isdigit() and 1 <= int(numero) <= 4) :
                    print("Veuillez choisir un chiffre correspondant aux propositions !")
                    numero = input("Veuillez svp entrer le numero : ")

                if int(numero) == 1 :

                    new_name = input("Veuillez svp entrer le nouveau nom du client : ")

                    while not new_name.isalpha():
                        print("Mauvaise entrée !")
                        new_name = input("Veuillez svp entrer le nouveau nom du client : ")

                    customer["name"] = new_name

                    print(f"***Nom du client {customer["id"]} modifié !***")

                elif int(numero) == 2 :

                    new_phone = input("Veuillez svp entrer le nouveau numero du client : ")

                    while not (new_phone.isdigit() and len((new_phone)) == 9):
                        print("Mauvaise entrée !")
                        new_phone = input("Veuillez svp entrer le nouveau numero du client : ")

                    customer["phone"] = new_phone

                    print(f"***Numero du client {customer["id"]} modifié !***")

                elif int(numero) == 3 :

                    new_adress = input("Veuillez svp entrer la nouvelle adresse du client : ")

                    customer["adress"] = new_adress

                    print(f"***Adresse du client {customer["id"]} modifiée !***")

                else :
                    new_mail = input("Veuillez svp entrer le nouvel email du client : ")

                    customer["mail"] = new_mail

                    print(f"***Email du client {customer["id"]} modifié !***")
        else : 
            print("***Client inexistant !***")

    def customer_balance(customers):
        the_customer = input("Veuillez svp entrer le code du client dont vous voulez voir le solde : ")

        for customer in customers:
             if customer["id"] == the_customer:
                print(f"""
                    Code : {customer["id"]}
                    Nom : {customer["name"]}
                    Solde : {customer["balance"]}
                """)
        
        else:
            print("***Client inexistant !***")




#Customer.add_customer(self="habib")
#Customer.add_customer()
#Customer.display_customers(Customer.customers)
#Customer.change_info()
#Customer.display_customers(Customer.customers)
#Customer.customer_balance(Customer.customers)
#Customer.delete_customer()
#Customer("D1","TARIK","781286853","DAKAR","0753habiba.fatima@gmail.com")
#print(Customer.customers)
    