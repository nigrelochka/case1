import turtle

# квадрат
# a – длина стороны квадрата
# (x, y) – координаты левого нижнего угла фигуры
# incline – наклон фигуры в градусах
def kvadrat(x, y, a, color,incline):
    turtle.pencolor(color)
    turtle.fillcolor(color)
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(a)
        print(turtle.position())
        turtle.left(90)
    turtle.end_fill()
    turtle.up()

# прямоугольный треугольник
# katet_gor  – длина горизонтального катета
# katet_vert – длина вертикального катета
# incline – наклон фигуры в градусах
def pryamtreg(x, y, katet_gor, katet_vert, color):
    turtle.pencolor(color)
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


# параллелограмм
# base   – длина основания (горизонтальная сторона)
# height – длина боковой стороны (наклонной)
# angle  – острый угол при основании (в градусах)
# (x, y) – координаты левого нижнего угла фигуры
# incline – наклон фигуры в градусах
def parallelogram(x, y, base, height, angle, color):
    turtle.pencolor(color)
    turtle.fillcolor(color)
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.begin_fill()
    turtle.forward(base)
    turtle.left(180 - angle)
    turtle.forward(height)
    turtle.left(angle)
    turtle.forward(base)
    turtle.left(180 - angle)
    turtle.forward(height)
    turtle.end_fill()
    turtle.setheading(0)
    turtle.up()

# Равнобедренный треугольник
# base  – длина основания
# height – высота
# (x, y) – координаты ЛЕВОГО НИЖНЕГО УГЛА основания
def ravnobedrennyi_treug(base, height, x, y, color):
    left_bottom = (x, y)
    right_bottom = (x + base, y)
    top = (x + base / 2, y + height)
    turtle.color(color)
    turtle.up()
    turtle.goto(left_bottom)
    turtle.down()
    turtle.begin_fill()
    turtle.goto(right_bottom)
    turtle.goto(top)
    turtle.goto(left_bottom)
    turtle.end_fill()
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
    turtle.color(color)
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
# b – ширина прямоугольника
# c – высота прямоугольника
# (x, y) – координаты левого нижнего угла фигуры
def pryamougolnik(x, y, b, c, color):
    turtle.pencolor(color)
    turtle.fillcolor(color)
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(b)
        turtle.left(90)
        turtle.forward(c)
        turtle.left(90)
    turtle.end_fill()
    turtle.up()

# ромб
# k - длина стороны ромба
# ugol - острый угол ромба
# (x, y) - координаты нижнего левого угла ромба
def romb (x,y,k, ugol, color):
    turtle.pencolor(color)
    turtle.fillcolor(color)
    turtle.up
    turtle.goto(x, y)
    turtle.left(ugol)
    turtle.down()
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(k)
        turtle.left(ugol)
        turtle.forward(k)
        turtle.left(180 - ugol)
    turtle.end_fill()
turtle.setup(1400,800)
