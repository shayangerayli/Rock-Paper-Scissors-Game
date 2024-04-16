import random

computerscore=0
clientscore=0
while True:
    
    Dicte={"k":"Kaghaz","g":"Gheychi","s":"Sang"}
    Parametr=["s","k","g"]
    computerInput=Parametr[random.randint(0,2)]
    ClientInput=input("Please Input Your Prameter (Sang)=s (Kaghaz)=k (Gheichi)=g ::::: ")
    if ClientInput in Parametr:
    
        print("Your Input Is ",Dicte[ClientInput])
        print("Computer Input Is ", Dicte[computerInput])
        if computerInput == ClientInput:
            print("Mosaavi Shode!!")
        elif ClientInput == "s":
            if computerInput == "k":
                computerscore=computerscore+1
                print("Computer Winer!!")
            elif computerInput=="g":
                clientscore=clientscore+1
                print("You Winer!!")
        elif ClientInput=="k":
            if computerInput=="s":
                clientscore=clientscore+1
                print("You Winer!!")
            elif computerInput=="g":
                computerscore=computerscore+1
                print("Computer Winer!!")
        elif ClientInput=="g":
            if computerInput=="s":
                computerscore=computerscore+1
                print("Computer Winer!!")
            elif computerInput=="k":
                clientscore=clientscore+1
                print("You Winer!!")
        print("....................")
        print("Computer Score Is ",computerscore)
        print("Client Score Is ",clientscore)
        print("....................")
        cont=input("You want countinue? (y/n) ")
        if cont=="y":
            pass
        else:
            break

    else:
        print("Erorr! Please input (s ,k ,g)")
        continue
    