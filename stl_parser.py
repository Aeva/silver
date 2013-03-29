

# This file is part of Silver.
#
# Silver is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Silver is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with VoxelPress.  If not, see <http://www.gnu.org/licenses/>.
#
# Have a nice day!




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


        
