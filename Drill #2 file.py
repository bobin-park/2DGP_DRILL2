from pico2d import *
import math
open_canvas()

img = load_image('character.png')
grass = load_image('grass.png')
character=load_image('character.png')
x,y=400,90
cx,cy=400,300
rad ,angle =210,math.radians(90)
rotation = 0
circle =0
Rect=True # 사각형
Tri=False  # 원
while(True):
    while (Rect):
        clear_canvas_now()
        grass.draw_now(400, 30)
        if (y == 90 and x <= 780):
            x = x + 2
            if (x == 400):
                rotation=0
                Tri = True
                Rect = False
                break
        elif (x >= 700 and y <= 560):
            y = y + 2
        elif (y >= 500 and x >= 20):
            x = x - 2
        elif (x <= 100 and y >= 90):
            y = y - 2
        elif (y == 90 and x <= 400):
            x = x + 2
        character.draw_now(x, y)
        delay(0.001)
    while (Tri):
        clear_canvas_now()
        grass.draw_now(400, 30)
        x = cx + rad * math.cos(angle)
        y= cy + rad*math.sin(angle)
        angle-=0.05
        rotation += 0.05
        character.draw_now(x, y)
        if( rotation >= 2 * math.pi):
            circle = 0
            y = 90
            x = 400
            Tri = False
            Rect = True
            break
        delay(0.01)



