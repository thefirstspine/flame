import fire
import json
import os
from basecommand import BaseCommand


class ComputePlayers(BaseCommand):

    def _get_player(self, player_id):
        """Get a player data"""
        with open('/flame-volume/data/wizzards/' + str(player_id), 'r') as outfile:
            data = outfile.read()
            return json.loads(data)

    def get_player(self, player_id):
        """Get a player data"""
        with open('/flame-volume/data/wizzards/' + str(player_id), 'r') as outfile:
            data = outfile.read()
            return self.output(data)

    def ranks(self):
        """Ranks the players according to their victories"""
        files = os.listdir('/flame-volume/data/wizzards')
        ranks = []
        for name in files:
            player_data = self.get_player(name)
            points = self.__compute_points(player_data['history'])
            ranks.append({
                'player': {
                    'id': player_data['id'],
                    'name': player_data['name'],
                },
                'points': points,
            })
        output = sorted(ranks, key=lambda x: x['points'], reverse=True)
        return self.output(output)

    def get_points(self, player_id):
        """Get the points of a player"""
        player_data = self.get_player(player_id)
        output = self.__compute_points(player_data['history'])
        return self.output(output)

    def __compute_points(self, history):
        """Compute the points from an history list"""
        points = 0
        for history_item in history:
            points += 3 if history_item['victory'] else -1
        return self.output(points)


if __name__ == '__main__':
    fire.Fire(ComputePlayers)
