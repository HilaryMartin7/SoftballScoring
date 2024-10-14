import pandas as pd

class SoftballScorekeeper:
    def __init__(self):
        self.home_score = 0
        self.away_score = 0
        self.inning = 1
        self.half_inning = "Top"
        self.outs = 0
        self.bases = [0, 0, 0]  # 0 for empty, 1 for occupied

    def display_scoreboard(self):
        print("-" * 20)
        print("Inning:", self.inning, self.half_inning)
        print("Outs:", self.outs)
        print("Bases:", self.bases)
        print("Home:", self.home_score, "Away:", self.away_score)
        print("-" * 20)

    def update_score(self, runs):
        if self.half_inning == "Top":
            self.away_score += runs
        else:
            self.home_score += runs

    def advance_runners(self, bases):
        for base in bases:
            if base == 1:
                self.bases = [0] + self.bases[:2]
            elif base == 2:
                self.bases = [0, 0] + self.bases[:1]
            elif base == 3:
                self.bases = [0, 0, 0]
                self.update_score(1)

    def handle_play(self, play):
        if play == "single":
            self.advance_runners([1, 2, 3])
            self.bases[0] = 1
        elif play == "double":
            self.advance_runners([1, 2, 3])
            self.bases[1] = 1
        elif play == "triple":
            self.advance_runners([1, 2, 3])
            self.bases[2] = 1
        elif play == "homerun":
            self.advance_runners([1, 2, 3])
            self.update_score(1)
        elif play == "out":
            self.outs += 1
            if self.outs == 3:
                self.change_inning()

    def change_inning(self):
        if self.half_inning == "Top":
            self.half_inning = "Bottom"
        else:
            self.inning += 1
            self.half_inning = "Top"
        self.outs = 0
        self.bases = [0, 0, 0]

if __name__ == "__main__":
    game = SoftballScorekeeper()
    while True:
        game.display_scoreboard()
        play = input("Enter play (e.g., single, double, out): ")
        game.handle_play(play)