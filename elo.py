import random
import pickle

with open("mentees.txt", "r") as f:
    mentees = f.read().splitlines()
    mentees = [mentee for mentee in mentees if mentee != ""]


class Score:
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.opponent_sum = 0

    def score(self):
        if self.wins + self.losses + self.draws == 0:
            return 1000

        return (self.opponent_sum + 400 * (self.wins - self.losses)) / (
            self.wins + self.losses + self.draws
        )

    def win(self, opponent_score):
        self.wins += 1
        self.opponent_sum += opponent_score

    def lose(self, opponent_score):
        self.losses += 1
        self.opponent_sum += opponent_score

    def draw(self, opponent_score):
        self.draws += 1
        self.opponent_sum += opponent_score


scores = {}
try:
    scores = pickle.load(open("scores.pickle", "rb"))
except FileNotFoundError:
    for mentee in mentees:
        scores[mentee] = Score()


counter = 0
while True:
    counter += 1
    try:
        # pick two random mentees
        menteeA = random.choice(mentees)
        menteeB = random.choice(mentees)
        if menteeA == menteeB:
            continue

        # print the match
        print(f"Match {counter}")
        print(f"A: {menteeA}")
        print(f"B: {menteeB}")

        # get the result
        result = input("Result (A/B/D): ").lower()
        print("")

        # update the scores
        scoreA, scoreB = scores[menteeA].score(), scores[menteeB].score()
        if result == "a":
            scores[menteeA].win(scoreB)
            scores[menteeB].lose(scoreA)
        elif result == "b":
            scores[menteeA].lose(scoreB)
            scores[menteeB].win(scoreA)
        elif result == "d":
            scores[menteeA].draw(scoreB)
            scores[menteeB].draw(scoreA)
        else:
            print("Invalid result")
            continue

    except KeyboardInterrupt:
        # print rankings
        print("\n\n=============\nRankings\n=============")
        for mentee in sorted(
            mentees, key=lambda x: scores[x].score(), reverse=True
        ):
            print(f"{scores[mentee].score():.2f} {mentee}\n")

        # save the scores
        pickle.dump(scores, open("scores.pickle", "wb"))
        print("")
        break
