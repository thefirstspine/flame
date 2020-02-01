import fire
import json
import os


class ComputePlayers:
    def get_player(self, player_id, path='/storage/arena', export_json=False):
        """Get a player data"""
        with open(path + '/wizzards/' + str(player_id), 'r') as outfile:
            data = outfile.read()
            return data if export_json is True else json.loads(data)

    def ranks(self, path='/storage/arena', export_json=False):
        """Ranks the players according to their victories"""
        files = os.listdir(path + '/wizzards')
        ranks = []
        for name in files:
            player_data = self.get_player(name, path)
            points = self.__compute_points(player_data['history'])
            ranks.append({
                'player': {
                    'id': player_data['id'],
                    'name': player_data['name'],
                },
                'points': points,
            })
        output = sorted(ranks, key=lambda x: x['points'], reverse=True)
        return json.dumps(output) if export_json is True else output

    def get_points(self, player_id, path='/storage/arena', export_json=False):
        """Get the points of a player"""
        player_data = self.get_player(player_id, path)
        output = self.__compute_points(player_data['history'])
        return json.dumps(output) if export_json is True else output

    def __compute_points(self, history, export_json=False):
        """Compute the points from an history list"""
        points = 0
        for history_item in history:
            points += 3 if history_item['victory'] else -1
        return json.dumps(points) if export_json is True else points


if __name__ == '__main__':
    fire.Fire(ComputePlayers)
