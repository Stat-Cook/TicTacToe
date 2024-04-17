from tictactoe import Game


if __name__ == '__main__':
    g = Game()
    while True:
        g.main()
        _input = input("Enter y/Y to play again:")

        if _input.lower() == "y":
            continue
        break

