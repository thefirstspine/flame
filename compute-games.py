import fire
import json
import os
from base import FireCommand


class ComputeGames(FireCommand):
    def get_game(self, player_id, env='production', export_json=False):
        """"Get a player data"""
        with open(self.get_data_path(env) + '/games/' + str(player_id), 'r') as outfile:
            data = outfile.read()
            return data if export_json is True else json.loads(data)

    def count_game_types(self, env='production', export_json=False):
        """Get the number of played games by types"""
        files = os.listdir(self.get_data_path(env) + '/games')
        types = {}
        for name in files:
            game_data = self.get_game(name, env)
            game_type_id = game_data['gameTypeId']
            try:
                types[game_type_id] += 1
            except KeyError:
                types[game_type_id] = 1
        return json.dumps(types) if export_json is True else types

    def count_games_per_hour(self, env='production', export_json=False):
        """Get the games played per hour"""


if __name__ == '__main__':
    fire.Fire(ComputeGames)
