#diceroll game
import random
score=0
def rolldice(x):
    global score
    guess=random.randint(1,6)
    print("Dice roll : ",guess)
    if int(x)==guess:
        score+=5
        print("_Congrats_You won")
        print("You Got :",score,"points")
    else:
        print("_Sorry_You lose")
        print("Total points scored :",score,"points")
    WPA=input("Play one more match, enter Y to play, N to quit : ")
    if WPA in ["yes","y","Y","YES"]:
        print("Yeah_Sure")
        input_()
    else:
        print("Total points scored :",score)
        print("#GAME OVER")
        
        
        
    
def input_():
    global a
    a=input("Enter a number between '1-6' : ")
    if len(a)==1:
        if a.isdigit():
            if int(a) in [1,2,3,4,5,6]:
                rolldice(a)
            else:
                print("!!Enter a number between '1-6' only!!")
                input_()
        else:
            print("Enter a valid number")
            input_()
    else:
        print("Enter only a single digit integer number")
        input_()
input_()