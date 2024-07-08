class Customer:

    customers = []

    def __init__(self,code,nom,telephone,adresse,email):

        self.id = code
        self.name = nom
        self.phone = telephone
        self.adress = adresse
        self.mail = email

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
                    """)
        else:
            print("Il n'y a aucun client!")

    @classmethod
    def add_customer(cls) :

        your_id = input("Veuillez svp entrer le code client : ")

        while not your_id.isalnum():
            print("Mauvais code !")
            your_id = input("Veuillez svp entrer le code client : ")

        your_name = input("Veuillez svp entrer le nom du client : ")

        while not your_name.isalpha():
            print("Mauvaise entrée !")
            your_name = input("Veuillez svp entrer votre nom : ")

        your_phone = input("Veuillez svp entrer le numero du client : ")

        while not (your_phone.isdigit() and len((your_phone)) == 9):
            print("Mauvaise entrée !")
            your_phone = input("Veuillez svp entrer le numero du client : ")

        your_adress = input("Veuillez svp entrer l'adresse du client : ")

        while not your_adress.isalpha():
            print("Mauvaise entrée !")
            your_adress = input("Veuillez svp entrer l'adresse du client : ")

        your_mail = input("Veuillez svp entrer l'email du client : ")

        new_customer = {
                    "Code" : your_id,
                    "Nom" : your_name,
                    "Téléphone" : your_phone,
                    "Adresse" : your_adress,
                    "Email" : your_mail
        }

        cls.customers.append(new_customer)

        print("Client ajouté avec succès !")

    @classmethod
    def delete_customer(cls) :

        to_delete = input("Veuillez svp entrer le code du client à supprimer : ")

        while not to_delete.isalnum():
            print("Mauvais code !")
            to_delete = input("Veuillez svp entrer le code du client à supprimer : ")

        for customer in cls.customers :

            if customer["id"] == to_delete :
                cls.customers.remove(customer)
                print("***Client supprimé !***")

            else :
                print("***Client inexistant !***")

Customer.add_customer()
Customer.display_customers()
#Customer.delete_customer()
#Customer("D1","TARIK","781286853","DAKAR","0753habiba.fatima@gmail.com")
#print(Customer.customers)
    