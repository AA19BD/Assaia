from connect4 import Connect4Game
from connect4 import ChipColor


def main():
    game = Connect4Game()
    print(f"Starting Connect 4 game with two players: {ChipColor.YELLOW.name} and {ChipColor.RED.name}")
    game.display()

    while True:
        for player_color in [ChipColor.YELLOW, ChipColor.RED]:
            while True:
                column_choice = input(f'Player {player_color.name} - Select a column (0-6): ')
                if not column_choice.isdigit() or int(column_choice) < 0 or int(column_choice) >= game.NUM_COLUMNS:
                    print('Invalid input. Please choose a valid column.')
                    continue
                try:
                    game.drop_chip(int(column_choice), player_color)
                    if game.check_for_win():
                        print(f"Player {player_color.name} wins!")
                        exit()
                except ValueError:
                    print('Invalid move. The selected column is full.')
                    continue
                else:
                    break
            game.display()


if __name__ == '__main__':
    main()
