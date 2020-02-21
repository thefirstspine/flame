import datetime
import fire
import json
import os
import requests
import time


class ComputeSessions:
    __db_name = "flame"
    __python_executable = "python3"

    def setup(self):
        """Influx setup. Creates the required influx database."""
        self.__query("CREATE DATABASE %s" % self.__db_name)

    def push(self, command, path=None):
        """Pushes stats from Flame command call."""
        # Create the command
        command_file = command.split(':')[0]
        command_arg1 = command.split(':')[1]
        command_exec = "%s compute-%s.py %s %s --export_json=True" % (
            self.__python_executable,
            command_file,
            command_arg1,
            "--path=" + path if path is not None else "")
        # Launch the command & get the result
        result = os.popen(command_exec).read()
        obj = json.loads(result)

        # Construct the measurements
        series = "%s-%s" % (command_file, command_arg1)
        category = command_file
        measurements = []
        for key, value in obj.items():
            measurements.append("%s=%s" % (key, self.__measurement(value)))

        # Write to influxdb
        self.__write("%s,Category=%s,From=Flame %s" % (series, category, ",".join(measurements)))

    def push_list(self, command, timestamp_field="created_at", path=None):
        """Pushes stats from Flame command call that produces a list."""
        # Create the command
        command_file = command.split(':')[0]
        command_arg1 = command.split(':')[1]
        command_exec = "%s compute-%s.py %s %s --export_json=True" % (
            self.__python_executable,
            command_file,
            command_arg1,
            "--path=" + path if path is not None else "")
        # Launch the command & get the result
        result = os.popen(command_exec).read()
        list = json.loads(result)
        influx_query = ""

        for obj in list:
            # Construct the measurements
            series = "%s-%s" % (command_file, command_arg1)
            category = command_file
            timestamp = time.mktime(datetime.datetime.strptime(obj[timestamp_field], "%Y-%m-%d %H:%M:%S").timetuple())
            measurements = []
            for key, value in obj.items():
                if key != timestamp_field:
                    measurements.append("%s=%s" % (key, self.__measurement(value)))
            influx_query += "%s,Category=%s,From=Flame %s %s000000000\n" %\
                            (series, category, ",".join(measurements), round(timestamp))

        # Write to influxdb
        print(influx_query)
        self.__write(influx_query)

    def __query(self, query):
        requests.post('http://localhost:8086/query', data="q=%s" % query)

    def __write(self, data):
        response = requests.post("http://localhost:8086/write?db=%s" % self.__db_name, data)
        print(response.content)

    def __measurement(self, value):
        try:
            int(value)
            return value
        except ValueError:
            return '"' + value + '"'


if __name__ == '__main__':
    fire.Fire(ComputeSessions)


