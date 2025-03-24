import random
import time

result_matrix = [
    [0, 1, -1], 
    [-1, 0, 1], 
    [1, -1, 0]  
]

map_choices = {"snake": 0, "water": 1, "gun": 2}
choices = list(map_choices.keys())

print("\n🎮 Welcome to the Snake-Water-Gun Game! 🎮")
print("First to 3 points wins the game!\n")

while True: 
    user_score = 0
    computer_score = 0
    rounds = 1

    while user_score < 3 and computer_score < 3:
        print(f"\n🔹 Round {rounds} 🔹")
        select_option = input("Enter your choice (Snake/Water/Gun): ").lower()

        if select_option not in choices:
            print("❌ Invalid choice! Please enter 'snake', 'water', or 'gun'.")
            continue

        computer_choice = random.choice(choices)
        user_index = map_choices[select_option]
        computer_index = map_choices[computer_choice]

        print("\nRock... Paper... Scissors... SHOOT! 🥁")
        time.sleep(1.5)

        result = result_matrix[user_index][computer_index]

        print(f"\n🧑 You chose: {select_option.capitalize()}")
        print(f"🤖 Computer chose: {computer_choice.capitalize()}")

        if result == 1:
            user_score += 1
            print("🎉 You Win this round! ✅")
        elif result == -1:
            computer_score += 1
            print("😢 You Lose this round! ❌")
        else:
            print("🤝 It's a Draw!")

        print(f"\n📊 Score: You {user_score} - {computer_score} Computer\n")
        rounds += 1


    if user_score == 3:
        print("\n🎊 Congratulations! You won the game! 🏆")
    else:
        print("\n🤖 Computer wins! Better luck next time!")

    
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\nThanks for playing! 🎮 See you next time!")
        break