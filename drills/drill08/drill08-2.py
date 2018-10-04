import turtle
import random

def draw_character(x,y):
    pass

def draw_curve_10_point_round(p1,p2,p3,p4):
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p1[0] + (3*t**3 - 5*t**2 + 2)*p2[0] + (-3*t**3 + 4*t**2 + t)*p3[0] + (t**3 - t**2)*p4[0])/2
        y = ((-t**3 + 2*t**2 - t)*p1[1] + (3*t**3 - 5*t**2 + 2)*p2[1] + (-3*t**3 + 4*t**2 + t)*p3[1] + (t**3 - t**2)*p4[1])/2
        draw_character((x, y))

    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p2[0] + (3*t**3 - 5*t**2 + 2)*p3[0] + (-3*t**3 + 4*t**2 + t)*p4[0] + (t**3 - t**2)*p1[0])/2
        y = ((-t**3 + 2*t**2 - t)*p2[1] + (3*t**3 - 5*t**2 + 2)*p3[1] + (-3*t**3 + 4*t**2 + t)*p4[1] + (t**3 - t**2)*p1[1])/2
        draw_character((x, y))

    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p3[0] + (3*t**3 - 5*t**2 + 2)*p4[0] + (-3*t**3 + 4*t**2 + t)*p1[0] + (t**3 - t**2)*p2[0])/2
        y = ((-t**3 + 2*t**2 - t)*p3[1] + (3*t**3 - 5*t**2 + 2)*p4[1] + (-3*t**3 + 4*t**2 + t)*p1[1] + (t**3 - t**2)*p2[1])/2
        draw_character((x, y))

    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p4[0] + (3*t**3 - 5*t**2 + 2)*p1[0] + (-3*t**3 + 4*t**2 + t)*p2[0] + (t**3 - t**2)*p3[0])/2
        y = ((-t**3 + 2*t**2 - t)*p4[1] + (3*t**3 - 5*t**2 + 2)*p1[1] + (-3*t**3 + 4*t**2 + t)*p2[1] + (t**3 - t**2)*p3[1])/2
        draw_character((x, y))

n=1
points =[(random.randint(-400,400),random.randint(-300,300))for i in range(10)]

draw_curve_10_point_round(points[n-1],points[n],points[n+1],points[n+2])
n=(n+1)%10