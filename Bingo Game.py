print("Welcome in BINGO")
import numpy
import random

arr1 = random.sample(range(1, 26), 25)
ar1 = numpy.array(arr1)
arr2 = random.sample(range(1, 26), 25)
ar2 = numpy.array(arr2)
GameOver = False
Bingo = 0
Bingo1 = 0

def Print1():
    print("Your card:")
    print(ar1[:5])
    print(ar1[5:10])
    print(ar1[10:15])
    print(ar1[15:20])
    print(ar1[20:25])

def Print2():
    print("Computer's card:")
    print(ar2[:5])
    print(ar2[5:10])
    print(ar2[10:15])
    print(ar2[15:20])
    print(ar2[20:25])

def User():
    print("Now it's your turn")
    num = int(input("Enter number : "))
    if num in ar1:
        ar1[ar1 == num] = 0
        ar2[ar2 == num] = 0
    else:
        print("Invalid number. Try again.")
        return

    global Bingo, GameOver
    if check_bingo(ar1):
        Bingo += 1
        print("Your Bingo:", Bingo)
        if Bingo == 5:
            print("Congratulations! You won!")
            GameOver = True

def Computer():
    print("Now it's the computer's turn")
    num = random.choice(ar2[ar2 != 0])
    ar2[ar2 == num] = 0
    ar1[ar1 == num] = 0
    print("Computer entered:", num)

    global Bingo1, GameOver
    if check_bingo(ar2):
        Bingo1 += 1
        print("Computer's Bingo:", Bingo1)
        if Bingo1 == 5:
            print("Computer won!")
            GameOver = True

def check_bingo(card):
    for i in range(5):
        if all(card[i*5:(i+1)*5] == 0):  # Horizontal check
            return True
        if all(card[i:25:5] == 0):  # Vertical check
            return True
    if all(card[0:25:6] == 0) or all(card[4:21:4] == 0):  # Diagonal checks
        return True
    return False

while not GameOver:
    Print1()
    User()
    if GameOver:
        break
    Print2()
    Computer()
