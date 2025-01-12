import turtle

def draw_fractal(t, length, angle, level):
    if level == 0:
        t.forward(length)
    else:
        draw_fractal(t, length / 3, angle, level - 1)
        t.left(angle)
        draw_fractal(t, length / 3, angle, level - 1)
        t.right(2 * angle)
        draw_fractal(t, length / 3, angle, level - 1)
        t.left(angle)
        draw_fractal(t, length / 3, angle, level - 1)

def main():
    
    window = turtle.Screen()
    window.bgcolor("black")
    t = turtle.Turtle()

   
    t.color("white")
    t.speed(0)
    t.up()
    t.goto(-200, -200)
    t.down()

    # Рисуем фрактал
    draw_fractal(t, 400, 60, 5)

    # Завершаем программу при клике на экран
    window.exitonclick()

if __name__ == "__main__":
    main()