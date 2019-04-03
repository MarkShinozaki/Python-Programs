#Abstraction 
def main():
    password()
    introduction()
    rules()
    body()
    playagain()
    
    
#password
def password():
    Username = input("\nEnter any Username: ")
    Password = input("Enter any Password: ")
    print("Your password has been Saved")
    print("------------------------------")
    print("\nHi there,", Username )
    print("\n------------------------------")
    
#intoduction
def introduction():
    print("\nWelcome to the wealth & life game.")
    print("------------------------------")

    print("\nThis Game tests your ability to escape poverty in 10 days.")
    print("\n------------------------------------------")
    print("Instructions:")
    print("\nChoose the best methods to making 10,000 dollars or more")
    print("If you do not succeed than you will DIE \n \nIf you make the right financial decisions you will win!")
    print("\n------------------------------------------")

#Rules
def rules():
    Rules = str(input("\nwould you like to see some Rules, Advice and Facts?: "))
    if Rules== "yes" or Rules =="ok" or Rules =="yea" or Rules =="y":
        print("\n 1. Total time is 10 days & you Start w/ $40 \n \n 2. sleep will increase health +1\n \n 3. Each day you pick that is not sleep results in -1 to health \n \n 4. If health becomes 0 you lose \n \n 5. Checking the inventory will not make any changes \n \n 6. investing money takes up twice the amount of health \n")
        print("------------------------------------------")
        print("\nAdvice")
        print("------")
        print("- Saving money & educating yourself is a great way to make more money")
        print("\nFacts")
        print("------")
        print("- You start with $40")
        print("- Asking for money will + $20")
        print("- sleeping will +1 to health")
        print("- Reading a book with + $20")
        print("- saving money will + $200")
        print("- Investing money will multiple $ by 4")
        print("- Investing money will -2 to health")
    else:
        print("\nChoose your next step on the path to riches")

#body code loop
def body():
    import random
    done = False
    money = 30
    health = 5
    days = 10
    read_books = 0
    inventory_check = 0
    print("\n------------------------------------------")
    print("*choose letter A,B,C,D,E,F to start*")
    while not done:
        print("\nA. Ask for money.","\nB. read a book.","\nC. Sleep.","\nD. Save money.","\nE. Invest money","\nF. Inventory check","\nQ. Quit.")
        choice = input("Your choice? ")
        if choice == "q" or choice == "Q":
            done = True
            
#The list of choices
    # Ask for money
        elif choice == "a" or choice == "A":
            print("You got $20 dollars!")
            money = money+20
            days = days - 1
            health = health - 1
            print("\nYou now have %d dollars" %(money,))
            print("your health is: %d" %(health,))
            print("you have %d days left " %(days,))
            print("\n------------------------------------------")
            
    #Read a book
        elif choice == "b" or choice == "B":
            money = money+20
            health = health - 1
            days = days - 1
            print("\nYou have made $20, Smarts will help you make money")
            print("You now have %d dollars" %(money,))
            print("your health is: %d" %(health,))
            print("you have %d days left " %(days,))
            print("\n------------------------------------------")
            
    #sleep
        elif choice == "c" or choice == "C":
            health = health + 1
            days = days - 1
            print("you have %d dollars" %(money,))
            print("your health is: %d" %(health,))
            print("you have %d days left " %(days,))
            print("\n------------------------------------------")
            
    #Save money
        elif choice == "d" or choice == "D":
            money = money+200
            days = days - 1
            health = health - 1
            print ("\nYou have saved your money & made $200")
            print("\nyou have %d dollars" %(money,))
            print("your health is: %d" %(health,))
            print("you have %d days left " %(days,))
            print("\n------------------------------------------")
            
    #Invest money
        elif choice == "e" or choice == "E":
            money=money*4
            days = days - 1
            health = health - 2
            print ("\nYou have invested your money and now have $%d" %(money,))
            print("\nyour health is: %d" %(health,))
            print("you have %d days left " %(days,))
            print("\n*investing produces more money, requrining -2 health*")
            print("\n------------------------------------------")
            
    #Inventory Check
        elif choice == "f" or choice == "F":
            print("\nInventory Check:")
            print("----------------")
            print("\n Money: %d\n Health: %d\n Days left: %d" %(money, health, days,))
            print("\n------------------------------------------")
            
        #Check statements
        #health warning 
        if health < 1 :
            print("*If your health hits zero you will die*")
            print("---------------------------------------")
        #end due to health
        if health <= 0 :
            print ("\nGame Over!! You let your health get too horrible to survive")
            done = True
        #end due to time!
        if days <= 0:
            print ("\nGame Over you ran out of time")
            done = True
    #won game
        if money >= 10000 and days >= 0 and health >= 1:
            print ("EXCELLENT JOB, YOU HAVE WON THE GAME!!!")
            done = True

#request to run again
def playagain():
    print("\n-----------------------------------------")
    while True:
        again = input("\nwould you like to play again?:")
        if again=="yes" or again=="Yes"  or again=="yea" or again=="ok" or again=="y":
            main()
        elif again=="no" or again=="No" or again=="nah" or again=="n":
             break
#Call to operate 
main()



       
    
    
