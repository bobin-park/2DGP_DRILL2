from pico2d import *

open_canvas()

img = load_image('character.png')
grass = load_image('grass.png')
character=load_image('character.png')
x=800  # 시작 위치를 오른쪽 끝으로 변경
while(x>0):  # x가 0보다 클 때까지 반복
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,90)
    x=x-2  # x 좌표 감소
    delay(0.01)

close_canvas()
