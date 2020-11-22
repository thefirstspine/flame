import fire
import os
from pymongo import MongoClient
from basecommand import BaseCommand


class ComputeGames(BaseCommand):

    def count_game_types(self):
        """Get the number of played games by types"""
        client = MongoClient(os.environ['FLAME_DB_URL'])
        db = client.get_database('arena')
        aggregated = db.gameinstances.aggregate(
            [
                {
                    '$group': {
                        '_id': "$gameTypeId",
                        'count': {'$sum': 1}
                    }
                },
                {
                    '$sort': {
                        '_id': 1
                    }
                }
            ]
        )
        return self.output(list(aggregated))


if __name__ == '__main__':
    fire.Fire(ComputeGames)
