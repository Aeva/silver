
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
uniform int jitter;
uniform float magnitude;

varying vec3 coord;


void main() {
  vec4 vertex = gl_Vertex;
  coord = vertex.xyz * scale;
  vertex.x = (vertex.x+offset_x) * scale + 1.0;
  vertex.y = (vertex.y+offset_y) * scale + 1.0;
  vertex.z *= scale;

  if (jitter > 0) {
    int phase = jitter-1;
    float dist = magnitude * .05;

    if (phase == 0) {
      vertex.x += dist;
      vertex.y += dist;
    }
    else if (phase == 1) {
      vertex.x += dist;
      vertex.y -= dist;
    }
    else if (phase == 2) {
      vertex.x -= dist;
      vertex.y += dist;
    }
    else if (phase == 3) {
      vertex.x -= dist;
      vertex.y -= dist;
    }
    else if (phase == 4) {
      vertex.x += dist;
    }
    else if (phase == 5) {
      vertex.x -= dist;
    }
    else if (phase == 6) {
      vertex.y += dist;
    }
    else if (phase == 7) {
      vertex.y -= dist;
    }
  }
  gl_Position = gl_ModelViewProjectionMatrix * vertex;
}
