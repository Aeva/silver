
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


varying vec3 coord;
uniform float layer_height;
uniform float target_layer;


void main() {
  if (coord.z < 0.0 && target_layer < 1.0) {
    gl_FragColor = vec4(1.0, 1.0, 1.0, 1.0);
  }
  else if (coord.z > (target_layer + layer_height)) {
    discard;
  }
  else {
    float layer_start = target_layer * layer_height;
    if (coord.z >= layer_start && coord.z <= layer_start + layer_height) {
      gl_FragColor = vec4(1.0, 1.0, 1.0, 1.0);
    }
    else {
      //gl_FragColor = vec4(0.1, 0.1, 0.1, 1.0);
      discard;
    }
  }
}
