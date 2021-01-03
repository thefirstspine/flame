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

    def count_day_sessions_per_product_and_version(self):
        """Get the sessions in the Solid Pancake service tracking"""
        cursor = self.__connection.cursor(cursor_factory=RealDictCursor)
        results = []
        cursor.execute(
            """SELECT session.* AS last_event_created_at
            FROM "event"
            INNER JOIN session ON (event.session_id = session.session_id)
            WHERE event.created_at > (NOW() - INTERVAL '1 DAY')
            GROUP BY session.session_id"""
        )
        for result in cursor.fetchall():
            results.append({
                "session_id": result['session_id'],
                "product": result['product'],
                "label": result['label'],
                "version": result['version'],
            })
        return self.output(results)

    def count_sessions_per_product_label_version(self):
        """Count the sessions per product"""
        cursor = self.__connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute("""SELECT product, version, label, COUNT(*) count
            FROM "session" GROUP BY ("product", "version", "label")
            ORDER BY ("product", "version", "label"); """)
        results = []
        for result in cursor.fetchall():
            results.append({
                "product": result['product'],
                "label": result['label'],
                "version": result['version'],
                "count": result['count'],
            })
        return self.output(results)

    def get_day_client_errors(self):
        """Get all the events with the category ClientError"""
        cursor = self.__connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute("""SELECT * FROM "event" 
            WHERE category = 'clientError' AND event.created_at > (NOW() - INTERVAL '1 DAY')""")
        results = []
        for result in cursor.fetchall():
            results.append({
                "event_id": result['event_id'],
                "session_id": result['session_id'],
                "category": result['category'],
                "event": result['event'],
                "action": result['action'],
                "label": result['label'],
                "created_at": result['created_at'],
            })
        return self.output(results)


if __name__ == '__main__':
    fire.Fire(ComputeSessions)
