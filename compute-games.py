import fire
import json
import os


class ComputeGames:
    def get_game(self, player_id, path='/storage/arena', export_json=False):
        """"Get a player data"""
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


if __name__ == '__main__':
    fire.Fire(ComputeGames)
