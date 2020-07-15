# Ian Maze
# COP2002.0M1/0M2
# March, 13, 2020
# Even and Odd
# This program uses input from the user to calculate the sum of all the even or
# odd numbers between 1 and the user defined integer

# Main Program Loop
choice = "y"
while choice.lower() == "y":

# Start Dialog!
    print("---------------------------------------------------------------------")
    print()
    print("Even/Odd Program!")
    print()

    print("This Program will find the sum from 1 and the user defined interger,")
    print("If the integer is even it will calcualte the sum of all the even #'s")
    print("up to the user defined number, it will do the same for odd numbers!")
    print()
    print()

# Get User Input!
    user_Number = int(input("Please enter a whole number between 1 and 50! : "))

# Validate User Input!
    if user_Number >= 1 and user_Number <= 50:

#Calculate Data To Produce Sum!
        even_total = 0
        odd_total = 0
        even_Or_odd = "true"
 
        for number in range(1, user_Number + 1):
            if(number % 2 == 0):
                even_total = even_total + number
                even_Or_odd = "true"
                
            else:
                odd_total = odd_total + number
                even_Or_odd = "false"

# Display Calculated Data!
        if even_Or_odd == "true":
            print()
            print("Its an even number!!")
            print("The even sum of 1 and ", user_Number, " is ", even_total)
            print()
            choice = input("Run Program Again? (y/n): ")
        else:
            print()
            print("Its an odd number!!")
            print("The odd sum of 1 and ", user_Number, " is ", odd_total)
            print()
            choice = input("Run Program Again? (y/n): ")

# If User Entered Wrong Input!    
    else:
        print("Hey! Not cool! I need a whole number between 1 and 50! Try again.")
        print()
        choice = input("Run Program Again? (y/n): ")

# Close Main Program Loop!
    print()

print("See Ya Later! :)")



