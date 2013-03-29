

import struct
from model_tools import *
from obj_parser import obj_parser




def ascii_stl_parser(fileob):
    """
    Parser for ascii-encoded stl files.  File format reference:
    http://en.wikipedia.org/wiki/STL_%28file_format%29#ASCII_STL
    """

    vertbuffer = []
    for line in fileob:
        try:
            if line.strip()[0].startswith("vertex"):
                vertbuffer += str2vector(line)
        except IndexError:
            raise ParserFailure("ascii_stl_parser tripped on a line.")
    return vertbuffer




def binary_stl_parser(fileob):
    """
    Parser for binary-encoded stl files.  File format reference:
    http://en.wikipedia.org/wiki/STL_%28file_format%29#Binary_STL
    """

    vertbuffer = []
    fileob.seek(80) # skip the header
    count = struct.unpack("<I", fileob.read(4))[0]
    for i in range(count):
        fileob.read(12) # skip the normal vector
        for v in range(3):
            vertbuffer += struct.unpack("<3f", fileob.read(12))
        fileob.read(2) # skip the attribute bytes
    return vertbuffer


        
