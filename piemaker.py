from dataclasses import dataclass
from designer import *
from random import randint
import math

@dataclass
class World:
    crust: DesignerObject
    filling: DesignerObject
    toppings: list[DesignerObject]
    slices: list[DesignerObject]
    
    
def create_world() -> World:
    crust_size = 100#randint(50,150)
    center_x = get_width()/2#randint(200,600)
    center_y = get_height()/2#randint(200,600)
    return World(
        circle("red",crust_size,center_x,center_y),
        circle("blue",crust_size-10,center_x,center_y),
        [],
        make_slices(crust_size,center_x,center_y)
        )

def make_slices(radius,center_x,center_y) -> list[DesignerObject]:
    output = []
    slice_num = randint(2,8)
    for i in range(slice_num):
        line_angle = ((360/slice_num) * i)* math.pi / 180
        output.append(line('black',
                           center_x,
                           center_y,
                           center_x+(radius*math.cos(line_angle)),
                           center_y+(radius*math.sin(line_angle)),
                           thickness = 4
                           )
                      )
    return output

when('starting',create_world)

start()