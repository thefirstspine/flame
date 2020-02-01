import fire
import json
import os
from datetime import datetime


class ComputeGames:
    def get_game(self, player_id, path='/storage/arena', export_json=False):
        """"Get a game instance data"""
        with open(path + '/games/' + str(player_id), 'r') as outfile:
            data = outfile.read()
            return data if export_json is True else json.loads(data)

    def count_game_types(self, path='/storage/arena', export_json=False):
        """Get the number of played games by types"""
        files = os.listdir(path + '/games')
        types = {}
        for name in files:
            game_data = self.get_game(name, path)
            game_type_id = game_data['gameTypeId']
            try:
                types[game_type_id] += 1
            except KeyError:
                types[game_type_id] = 1
        return json.dumps(types) if export_json is True else types

    def count_games_per_hour(self, path='/storage/arena', export_json=False):
        """Get the games played per hour"""
        files = os.listdir(path + '/games')
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
            game_data = self.get_game(name, path)
            try:
                first_action = game_data['actions']['previous'][0]
                dt_object = datetime.fromtimestamp(first_action['createdAt'] / 1000)
                hour = str(dt_object.hour)
                hours[hour] += 1
            except KeyError:
                pass
            except IndexError:
                pass
        return json.dumps(hours) if export_json is True else hours

    def count_games_per_weekday(self, path='/storage/arena', export_json=False):
        """Get the games played per hour"""
        files = os.listdir(path + '/games')
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
            game_data = self.get_game(name, path)
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
        return json.dumps(weekdays) if export_json is True else weekdays


if __name__ == '__main__':
    fire.Fire(ComputeGames)
