#!/usr/bin/env python

import sys
import math
import time
import pyglet
from pyglet.gl import *
from glsl import Shader
from vector_model import VectorModel


def setup_context(model, scale=5.0):
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
    

if __name__ == "__main__":
    print "--> Parsing model..."
    model = VectorModel(sys.argv[1])
    print "--> Rendering crossections..."
    ctx = setup_context(model)
    #gl.glColor3f(1.0, 1.0, 1.0)
    
    @ctx.event
    def on_draw():
        render(model)

    #pyglet being weird... why does this need to happen thrice?
    for i in range(3):
        pyglet.clock.tick()
        ctx.clear()
        ctx.switch_to()
        ctx.dispatch_events()
        ctx.dispatch_event('on_draw')
        ctx.flip()

    print "--> Rendered %s faces." % (len(model.vertbuffer)/3)

    dump_buffer()
