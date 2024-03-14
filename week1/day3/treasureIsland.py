print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
print("After a long and perilous jouney across the Atlantic to the new world")
print("you find yourself on a new island... what mysteries will unfold?")
print("On the island you fihd a mysterious ancient temple, you come to an intersection...")

first_turn = (input("Which way will you go? L or R"))

if first_turn == "R":
    print("You have fallen into a pit of radioactive worms GAME OVER")
else:
    print("The path on the left has taken you farther into the temple.")
    print("This path has many traps, but you manage to get past unharmed.")
    second_turn = (input("You have reached a flooded area, Swim or Wait? "))

    if second_turn == "Swim":
        print("The current is too strong, you wash away and drown... GAME OVER")
    else:
        print("You have waited for the flood waters to go down.\nYou are coming closer to the end where you see 3 doors.")
        print("The three doors are colored Blue, Yellow, and Red")
        third_turn = (input("Which door do you choose? Red, Yellow, or Blue? " ))

        if third_turn == "Yellow":
            print("You have found the treasure!")
        else:
            print("You have fallen into the void of an alternate dimension GAME OVER")