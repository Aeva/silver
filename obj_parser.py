

from model_tools import *


def obj_parser(fileob):
    """
    Parser for wavefront obj files.  File format reference:
    http://en.wikipedia.org/wiki/Wavefront_.obj_file
    """

    verts = []
    vertbuffer = []

    for line in fileob:
        if line.strip()[0] == "v":
            verts.append(str2vector(line))
        if line.strip()[0] == "f":
            params = line.strip().split(" ")[1:]
            if line.count("/"):
                params = [p.split("/")[0] for p in params]
            params = map(lambda x:int(x)-1, params)
            for i in params:
                vertbuffer += verts[i]

    return vertbuffer
