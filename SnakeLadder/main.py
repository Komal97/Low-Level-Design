from service import GameService
from model import Player

def main():
    
    game_service = GameService()
    
    board_size = int(input('Please Enter board size: '))
    num_players = int(input('Please enter number of players: '))
    
    players_list = []
    for num in range(num_players):
        player_name = input(f'Please enter {num} player name: ')
        players_list.append(Player(player_name))
        
    game_service.initialize_board(board_size, players_list)
    game_service.play_game()

main()