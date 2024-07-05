note = input("Veuillez svp entrer votre note (entre 0 et 20) : ")
while not (note.isdigit() and 0 <= int(note) <= 20) :
    print("Entrée incorrecte")
    note = input("Veuillez svp entrer votre notre (entre 0 et 20) : ")
else:
    if 18 <= int(note) <= 20 :
        print("Excellent")
    elif 16 <= int(note) < 18 :
        print("Très bien")
    elif 14 <= int(note) < 16 :
        print("Bien")
    elif 12 <= int(note) < 14 :
        print("Satisfaisant")
    elif 10 <= int(note) < 12 :
        print("Passable")
    else:
        print("Echec")