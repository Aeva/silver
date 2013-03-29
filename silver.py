#!/usr/bin/env python

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


import sys
import math
import time
import pyglet
from pyglet.gl import *
from glsl import Shader
from vector_model import VectorModel


def setup_context(model, scale=1.0):
    width = int(math.ceil(model.width)*scale)+2
    height = int(math.ceil(model.depth)*scale)+2
    window = pyglet.window.Window(width, height, visible=True)
    with open("vertex.glsl", "r") as fileob:
        vert = fileob.read()
    with open("fragment.glsl", "r") as fileob:
        frag = fileob.read()
    shader = Shader(vert, frag)
    shader.bind()
    shader.uniformf("offset_x", (model.min[0]*-1))
    shader.uniformf("offset_y", (model.min[1]*-1))
    shader.uniformf("scale", scale)
    window.shader = shader

    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    gl.glOrtho(0, width, 0, height, -1, 1)
    gl.glMatrixMode(gl.GL_MODELVIEW)

    return window


def dump_buffer():
    buffers = pyglet.image.get_buffer_manager()
    color_buffer = buffers.get_color_buffer()
    color_buffer.save("test.png")
    

def render(model):
    vert_count = len(model.vertbuffer)
    vertices = (GLfloat * vert_count)(*model.vertbuffer)
    glEnableClientState(GL_VERTEX_ARRAY)
    glVertexPointer(3, GL_FLOAT, 0, vertices)
    glDrawArrays(GL_TRIANGLES, 0, vert_count/3)


def process(ctx, model):
    @ctx.event
    def on_draw():
        ctx.shader.uniformi("jitter", 0)
        ctx.shader.uniformf("magnitude", 0.0)
        render(model)

        for mag in range(1,10):
            ctx.shader.uniformf("magnitude", mag)
            for jit in range(1,9):
                ctx.shader.uniformi("jitter", jit)

                render(model)

    #pyglet being weird... why does this need to happen thrice?
    for i in range(2):
        pyglet.clock.tick()
        ctx.clear()
        ctx.switch_to()
        ctx.dispatch_events()
        ctx.dispatch_event('on_draw')
        ctx.flip()

    print "--> Rendered %s faces." % (len(model.vertbuffer)/3)
    dump_buffer()
    

if __name__ == "__main__":
    print "--> Parsing model..."
    model = VectorModel(sys.argv[1])
    print "--> Rendering crossections..."
    ctx = setup_context(model, 5)

    ctx.shader.uniformf("layer_height", .4)
    ctx.shader.uniformf("target_layer", 1)

    process(ctx, model)
    import pdb; pdb.set_trace()
