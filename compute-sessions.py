import fire
import json
import psycopg2
from psycopg2.extras import RealDictCursor
from configparser import ConfigParser


class ComputeSessions:

    __connection = None

    def __init__(self):
        config = self.__config()
        configstr = "host=%s dbname=%s user=%s password=%s port=%s" %\
                    (config['host'], config['database'], config['user'], config['password'], config['port'])
        self.__connection = psycopg2.connect(configstr)

    def __config(self, filename='database.ini', section='postgresql'):
        # create a parser
        parser = ConfigParser()
        # read config file
        parser.read(filename)
        # get section, default to postgresql
        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, filename))
        return db

    def get_sessions(self, offset=0, limit=10, export_json=False):
        """Get the sessions in the Solid Pancake service tracking"""
        cursor = self.__connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute(
            """SELECT * FROM "session" ORDER BY created_at DESC LIMIT %s OFFSET %s""",
            (limit, offset))
        sessions = []
        for result in cursor.fetchmany(limit):
            sessions.append({
                'session_id': result['session_id'],
                'product': result['product'],
                'label': result['label'],
                'version': result['version'],
                'created_at': result['created_at'].strftime('%Y-%m-%d %H:%M:%S'),
            })
        return json.dumps(sessions) if export_json is True else sessions

    def get_events(self, offset=0, limit=10, export_json=False):
        """Get the last events in the Solid Pancake service tracking"""
        cursor = self.__connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute(
            """SELECT event.*, session.product, session.version FROM "event" JOIN "session" ON session.session_id = 
            event.session_id ORDER BY created_at DESC LIMIT %s OFFSET %s""",
            (limit, offset))
        events = []
        for result in cursor.fetchmany(limit):
            events.append({
                'event': result['event'],
                'category': result['category'],
                'action': result['action'],
                'label': result['label'],
                'product': result['product'],
                'version': result['version'],
                'created_at': result['created_at'].strftime('%Y-%m-%d %H:%M:%S'),
            })
        return json.dumps(events) if export_json is True else events

    def count_active_sessions_per_product_and_version(self, export_json=False):
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
        return json.dumps(sessions) if export_json is True else sessions

    def get_sessions_with_events(self, export_json=False):
        """Get the sessions with events in the Solid Pancake service tracking"""
        cursor = self.__connection.cursor(cursor_factory=RealDictCursor)
        sessions = self.get_sessions(offset=0, limit=10, export_json=False)
        for session in sessions:
            events = []
            cursor.execute(
                """SELECT * FROM "event" WHERE session_id = '%s' ORDER BY created_at ASC""" % session['session_id'])
            for event in cursor.fetchall():
                events.append({
                    'event': event['event'],
                    'category': event['category'],
                    'action': event['action'],
                    'label': event['label'],
                    'created_at': event['created_at'].strftime('%Y-%m-%d %H:%M:%S'),
                })
            session['events'] = events
        return json.dumps(sessions) if export_json is True else sessions

    def count_sessions_per_product(self, export_json=False):
        """Count the sessions per product"""
        cursor = self.__connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute("""SELECT product, COUNT(product) FROM "session" GROUP BY "product" """)
        products = {}
        for result in cursor.fetchall():
            products[result['product']] = result['count']
        return json.dumps(products) if export_json is True else products


if __name__ == '__main__':
    fire.Fire(ComputeSessions)

