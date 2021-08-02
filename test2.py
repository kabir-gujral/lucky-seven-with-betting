#betting feature, ask player how much to bet, min bet 50,purse 500 and whenever game ends i need to specify how much money left
from random import shuffle
yourvalue=None
outputDice1=None
outputDice2=None
totalmoney=500
bet=None
winnings=None 
lose=None
addmore=None
extra=None
totalloss=None
wins=0
loses=0
dice1=[1,2,3,4,5,6]
dice2=[1,2,3,4,5,6]

def betting():
    global totalmoney,bet,addmore,extra
    bet=int(input("enter the amount you want to bet : "))

def add():
    global totalmoney,addmore
    addmore=int(input("enter the amount you wanna add more : "))
    if addmore > 500:
        print('enter a value less than 500')
        add()
    totalmoney=totalmoney+addmore



 


def takeInput():
    global yourvalue
    yourvalue=input("enter above 7, below 7 or equal to 7 : ")


def diceRoll1():
    shuffle(dice1)
    outputDice1=dice1[0]
    return outputDice1

   

def diceroll2():
    global dice2,outputDice2
    shuffle(dice2)
    outputDice2=dice2[0]
    return outputDice2


def checkWin():
    a=diceRoll1()
    b=diceroll2()
    global winnings,lose,totalmoney,totalloss,wins,loses 
    if a+b > 7 and yourvalue=="above 7":
         print(f"you won you number was :{a+b}")
         wins+=1
         winnings=totalmoney+bet
         totalmoney=totalmoney+bet
         if totalmoney==0:
             print("game ended add more money to play ")
             add()
         print(f"you won :{bet}  money left:{winnings}   wins :{wins}     loses :{loses}")
    elif a+b < 7 and yourvalue=="below 7":

        print(f"you won you number was :{a+b}")
        wins+=1
        winnings=totalmoney+bet
        totalmoney=totalmoney+bet
        if totalmoney==0:
            
            print("game ended add more money to play ")
            add()
         
            
        print(f"you won :{bet}  money left:{winnings}    wins :{wins}      loses :{loses}")
    elif a+b==7 and yourvalue=="equal":

        print(f"you won you number was :{a+b}")
        wins+=1
        winnings=totalmoney+bet
        totalmoney=totalmoney+bet
        if totalmoney==0:
            add()
        print(f"you won :{bet}  money left:{winnings}   wins :{wins}      loses :{loses}")
    else:

        print(f"you lost you number was :{a+b}") 
        loses+=1
        totalloss=totalmoney-bet
        totalmoney=totalmoney-bet
        if totalmoney==0:
            print("game ended add more money to play ")   # how to end the gamne now
            add()
            
        print(f"you lost :{bet}  money left:{totalloss}   wins :{wins}     loses :{loses}")
  
  
                                                                                                                                                                                                                                                                                                                                                                                          
while True:
    while True:
        takeInput()
        betting()
        if bet <= 50:
            print("enter a vlaid bet ")
            break
        if bet ==0:
            print("enter a valid bet ")
            break
        if bet > totalmoney:
            print("you cant bet more than what you have ")
            break
        checkWin()
        break
        
    playAgain=input("do you want to play again : ")
    if playAgain=="yes":
        pass
    else:
        break
print("game ended")


  


    

    
       
            
        
        
            
    



    

        




    
    
  



     
        

  


    

    

        




    
    
  


