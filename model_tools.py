

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




class ParserFailure(Exception):
    pass


def str2vector(line, expected=3, skip=1, delim=" "):
    """Parses a vector out of a string."""

    try:
        return tuple(map(float, line.strip().split(delim)[skip:])[:expected])
    except:
        raise ParserFailure("str2vector tripped on a line.")
