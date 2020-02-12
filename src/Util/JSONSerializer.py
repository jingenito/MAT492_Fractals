from os import path
import json

class JSONSerializer:

    def __init__(self, filename) :
        self.filename = filename
    
    def set_filename(self, filename) :
        self.filename = filename

    def SerializeJSON(self, data) :
        mode = "w" if path.exists(self.filename) else "x"
        with open(self.filename,mode) as json_file:
            json.dump(data,json_file, default=lambda x: x.__dict__)

    def DeserializeJSON(self) :
        with open(self.filename) as json_file:
            return json.load(json_file)