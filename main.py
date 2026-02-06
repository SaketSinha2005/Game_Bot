from pingv4 import Connect4Game, MinimaxBot
from submissions.saket_ss691 import ss691

def main():
    bot = ss691   # IMPORTANT

    print("=" * 50)
    print(f"Testing Bot: {bot.strategy_name}")
    print(f"Author: {bot.author_name} {bot.author_netid}")
    print("=" * 50)

    input("Press Enter to start")
    game = Connect4Game(player1=MinimaxBot, player2=bot)
    game.run()

if __name__ == "__main__":
    main()
