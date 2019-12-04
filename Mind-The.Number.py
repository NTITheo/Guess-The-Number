import random

loop = True
loop2 = True
while loop2==True:
    number = random.randint (1,10)
    print("1, 2, 3, 4, 5, 6, 7, 8, 9, 10")
    loop=True
    while loop==True:
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




