class InvalidOptionError(Exception):
    pass
class Quiz:
    def __init__(self):
        self.questions = [
            "1. Largest planet?\nA. Earth\nB. Mars\nC. Jupiter",
            "2. 5 + 3 = ?\nA. 6\nB. 8\nC. 10",
            "3. Capital of India?\nA. Delhi\nB. Mumbai\nC. Chennai",
            "4. Sun is a?\nA. Planet\nB. Star\nC. Satellite",
            "5. 10 / 2 = ?\nA. 2\nB. 5\nC. 10",
            "6. Water formula?\nA. CO2\nB. H2O\nC. O2",
            "7. Opposite of hot?\nA. Cold\nB. Warm\nC. Cool",
            "8. 3 * 3 = ?\nA. 6\nB. 9\nC. 12"]

        self.answers = ['C', 'B', 'A', 'B', 'B', 'B', 'A', 'B']
        self.score = 0

    def start_quiz(self):
        for i in range(len(self.questions)):
            while True:
                try:
                    print("\n" + self.questions[i])
                    user_ans = input("Enter option (A/B/C): ").upper()

                    if user_ans not in ['A', 'B', 'C']:
                        raise InvalidOptionError
                    if user_ans == self.answers[i]:
                        print("Correct")
                        self.score += 1
                    else:
                        print("Wrong ")
                    break
                except InvalidOptionError:
                    print("Invalid option selected! Try again.")

    def display_score(self):
        print("\nFinal Score:", self.score, "/", len(self.questions))

q = Quiz()
q.start_quiz()
q.display_score()
