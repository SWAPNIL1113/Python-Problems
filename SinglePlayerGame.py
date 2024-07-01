import random;

class SinglePlayerGame:
    def __init__(self, lower_bound=1, upper_bound=100):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.target = random.randint(self.lower_bound, self.upper_bound)
        self.guesses=0
    def heuristic(self, guess):
        return abs(self.target - guess)
    def play(self):
        print(f"Guess the number between {self.lower_bound} and {self.upper_bound}")
        while True:
            try:
                guess = int(input("Enter your guess: "))
                self.guesses +=1
                if guess < self.lower_bound or guess > self.upper_bound:
                    print(f"Please guess a number between{self.lower_bound} and {self.upper_bound}")
                    continue
                heuristic_value = self.heuristic(guess)
                if heuristic_value == 0:
                    print(f"Congratulations ! You've guessed the correct number {self.target} in {self.guesses} guesses")
                    break
                else :
                    print(f"Your guess is {'higher' if guess > self.target else 'lower'} than the target.")
                    print(f"Hint: You are {heuristic_value } units away from the target")
                    
            except ValueError :
                print(f"Invalid input. Please enter a valid number")                   
if __name__ == "__main__":
        game = SinglePlayerGame()
        game.play()