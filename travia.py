class Question:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

    def display_question(self):
        print(self.question)
        for i, option in enumerate(self.options, 1):
            print(f"{i}. {option}")
        print()

    def check_answer(self, player_answer):
        return player_answer == self.correct_answer


def main():
    # Create a list of 10 Question objects
    trivia_questions = [
        Question("What is the capital of France?", ["Paris", "Berlin", "London", "Rome"], 1),
        Question("Which planet is known as the Red Planet?", ["Mars", "Venus", "Jupiter", "Saturn"], 1),
        Question("Who wrote 'Romeo and Juliet'?",
                 ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"], 2),
        # Add more questions as needed
    ]

    # Initialize players' scores
    player1_score = 0
    player2_score = 0

    # Loop through each question for both players
    for player in range(2):
        print(f"Player {player + 1}'s turn:")
        for question in trivia_questions:
            question.display_question()
            player_answer = int(input("Enter the number of your answer (1-4): "))

            # Check if the answer is correct and update the player's score
            if question.check_answer(player_answer):
                print("Correct!\n")
                if player == 0:
                    player1_score += 1
                else:
                    player2_score += 1
            else:
                print("Incorrect. The correct answer was:", question.options[question.correct_answer - 1], "\n")

    # Display the final scores and declare the winner
    print("Player 1's score:", player1_score)
    print("Player 2's score:", player2_score)

    if player1_score > player2_score:
        print("Player 1 is the winner!")
    elif player2_score > player1_score:
        print("Player 2 is the winner!")
    else:
        print("It's a tie!")


if __name__ == "__main__":
    main()
