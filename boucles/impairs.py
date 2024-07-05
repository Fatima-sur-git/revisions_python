number = range(1,21)
count = 0
while count<10 :
    for num in number:
        if int(num) % 2 != 0:
            print (num)
            count += 1
