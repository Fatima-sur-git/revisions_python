number = input("Veuillez svp entrer un nombre : ")

while not number.isdigit():
    number = input("Veuillez svp entrer un nombre : ")

num = 1
while num < int(number):
    print(num)
    num += 1