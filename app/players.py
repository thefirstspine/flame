import fire
import os
from pymongo import MongoClient
from basecommand import BaseCommand


class ComputePlayers(BaseCommand):

    def ranks(self):
        """Get the number of played games by types"""
        client = MongoClient(os.environ['FLAME_DB_URL'])
        db = client.get_database('arena')
        documents = db.wizards.find({})
        entities = list(documents)
        ranks = []
        for entity in entities:
            points = self.__compute_points(entity['history'])
            ranks.append({
                'player': {
                    'id': entity['id'],
                    'name': entity['name'],
                },
                'points': points,
            })
        output = sorted(ranks, key=lambda x: x['points'], reverse=True)
        return self.output(output)

    def __compute_points(self, history):
        """Compute the points from an history list"""
        points = 0
        for history_item in history:
            points += 3 if history_item['victory'] else -1
        return self.output(points)


if __name__ == '__main__':
    fire.Fire(ComputePlayers)
