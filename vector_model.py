

from model_tools import *
from stl_parser import ascii_stl_parser, binary_stl_parser
from obj_parser import obj_parser




class VectorModel():
    """Class representing the topology of a vector-represented 3D
    model.  Supports obj and stl file formats.  Ignores normal, color,
    texture, and other attribute information, currently."""
    
    def __init__(self, path):
        self.vertbuffer = []
        self.average = [0, 0, 0]
        self.min = [None, None, None]
        self.max = [None, None, None]
        self.width = 0  # x axis
        self.depth = 0  # y axis
        self.height = 0 # z axis

        parsers = {
            "stl" : [
                ("ascii stl", ascii_stl_parser),
                ("binary stl", binary_stl_parser),
                ],
            "obj": [
                ("obj", obj_parser),
                ],
            }

        ext = path.split(".")[-1].lower()
        log = ""
        with open(path, "rb") as fileob:
            for name, parser in parsers[ext]:
                try:
                    log += "Trying {0} parser on {1}...\n".format(name, path)
                    self.vertbuffer = parser(fileob)
                except ParserFailure:
                    log += "Parser failed."
                    fileob.seek(0)

        if not self.vertbuffer:
            raise ParserFailure(
                "Parsing process failed, or model contains no vertices.")

        assert len(self.vertbuffer) % 3 == 0
        self.min = self.vertbuffer[0:3]
        self.max = self.vertbuffer[0:3]

        # divine some metrics from the model
        for i in range(0, len(self.vertbuffer), 3):
            vertex = self.vertbuffer[i:i+3]
            for v in range(3):
                self.average[v] += vertex[v]
                if vertex[v] < self.min[v]:
                    self.min[v] = vertex[v]
                if vertex[v] > self.max[v]:
                    self.max[v] = vertex[v]

        # determine the average coordinate
        for v in range(3):
            self.average[v] /= len(self.vertbuffer)

        # determine model dimensions
        self.width = abs(self.max[0] - self.min[0])
        self.depth = abs(self.max[1] - self.min[1])
        self.height = abs(self.max[2] - self.min[2])
