from tictactoe.board import Board

class Game:

    def __init__(self):
        self.board = Board()
        self.players = ["X", "O"]
        self.player_index = 0

    def get_input(self, player):
        while True:
            try:
                print(f"Player '{player}' - enter a square [1-9]:")
                raw_input = input()
                parsed_input = int(raw_input)
            except ValueError:
                print(f"The value {raw_input} is not a valid value.  Please try again")
                continue

            if parsed_input not in range(1, 10):
                print(f"The value {parsed_input} is not in the range 1-9.  Please try again")
                continue

            break

        return parsed_input

    def change_player(self):
        self.player_index = (self.player_index + 1) % 2

    @property
    def current_player(self):
        return self.players[self.player_index]

    def main(self):
        while not self.board.check_for_victory():
            self.board.draw_board()
            try:
                input = self.get_input(self.current_player)
                self.board.add_move(self.current_player, input)

            except AttributeError:
                print("Sorry that square is already taken - try again")
                continue

            self.change_player()

        winner = self.board.check_for_victory()
        print(f"Winner if {winner}!")

if __name__ == '__main__':
    g = Game()
    g.main()
