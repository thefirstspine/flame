import fire
import json
import os


class ComputePlayers(object):
    """Command to compute on players data."""

    DATA_PATH = './data'

    def get(self, player_id):
        """"Get a player data"""
        with open(self.DATA_PATH + '/wizzards/' + str(player_id), 'r') as outfile:
            data = outfile.read()
            return json.loads(data)

    def ranks(self):
        """Ranks the players according to their victories"""
        files = os.listdir(self.DATA_PATH + '/wizzards')
        ranks = []
        for name in files:
            player_data = self.get(name)
            points = self.__compute_points(player_data['history'])
            ranks.append({
                'player': player_data,
                'points': points,
            })
        return sorted(ranks, key=lambda x: x['points'], reverse=True)

    def points(self, player_id):
        """Get the points of a player"""
        player_data = self.get(player_id)
        return self.__compute_points(player_data['history'])

    def __compute_points(self, history):
        """Compute the points from an history list"""
        points = 0
        for history_item in history:
            points += 3 if history_item['victory'] else -1
        return points


if __name__ == '__main__':
    fire.Fire(ComputePlayers)
