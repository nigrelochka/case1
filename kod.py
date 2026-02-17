import turtle

# квадрат
# a – длина стороны квадрата
# (x, y) – координаты левого нижнего угла фигуры
# incline – наклон фигуры в градусах
def kvadrat(x, y, a, color):
    turtle.fillcolor(color)
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(a)
        turtle.left(90)
    turtle.end_fill()
    turtle.up()

# прямоугольный треугольник
# katet_gor  – длина горизонтального катета
# katet_vert – длина вертикального катета
def pryamtreg(x, y, katet_gor, katet_vert, color):
    turtle.fillcolor(color)
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.begin_fill()
    turtle.forward(katet_gor)
    turtle.left(90)
    turtle.forward(katet_vert)
    turtle.goto(x, y)
    turtle.end_fill()
    turtle.setheading(0)
    turtle.up()

# base - длина основания
# side - длина боковых сторон
# x, y - координаты левого нижнего угла основания
# color - цвет треугольника
def ravnobedrennyi_treug(base, side, x, y, color):
    import math
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.fillcolor(color)
    turtle.begin_fill()
    if side <= base / 2:
        return print("Боковая сторона должна быть больше половины основания!")
    # Вычисляем угол при основании
    ugol = math.degrees(math.acos((base / 2) / side))
    turtle.forward(base)
    turtle.left(180 - ugol)
    turtle.forward(side)
    turtle.left(2 * ugol)
    turtle.forward(side)
    turtle.end_fill()
    turtle.setheading(0)
    turtle.up()

#Равносторонний треугольник
# x, y - координаты начала рисования (левый нижний угол основания)
# size - длина стороны треугольника
def triangle(x, y, size, color):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(size)
        turtle.left(120)
    turtle.end_fill()
    turtle.setheading(0)
    turtle.up()

# Трапеция (равнобедренная)
# base_bottom – нижнее основание
# base_top    – верхнее основание
# height      – высота
# (x, y)      – координаты ЛЕВОГО НИЖНЕГО УГЛА нижнего основания
def trapeziya(base_bottom, base_top, height, x, y, color):
    left_bottom = (x, y)
    right_bottom = (x + base_bottom, y)
    left_top = (x + (base_bottom - base_top) / 2, y + height)
    right_top = (x + (base_bottom - base_top) / 2 + base_top, y + height)
    turtle.fillcolor(color)
    turtle.up()
    turtle.goto(left_bottom)
    turtle.down()
    turtle.begin_fill()
    turtle.goto(right_bottom)
    turtle.goto(right_top)
    turtle.goto(left_top)
    turtle.goto(left_bottom)
    turtle.end_fill()
    turtle.up()

# прямоугольник
# shirina – ширина прямоугольника
# height – высота прямоугольника
# (x, y) – координаты левого нижнего угла фигуры
def pryamougolnik(x, y, shirina, height, color):
    turtle.fillcolor(color)
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(shirina)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()
    turtle.up()

# ромб
# k - длина стороны ромба
# angle - острый угол ромба
# (x, y) - координаты нижнего левого угла ромба
def romb(x, y, k, angle, color):
    turtle.fillcolor(color)
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.begin_fill()
    turtle.left(angle)
    for i in range(2):
        turtle.forward(k)
        turtle.left(angle)
        turtle.forward(k)
        turtle.left(180 - angle)
    turtle.end_fill()
    turtle.setheading(0)

def cat_head():
    turtle.setheading(45)
    kvadrat(-550, 200, 75, '#E0B672')  # голова
    turtle.setheading(-45)
    pryamtreg(-496.97, 253.03, -75, 75, '#CC8A6E')  # правое ухо
    turtle.setheading(45)
    pryamtreg(-603.03, 253.03, 75, 75, '#FFDBBB')  # левое ухо

def cat_body():
    turtle.setheading(-45)
    kvadrat(-550, 200, 75, '#E0B672')  # шея
    turtle.setheading(-45)
    pryamtreg(-496.97, 253.00, 75, 75, '#FFDBBB')  # спина
    turtle.setheading(-45 * 3)
    kvadrat(-390.90, 253.00, 75, '#E0B672')  # живот
    turtle.setheading(-45 * 3)
    pryamtreg(-496.97, 146.97, -75, 75, '#CC8A6E')  # лапа правая
    turtle.setheading(45 * 3)
    pryamtreg(-496.97, 146.97, 75, 75, '#CC8A6E')  # лапа левая

def cat_hvost():
    turtle.setheading(-45)
    pryamtreg(-337.87, 199.97, -75, 75, '#E0B672')  # начало хвоста
    turtle.setheading(45)
    pryamtreg(-390.90, 253, 75, 75, '#CC8A6E')  # кончик хвоста

def cat_levi_verni_ygol():
    cat_head()
    cat_body()
    cat_hvost()

