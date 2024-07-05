number = input("Veuillez svp entrer un nombre : ")

while not number.isdigit():
    number = input("Veuillez svp entrer un nombre : ")

for num in range(1,int(number)):
    print(num)