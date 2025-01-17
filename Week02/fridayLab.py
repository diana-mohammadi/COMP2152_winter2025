import random

#Define the choices in the array
choices = ["Rock", "Paper", "Scissors"]

def main():
    try:
        user_input= input("Enter your choice (Rock, Paper, Scissors): ").capitalize()

        #validate the user input
        if user_input not in choices:
            raise ValueError("Invalid choice, please enter Rock, Paper, Scissors")

        #convert the user input to an index
        player_choice = choices.index(user_input)
        computer_choice = random.randint(0,2)
        print(f"Player choice: {choices[player_choice]}")
        print(f"Computer choice: {choices[computer_choice]}")

        #Determine the winner
        if computer_choice == player_choice:
            print("It is a tie!")
        elif (player_choice==0 and computer_choice==2) or \
            (player_choice==1 and computer_choice==0) or \
            (player_choice==2 and computer_choice==1):
            print("Player wins!")
        else:
            print("Computer wins!")
    except ValueError as e:
        print(f"Error: {e}")


#run the game through the main function
if __name__ == "__main__":
    main()