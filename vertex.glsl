
/*
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
*/


uniform float offset_x;
uniform float offset_y;
uniform float scale;


void main() {
  vec4 vertex = gl_Vertex;
  vertex[0] = (vertex[0]+offset_x) * scale + 1.0;
  vertex[1] = (vertex[1]+offset_y) * scale + 1.0;
  vertex[2] *= scale;
  gl_Position = gl_ModelViewProjectionMatrix * vertex;
}
