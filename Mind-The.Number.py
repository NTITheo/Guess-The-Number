import random

loop = True
loop2 = True
while loop2==True:
    number = random.randint (1,10)
    while loop==True:
        print("1, 2, 3, 4, 5, 6, 7, 8, 9, 10")
        val = int(input("Gissa nummer: "))
        if val == number:
            print ("Du gissa rätt")
            loop = False
        elif val > number:
            print ("Du gissa för högt")
        elif val < number:
            print ("Du gissa för lågt")
        else:
            loop=False
            exit()




