from dao import GameDao
from model import Board, Dice

class GameService:
    
    def __init__(self):
        self.__game_dao = GameDao()
        self.__board = 0
        self.__dice = Dice()
        
    def initialize_board(self, board_size, players_list):
        
        self.__game_dao.set_ladders()
        self.__game_dao.set_snakes()
        self.__board = Board(board_size)
        
        for player in players_list:
            self.__game_dao.add_player(player)
        
    def play_game(self):
        
        while True:
            
            dice_num = self.__dice.roll_dice()
            player = self.__game_dao.get_player()
            
            print(f'{player.get_name()} turn, dice number: {dice_num}')
            position = player.get_position()
            new_position = dice_num + position
            if new_position > self.__board.get_size():
                self.__game_dao.add_player(player)
                continue
            if new_position == self.__board.get_size():
                print(f'{player.get_name()} wins')
                player.set_is_won(True)
                break
            
            if self.__game_dao.get_snakes(new_position) != None:
                new_position = self.__game_dao.get_snakes(new_position)
                print(f'Snake bits, new position is {new_position}')
            elif self.__game_dao.get_ladders(new_position) != None:
                new_position = self.__game_dao.get_ladders(new_position)
                print(f'Ladder Climbed, new position is {new_position}')
            else:
                print(f'new position is {new_position}')
            
            player.set_position(new_position)
            self.__game_dao.add_player(player)
        
        