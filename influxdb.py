import fire
import json
import os
import requests


class ComputeSessions:
    __db_name = "flame"
    __python_executable = "python3"

    def setup(self):
        self.__query("CREATE DATABASE %s" % self.__db_name)

    def push(self, command, path=None):
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
            measurements.append("%s=%s" % (key, value))

        # Write to influxdb
        self.__write("%s,Category=%s,From=Flame %s" % (series, category, ",".join(measurements)))

    def __query(self, query):
        requests.post('http://localhost:8086/query', data="q=%s" % query)

    def __write(self, data):
        requests.post("http://localhost:8086/write?db=%s" % self.__db_name, data)


if __name__ == '__main__':
    fire.Fire(ComputeSessions)

