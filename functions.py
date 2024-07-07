import sys

panier = []

#la fonction pour le menu
def menu():

    print ("""
           
    Choisissez parmi les 5 options suivantes:

    1- Ajouter un article dans le panier
    2- Supprimer un article du panier
    3- Afficher tous les articles
    4- Vider le panier
    5- Quitter
            
                """)
    
#fonction pour ajouter un article au panier
def add_article(your_article, the_price):
    
        article = {
            "name" : your_article,
            "price" : the_price
        }

        panier.append(article)

        print("**l'article a bien été ajouté dans votre panier**")

#fonction pour supprimer un article du panier
def delete_article(name) :

    for article in panier:
            
            if article["name"] == name:
                panier.remove(article)
                print("**l'article a été bien supprimé de votre panier**")
            else:
                print("**aucun article avec ce nom**")

#fonction pour afficher les articles du panier
def display_articles():

    if len(panier) != 0 :
            
        print("**voici la liste des articles du panier**")

        for i, article in enumerate(panier, start=1):
            print(f"""
                        **Article {i}**
                        
                        Nom de l'article : {article["name"]}
                        Prix de l'article : {article["price"]}

                        """)
    else:
        print("**Votre panier est vide!**")

#fonction pour vider le panier
def clear_all():

    if len(panier) != 0 :
            
            panier.clear()
            print("** Votre panier a bien été vidé ! **")

    else:
        print("** Votre panier est déja vide ! **")

#programme
menu()
choice = input("Quel est votre choix ? : ")

while not (choice.isdigit() and 1 <= int(choice) <= 5):
    print("mauvaise entrée, veuillez entrer une valeur entre 1 et 5")
    menu()
    choice = input("Quel est votre choix ? : ")

while int(choice) != 5 :

    if int(choice) == 1 :

        your_article = input("Entrez le nom de votre article : ")

        while not your_article.isalnum():
           your_article = input("Entrez le nom de votre article : ")

        the_price = input("Combien coute-t-il ? : ")

        while not the_price.isdigit():
            the_price = input("Combien coute-t-il ? : ")

        add_article(your_article, the_price)

    elif int(choice) == 2 :

        to_delete = input("Veuillez svp entrer le nom de l'article à supprimer : ")

        while not to_delete.isalnum():
           to_delete = input("Veuillez svp entrer le nom de l'article à supprimer : ")

        delete_article(to_delete)
        
    elif int(choice) == 3 :

        display_articles()

    elif int(choice) == 4 :

        clear_all()
        
    menu()  
    choice = input("Quel est votre choix ? : ")
    #on verifie toujours que l'option choisie est valide, tant que ce n'est pas le cas, on redemande à l'utilisateur de choisir
    while not (choice.isdigit() and 1 <= int(choice) <= 5):
        print("mauvaise entrée, veuillez entrer une valeur entre 1 et 5")
        menu()
        choice = input("Quel est votre choix ? : ")

#lorsque l'option choisie est 5, on n'affiche plus de menu et on ne demande plus à l'utilisateur de choisir.
if int(choice) == 5 : 
    print("**Fin du programme!!!**")
    sys.exit()
