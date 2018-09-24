def room_two():
    print(""""
     
                  
      ----
     ( - -)
     ( < >)
     /    \
"""
            )






def room_three():
    print(
            """
                 /    ---------
                /
---------------/
"""
           )

def room_four():
     print(
        """
        
         | ----------|
         | |       | |
         | |       | |
          \ \      / /

          """
        )
       

def room_five():
     print(
        """

-----------------|
|    \      /    |
| <--0--> <-0--> |
|                | 
|    /      \    |
|----------------

"""
        )
     print("You made it; the MCP sits before you, though unaware of your presence.")



   
    

move_one = ""
move_two = ""
move_three = ""
move_four = ""
move_five = ""


print(
    """



-------------   |----------       -----------  |\       |
      |         |         |       |         |  | \      |
      |         |         |       |         |  |  \     |
      |         |----------       |         |  |   \    |
      |         |      \          |         |  |    \   |
      |         |       \         |         |  |     \  |  
      |         |        \        |         |  |      \ |
                                  -----------  |       \|



"""
    )

print("\nWelcome to the unauthorized Tron video game.")
print("\nThe object is simple: You must navigate through five rooms" +
      "\nto reach the MCP and destroy it. Each room will have two possible" +
      "\nmoves. Choose wisely, as one wrong move will result in game over.")

input("\nPress Enter to begin.")





Room_one = print(
                """
------------          -----
|          |          |   |      
|  000     |          |   |        
|   1      |          |   |       
|   1      |          |   |
|   1      |          |   | 
|          |          |   |
|-----------          |----

"""
   )


move_one = input("\nChoose which portal to enter Type either left or right.")
if move_one == "left":
    print("\nYou have entered the Room of Binary. Without proper armor," +
          "you have been reduced to 1's and 0's")
    input("Press enter to exit.")

elif move_one == "right":
    room_two()
    move_two = input("\nWill you board his ship and join him in his quest? Yes or No")

            
if move_two == "no":
    print("\nBecause you refused, you're trapped in your own game forever.")
    input("Press enter to exit.")
    
elif move_two == "yes":
    room_three()
    print("\nYou've entered the network, however the ship cannot continue." +
      "\nWhat do you want to do?")
    move_three = input("\nYou can redirect the beam or try crossing the" +
               "\ngap. What's your choice?")
if move_three == "cross":
    print("\nUnfortunately, it was too wide and the ship falls to oblivion.")
    input("Press enter to exit.")
elif move_three == "redirect":
    room_four()
    print("\nDestroy the Recognizer by throwing your disc.")
    move_four = input("\nType direct for a direct hit, or wall for a ricochet.")


if move_four == "direct":
    print("\nYour disc was disintegrated upon direct contact with the Recognizer's armor; it retaliates by blasting you into oblivion.")
    input("Press enter to exit.")

elif move_four == "wall":
    print("Your disc hit the Recognizer's head, vaporizing it.")
    room_five()
    move_five = input("Would you like to attack the MCP directly, or distract it?")


if move_five == "attack":
    print("\nThe Master Control Program saw you coming and erased you.")
    input("Tron was killed shortly after. The programs will have to wait for a new champion.")
elif move_five == "distract":
     print("\nYou distract the Master Control Program allowing Tron to" +
          "execute a sneak attack. Congratulations! Because of you and Tron, the programs are now free.")
     input("Press enter to return to the ENCOM and retrieve the printout with incriminating information against Dillinger.")

    
