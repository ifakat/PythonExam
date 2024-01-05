
#######Second Question ################
####################################
# Trivia Game Option two
###################################



# Assumptions for Trivia 2:
# 1. Each player answers the same 5 randomly selected questions out of a pool of 10 questions.
# 2. The winner is determined after both players have answered their questions, and the results are displayed.
# 3. At the end, if a player enters the number of an option that is not available, they are warned, and the valid number of options is displayed to choose.
# 4. Additionally, after displaying the winner results, the answers given by each player and the correct answers are shown.

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


def get_valid_input():
    while True:
        try:
            player_answer = int(input("Enter the number of your answer (1-4): "))
            if 1 <= player_answer <= 4:
                return player_answer
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")


def main():
    # Create a list of 10 Question objects
    trivia_questions = [
        Question("What is the capital of France?", ["Paris", "Berlin", "Madrid", "Rome"], 1),
        Question("Which planet is known as the Red Planet?", ["Mars", "Venus", "Jupiter", "Saturn"], 1),
        Question("Who wrote 'Romeo and Juliet'?", ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"], 2),
        Question("What is the largest mammal?", ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"], 2),
        Question("Which programming language is known for its readability?", ["Java", "C++", "Python", "JavaScript"], 3),
        Question("In what year did the Titanic sink?", ["1905", "1912", "1920", "1931"], 2),
        Question("What is the currency of Japan?", ["Won", "Yuan", "Yen", "Ringgit"], 3),
        Question("Who painted the Mona Lisa?", ["Pablo Picasso", "Vincent van Gogh", "Leonardo da Vinci", "Claude Monet"], 3),
        Question("Which element has the chemical symbol 'O'?", ["Oxygen", "Gold", "Silver", "Iron"], 1),
        Question("What is the largest ocean on Earth?", ["Atlantic Ocean", "Indian Ocean", "Southern Ocean", "Pacific Ocean"], 4),
    ]

    # Initialize players' scores
    player1_score = 0
    player2_score = 0

    # Lists to store correct and incorrect answers for each player
    player1_correct_answers = []
    player1_incorrect_answers = []
    player2_correct_answers = []
    player2_incorrect_answers = []

    # Shuffle the questions to ensure each player gets a different set
    import random
    random.shuffle(trivia_questions)

    # Loop through each question for both players
    for player in range(2):
        print(f"Player {player + 1}'s turn:")
        for question in random.sample(trivia_questions, 5):
            question.display_question()
            player_answer = get_valid_input()

            # Check if the answer is correct and update the player's score
            if question.check_answer(player_answer):
                print("Correct!\n")
                if player == 0:
                    player1_score += 1
                    player1_correct_answers.append((question.question, question.options[question.correct_answer - 1]))
                else:
                    player2_score += 1
                    player2_correct_answers.append((question.question, question.options[question.correct_answer - 1]))
            else:
                print(f"Incorrect. The correct answer was: {question.options[question.correct_answer - 1]}\n")
                if player == 0:
                    player1_incorrect_answers.append((question.question, question.options[question.correct_answer - 1]))
                else:
                    player2_incorrect_answers.append((question.question, question.options[question.correct_answer - 1]))

    # Display the final scores and declare the winner
    print("\nPlayer 1's score:", player1_score)
    print("Player 2's score:", player2_score)

    if player1_score > player2_score:
        print("Player 1 is the winner!")
    elif player2_score > player1_score:
        print("Player 2 is the winner!")
    elif player1_score == player2_score and player1_score != 0:
        print("It's a tie!")
    else:
        print("No winner. Both players scored zero.")

    # Display the correct and incorrect answers for each player
    print("\nPlayer 1's Correct Answers:")
    for i, (question, correct_answer) in enumerate(player1_correct_answers, 1):
        print(f"{i}. {question} - Your Answer: {correct_answer}")

    print("\nPlayer 1's Incorrect Answers:")
    for i, (question, correct_answer) in enumerate(player1_incorrect_answers, 1):
        print(f"{i}. {question} - Correct Answer: {correct_answer}")

    print("\nPlayer 2's Correct Answers:")
    for i, (question, correct_answer) in enumerate(player2_correct_answers, 1):
        print(f"{i}. {question} - Your Answer: {correct_answer}")

    print("\nPlayer 2's Incorrect Answers:")
    for i, (question, correct_answer) in enumerate(player2_incorrect_answers, 1):
        print(f"{i}. {question} - Correct Answer: {correct_answer}")

if __name__ == "__main__":
    main()