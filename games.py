import fire
import json
import os
from datetime import datetime
from basecommand import BaseCommand


class ComputeGames(BaseCommand):

    def __get_game(self, game_id):
        """"Get a game instance data"""
        with open('/flame-volume/data/games/' + str(game_id), 'r') as outfile:
            data = outfile.read()
            return json.loads(data)

    def get_game(self, game_id):
        """"Get a game instance data"""
        return self.output(self.__get_game(game_id))

    def count_game_types(self):
        """Get the number of played games by types"""
        files = os.listdir('/flame-volume/data/games/')
        types = {}
        for name in files:
            game_data = self.__get_game(name)
            game_type_id = game_data['gameTypeId']
            try:
                types[game_type_id] += 1
            except KeyError:
                types[game_type_id] = 1
        return self.output(types)

    def count_games_per_hour(self):
        """Get the games played per hour"""
        files = os.listdir('/flame-volume/data/games/')
        hours = {
            '0': 0,
            '1': 0,
            '2': 0,
            '3': 0,
            '4': 0,
            '5': 0,
            '6': 0,
            '7': 0,
            '8': 0,
            '9': 0,
            '10': 0,
            '11': 0,
            '12': 0,
            '13': 0,
            '14': 0,
            '15': 0,
            '16': 0,
            '17': 0,
            '18': 0,
            '19': 0,
            '20': 0,
            '21': 0,
            '22': 0,
            '23': 0,
        }
        for name in files:
            game_data = self.__get_game(name)
            try:
                first_action = game_data['actions']['previous'][0]
                dt_object = datetime.fromtimestamp(first_action['createdAt'] / 1000)
                hour = str(dt_object.hour)
                hours[hour] += 1
            except KeyError:
                pass
            except IndexError:
                pass
        return self.output(hours)

    def count_games_per_weekday(self):
        """Get the games played per weekday"""
        files = os.listdir('/flame-volume/data/games/')
        weekdays = {
            'mo': 0,
            'tu': 0,
            'we': 0,
            'th': 0,
            'fr': 0,
            'sa': 0,
            'su': 0,
        }
        weekdays_map = {
            '0': 'mo',
            '1': 'tu',
            '2': 'we',
            '3': 'th',
            '4': 'fr',
            '5': 'sa',
            '6': 'su',
        }
        for name in files:
            game_data = self.__get_game(name)
            try:
                first_action = game_data['actions']['previous'][0]
                dt_object = datetime.fromtimestamp(first_action['createdAt'] / 1000)
                weekday_index = str(dt_object.weekday())
                weekday = weekdays_map[weekday_index]
                weekdays[weekday] += 1
            except KeyError:
                pass
            except IndexError:
                pass
        return self.output(weekdays)

    def count_destroyed_cards_per_type(self):
        """Get the destroyed cards per type"""
        files = os.listdir('/flame-volume/data/games/')
        types = {
            'creature': 0,
            'spell': 0,
            'artifact': 0,
            'player': 0,
            'square': 0,
        }
        for name in files:
            game_data = self.__get_game(name)
            for card in game_data['cards']:
                try:
                    if card['currentStats']['life'] <= 0:
                        type = card['card']['type']
                        types[type] += 1
                except KeyError:
                    pass
                except IndexError:
                    pass
        return self.output(types)


if __name__ == '__main__':
    fire.Fire(ComputeGames)
