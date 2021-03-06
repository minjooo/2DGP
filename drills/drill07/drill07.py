import turtle
import random
from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

#def stop():
#    turtle.bye()


#def prepare_turtle_canvas():
#    turtle.setup(1024, 768)
#    turtle.bgcolor(0.2, 0.2, 0.2)
#    turtle.penup()
# #   turtle.hideturtle()
#    turtle.shape('arrow')
#    turtle.shapesize(2)
#    turtle.pensize(5)
#    turtle.color(1, 0, 0)
#    turtle.speed(100)
#    turtle.goto(-500, 0)
#    turtle.pendown()
#    turtle.goto(480, 0)
#    turtle.stamp()
#    turtle.penup()
#    turtle.goto(0, -360)
#    turtle.pendown()
#    turtle.goto(0, 360)
#    turtle.setheading(90)
#    turtle.stamp()
#    turtle.penup()
#    turtle.home()
#
#    turtle.shape('circle')
#    turtle.pensize(1)
#    turtle.color(0, 0, 0)
#    turtle.speed(50)
#
#    turtle.onkey(stop, 'Escape')
#    turtle.listen()
#
#
#def draw_big_point(p):
#    turtle.goto(p)
#    turtle.color(0.8, 0.9, 0)
#    turtle.dot(15)
#    turtle.write('     '+str(p))
#
#
#def draw_point(p):
#    turtle.goto(p)
#    turtle.dot(5, random.random(), random.random(), random.random())


#def draw_line_basic(p1, p2): # y축과 평행인 직선을 그리지 못함
#    draw_big_point(p1)
#    draw_big_point(p2)
#
#    x1,y1=p1[0],p1[1]
#    x2,y2=p2[0],p2[1]
#
#    a=(y2-y1)/(x2-x1)
#    b=y1-x1*a
#
#    for x in range (x1,x2+1,20): #_ 맨 마지막 숫자 늘리면 듬성듬성
#        y=a*x+b
#        draw_point((x,y))
#
#    draw_point(p2)
#    pass


#def draw_line(p1, p2):
#    draw_big_point(p1)
#    draw_big_point(p2)
#
#    for i in range (0,100+1,4):
#        t=i/100
#        x=(1-t)*p1[0]+t*p2[0]
#        y=(1-t)*p1[1]+t*p2[1]
#        draw_point((x,y))
#
#    draw_point(p2)
#    pass
#
#
#prepare_turtle_canvas()

# draw_line_basic((-100,200),(300,-200))
# draw_line((-100,300),(400,-300))
open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')


size=6
points = [(random.randint(-500,500),random.randint(-350,350)) for i in range(size)]
n=1

global frame

def draw_character(x,y):
    character.clip_draw(frame*100,100*1,100,100,x,y)
    pass
def move_character(p1,p2):
    for i in range(0, 100 + 1, 1):
        t=i/100
        x=(1-t)*p1[0]+t*p2[0]
        y=(1-t)*p1[1]+t*p2[1]
        draw_character(x,y)
        frame=(frame+1)%8
    pass

frame=0

while True:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    move_character(points[n-1], points[n])
    update_canvas()
    delay(0.02)
    n = (n + 1) % size

turtle.done()