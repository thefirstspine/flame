import fire
import os
import psycopg2
from psycopg2.extras import RealDictCursor
from basecommand import BaseCommand


class ComputeSessions(BaseCommand):

    __connection = None

    def __init__(self, outputs_to="python"):
        super().__init__(outputs_to=outputs_to)
        self.__connection = psycopg2.connect(os.environ['FLAME_DB_URL'])

    def count_active_sessions_per_product_and_version(self):
        """Get the sessions in the Solid Pancake service tracking"""
        cursor = self.__connection.cursor(cursor_factory=RealDictCursor)
        sessions = {}
        cursor.execute(
            """SELECT session.* AS last_event_created_at
            FROM "event"
            INNER JOIN session ON (event.session_id = session.session_id)
            WHERE event.created_at > (NOW() - INTERVAL '15 MINUTES')
            GROUP BY session.session_id"""
        )
        for result in cursor.fetchall():
            key = """%s-%s-%s""" % (result['product'], result['version'], result['label'])
            try:
                sessions[key] += 1
            except KeyError:
                sessions[key] = 1
            try:
                sessions['product-' + result['product']] += 1
            except KeyError:
                sessions['product-' + result['product']] = 1
            try:
                sessions['version-' + result['version']] += 1
            except KeyError:
                sessions['version-' + result['version']] = 1
            try:
                sessions['label-' + result['label']] += 1
            except KeyError:
                sessions['label-' + result['label']] = 1
        return self.output(sessions)

    def count_sessions_per_product(self):
        """Count the sessions per product"""
        cursor = self.__connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute("""SELECT product, COUNT(product) FROM "session" GROUP BY "product" """)
        products = {}
        for result in cursor.fetchall():
            products[result['product']] = result['count']
        return self.output(products)


if __name__ == '__main__':
    fire.Fire(ComputeSessions)
