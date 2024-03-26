import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def roll_dice(self):
        return random.randint(1, 6)

    def play_round(self):
        print(f"{self.name}'s turn:")
        input("Press Enter to roll the dice...")
        dice1 = self.roll_dice()
        dice2 = self.roll_dice()
        total = dice1 + dice2
        print(f"{self.name} rolled: {dice1} and {dice2}")
        print(f"Total: {total}")
        self.score += total
        print(f"{self.name}'s total score: {self.score}\n")


def main():
    print("Welcome to the Dice Rolling Game!")
    num_players = int(input("Enter the number of players: "))

    players = []
    for i in range(num_players):
        name = input(f"Enter name for Player {i+1}: ")
        player = Player(name)
        players.append(player)

    num_rounds = int(input("Enter the number of rounds to play: "))

    for round_num in range(1, num_rounds + 1):
        print(f"\nRound {round_num} begins!\n")
        for player in players:
            player.play_round()

    print("\nGame Over!\n")
    print("Final Scores:")
    for player in players:
        print(f"{player.name}: {player.score}")

    # Find the winner
    winners = [player for player in players if player.score == max(p.score for p in players)]
    if len(winners) == 1:
        print(f"\n{winners[0].name} wins!")
    else:
        print("\nIt's a tie!")


if __name__ == "__main__":
    main()
