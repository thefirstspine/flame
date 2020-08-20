import json


class BaseCommand:
    outputs_to = None

    def __init__(self, outputs_to="python"):
        self.outputs_to = outputs_to

    def output(self, data):
        if self.outputs_to == "json":
            return json.dumps(data)
        else:
            return data
