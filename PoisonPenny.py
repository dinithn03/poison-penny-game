#Name: Dinith
#Purpose: Create the poisoned penny game mainly using the while loop, but also using many of the previous loops and functions learned
#Date: November 8th, 2018

#Printing the title and intro paragraph
print("Poison Penny")
print("------------\n")
print("Poison penny is a game for two players. Twelve pennies and a nickel are laid out.")
print("Each player can take one or two pennies, alternating turns until only the")
print("nickel (the poison) is left. Whoever's turn it is, when only the poisoned nickel is left, loses.")

again = "y"

#Creating the main while loop so that if the user want's to play again, it loops back to the start
while again == "y" or again == "Y":
#Pennies are set to 12 at the beggining of each game
    p = int(12)
#Prompts the two players to enter their names
    player1 = input("\nEnter player 1's name: ")
    player2 = input("Enter player 2's name: ")
#Continuosly asks the asks the user to take pennies until none remaain
    while p != 0:
#Creating the code that simataneously asks to take pennies between the two users
        if p != 0:
            print("\nThere are", p, "pennies and 1 nickel left.")
            print(str(player1) + ", ", end="")
            take = int(input("how many pennies do you wish to take? "))
        else:
            break
        while take != 1 or take != 2:
            if take == 1 or take == 2:
                break
            print(str(player1) + ", ", end="")
            take = int(input("how many pennies do you wish to take? "))
#Creating a while loop so that when there is one penny remaining, the user has to take the penny
        while p == 1:
            while take != p:
                print(str(player1) + ", ", end="")
                take = int(input("how many pennies do you wish to take? "))
            if take == p:
                print("\n" + player2 + ", you lose because you must take the nickel.")
                print("Congratulations", player1 + ", you are the winner.")
                p = p-take
#Setting a while loop so that if there is 2 pennies left, and the player chooses 1 penny, there will be 1 penny left and the other player must take 1 penny and win
        while p == 2:
            while take != 1 or take != 2:
                if take == 1 or take == 2:
                    break
                print(str(player1) + ", ", end="")
                take = int(input("how many pennies do you wish to take? "))
#If player 1 chooses 1 penny when there are 2 left, player 2 must take the last one and win
            if take == 1:
                p = p-take
                print("\nThere are", p, "pennies and 1 nickel left.")
                print(str(player2) + ", ", end="")
                take = int(input("how many pennies do you wish to take? "))
                while take != 1:
                    print(str(player2) + ", ", end="")
                    take = int(input("how many pennies do you wish to take? "))
                print("\n" + player1 + ", you lose because you must take the nickel.")
                print("Congratulations", player2 + ", you are the winner.")
#If player 1 chooses 2 pennies, when there are 2 left, they win
            elif take == 2:
                print("\n" + player2 + ", you lose because you must take the nickel.")
                print("Congratulations", player1 + ", you are the winner.")
                p = p-take
        if take == 1 and p > 0:
            p = p-1
        elif take == 2 and p > 0:
            p = p-2
            
        if p != 0:
            print("\nThere are", p, "pennies and 1 nickel left.")
            print(str(player2) + ", ", end="")
            take = int(input("how many pennies do you wish to take? "))
        else:
            break
        while take != 1 or take != 2:
            if take == 1 or take == 2:
                break
            print(str(player2) + ", ", end="")
            take = int(input("how many pennies do you wish to take? ")) \
#Creating a while loop so that when there is one penny remaining, the user has to take the penny
        while p == 1:
            while take != p:
                print(str(player2) + ", ", end="")
                take = int(input("how many pennies do you wish to take? "))
            if take == p:
                print("\n" + player1 + ", you lose because you must take the nickel.")
                print("Congratulations", player2 + ", you are the winner.")
                p = p-take
#Setting a while loop so that if there is 2 pennies left, and the player chooses 1 penny, there will be 1 penny left and the other player must take 1 penny and win
        while p == 2:
            while take != 1 or take != 2:
                if take == 1 or take == 2:
                    break
                print(str(player2) + ", ", end="")
                take = int(input("how many pennies do you wish to take? "))
#If player 2 chooses 1 penny when there are 2 left, player 1 must take the last one and win
            if take == 1:
                p = p-take
                print("\nThere are", p, "pennies and 1 nickel left.")
                print(str(player1) + ", ", end="")
                take = int(input("how many pennies do you wish to take? "))
                while take != 1:
                    print(str(player1) + ", ", end="")
                    take = int(input("how many pennies do you wish to take? "))
                print("\n" + player2 + ", you lose because you must take the nickel.")
                print("Congratulations", player1 + ", you are the winner.")
#If player 2 chooses 2 pennies, when there are 2 left, they win
            elif take == 2:
                print("\n" + player1 + ", you lose because you must take the nickel.")
                print("Congratulations", player2 + ", you are the winner.")
                p = p-take
        if take == 1 and p > 0:
            p = p-1
        elif take == 2 and p > 0:
            p = p-2
#Asking the user if they want to play again
    again = input("\nWould you like to play again? (Y/N): ")
    
print("\nThank you for playing. Come back soon.")


       
