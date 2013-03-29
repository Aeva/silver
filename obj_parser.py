

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