def home():
    pryamougolnik(-530, -200, 30, 100, 'gray')
    kvadrat(-550, -300, 150, '#DEA785')
    ravnobedrennyi_treug(150, 100, -550, -150, '#BC6C54')
    pryamougolnik(-535, -300, 35, 70, '#61212D')
    kvadrat(-475, -250, 50, '#FFF9A3')
    pryamougolnik(-452, -250, 4, 50, '#61212D')
    pryamougolnik(-475, -227, 50, 4, '#61212D')

def tree():
    pryamougolnik(-350, -300, 40, 130, 'brown')
    kvadrat(-420, -250, 100, '#2C592E')
    kvadrat(-380, -180, 120, '#84C77F')
    kvadrat(-340, -235, 110, 'green')

def zabor():
    x = -600
    for i in range(10):
        x1 = x + (35 * i)
        pryamougolnik(x1, -320, 35, 40, '#BE8B71')
        triangle(x1, -280, 35, '#BE8B71')

def dacha():
    home()
    tree()
    zabor()

def body_fish(x_offset, y_offset):
    trapeziya(150, 100, 80, -100 + x_offset, 0 + y_offset, "#FA7305")

def tail_fish(x_offset, y_offset):
    ravnobedrennyi_treug(80, 60, -120 + x_offset, 40 + y_offset, "#FCA47C")

def fin_fish(x_offset, y_offset):
    pryamtreg(-50 + x_offset, 80 + y_offset, 50, 30, "#F9D779")

def eye_fish(x_offset, y_offset):
    kvadrat(20 + x_offset, 30 + y_offset, 10, "black")

def mouth_fish(x_offset, y_offset):
    ravnobedrennyi_treug(15, 12, 30 + x_offset, 10 + y_offset, "pink")

def bubbles(x_offset, y_offset):
    kvadrat(50 + x_offset, 35 + y_offset, 10, 'lightblue')
    kvadrat(62 + x_offset, 49 + y_offset, 13, '#92A7D6')
    kvadrat(58 + x_offset, 67 + y_offset, 10, 'lightblue')
    kvadrat(49 + x_offset, 80 + y_offset, 7, '#92A7D6')
    kvadrat(65 + x_offset, 80 + y_offset, 7, '#92A7D6')
    kvadrat(58 + x_offset, 90 + y_offset, 5, 'lightblue')

def origami_fish(x_offset, y_offset):
    body_fish(x_offset, y_offset)
    tail_fish(x_offset, y_offset)
    fin_fish(x_offset, y_offset)
    eye_fish(x_offset, y_offset)
    mouth_fish(x_offset, y_offset)
    bubbles(x_offset, y_offset)

def ship_hullt(x_offset, y_offset):
    trapeziya(200, 280, 50, -100 + x_offset, -50 + y_offset, "#784F2E")
    pryamougolnik(-130 + x_offset, -25 + y_offset, 260, 5, "gold")

def mast(x_offset, y_offset):
    pryamougolnik(-6 + x_offset, -30 + y_offset, 12, 180, "#A56D50")

def front_sail(x_offset, y_offset):
    ravnobedrennyi_treug(100, 100, -50 + x_offset, 30 + y_offset, "#CD5C5C")

def upper_sail(x_offset, y_offset):
    ravnobedrennyi_treug(50, 40, 0 + x_offset, 118 + y_offset, "#F9D779")

def flag(x_offset, y_offset):
    turtle.right(90)
    romb(25 + x_offset, 140 + y_offset, 20, 60, "#FB3811")

def windows(x_offset, y_offset):
    kvadrat(-58 + x_offset, -30 + y_offset, 15, "lightblue")
    kvadrat(40 + x_offset, -30 + y_offset, 15, "lightblue")

def sailboat(x_offset, y_offset):
    mast(x_offset, y_offset)
    ship_hullt(x_offset, y_offset)
    front_sail(x_offset, y_offset)
    upper_sail(x_offset, y_offset)
    flag(x_offset, y_offset)
    windows(x_offset, y_offset)

def heart():
    kvadrat(-75, -75, 150, '#E47C9C')
    trapeziya(200, 100, 75, 0, 75, '#EEF1F8')
    trapeziya(200, 100, 75, -200, 75, '#D99BD8')
    turtle.setheading(180)
    pryamtreg(-200, 75, -125, 150, '#908DCE')
    turtle.setheading(180)
    pryamtreg(200, 75, 125, 150, '#A1C3E7')
    turtle.setheading(180)
    ravnobedrennyi_treug(150, 110, 75, -75, '#F6A0AC')

turtle.setup(1400, 800)
turtle.speed(30)
heart()
cat_levi_verni_ygol()
dacha()
origami_fish(350, 220)
origami_fish(600, 200)
origami_fish(480, 80)
sailboat(400, -250)
turtle.hideturtle()
turtle.done()








