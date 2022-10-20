# -----------------------------------------------------------------------------
# IMPORTS
# -----------------------------------------------------------------------------

from svg.svg import *
from random import randint

# -----------------------------------------------------------------------------
# FUNCIONES
# -----------------------------------------------------------------------------

def randomSVG():
    figura = randint(1,2)
    if figura == 1 :
        return dibujarTriangulo()
    elif figura == 2 :
        return dibujarRectangulo()

def dibujarTriangulo():
    scene  = Scene("triangle")
    point1 = (randint(10,490),randint(10,490))
    point2 = (randint(10,490),randint(10,490))
    point3 = (randint(10,490),randint(10,490))
    points = [point1,point2,point3]
    fill_color = (randint(0,255),randint(0,255),randint(0,255))
    line_color = (randint(0,255),randint(0,255),randint(0,255))
    line_width = randint(1,4)
    scene.add(Polygon(points,fill_color,line_color,line_width))
    return scene.strarray()

def dibujarRectangulo():
    scene  = Scene("rectangle")
    origin = (randint(50,200),randint(50,200))
    height = randint(50,200)
    width  = randint(50,200)
    fill_color = (randint(0,255),randint(0,255),randint(0,255))
    line_color = (randint(0,255),randint(0,255),randint(0,255))
    line_width = randint(1,4)
    scene.add(Rectangle(origin,height,width,fill_color,line_color,line_width))
    return scene.strarray()

# -----------------------------------------------------------------------------
# MAIN
# -----------------------------------------------------------------------------

if __name__ == "__main__": 
    randomSVG()
