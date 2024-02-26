import requests
import random

def get_api_question():
    while True:
        try:
            response = requests.get("https://opentdb.com/api.php?amount=1&category=18&type=multiple")
            data = response.json()
            category = data["results"][0]["category"]
            difficulty = data["results"][0]["difficulty"]
            question = data["results"][0]["question"]
            correct_answer = data["results"][0]["correct_answer"]
            incorrect_answers = data["results"][0]["incorrect_answers"]
            return category, difficulty, question, correct_answer, incorrect_answers
        except Exception:
            pass

def play_game():
    while True:
        category, difficulty, question, correct_answer, incorrect_answers = get_api_question()
        answers = [correct_answer] + incorrect_answers
        random.shuffle(answers)

        print("Difficulty:", difficulty.capitalize())
        print("Question:", question)
        for index, answer in enumerate(answers):
            print(f"{index + 1}. {answer}")

        while True:
            user_answer = input("\nYour answer (Enter the corresponding number or 'quit' to end the game): ").lower()

            if user_answer == "quit":
                return

            if user_answer.isdigit() and 1 <= int(user_answer) <= len(answers):
                if answers[int(user_answer) - 1] == correct_answer:
                    print(f"Correct! Answer: {correct_answer}\n")
                else:
                    print("Incorrect.The correct answer is:", correct_answer, "\n")
                break
            else:
                print("Invalid response. Please choose one of the options presented.\n")

    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
