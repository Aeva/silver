
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
