# ejercicio1_casa.py

from PIL import Image
import math


# Funcion DDA
def dda(pixels, x0, y0, x1, y1, color, ancho, alto):
    dx, dy = x1 - x0, y1 - y0
    pasos = max(abs(dx), abs(dy))

    if pasos == 0:
        return

    x_inc, y_inc = dx / pasos, dy / pasos
    x, y = x0, y0

    for _ in range(int(pasos) + 1):
        px, py = round(x), round(y)

        if 0 <= px < ancho and 0 <= py < alto:
            pixels[px, py] = color

        x += x_inc
        y += y_inc


# Funcion para dibujar rectangulos

def dibujar_rectangulo(pixels, x0, y0, x1, y1, color, ancho, alto):
    # Linea superior
    dda(pixels, x0, y0, x1, y0, color, ancho, alto)

    # Linea derecha
    dda(pixels, x1, y0, x1, y1, color, ancho, alto)

    # Linea inferior
    dda(pixels, x1, y1, x0, y1, color, ancho, alto)

    # Linea izquierda
    dda(pixels, x0, y1, x0, y0, color, ancho, alto)

# Funcion para dibujar triangulos

def dibujar_triangulo(pixels, p1, p2, p3, color, ancho, alto):

    dda(
        pixels,
        p1[0], p1[1],
        p2[0], p2[1],
        color,
        ancho,
        alto
    )

    dda(
        pixels,
        p2[0], p2[1],
        p3[0], p3[1],
        color,
        ancho,
        alto
    )

    dda(
        pixels,
        p3[0], p3[1],
        p1[0], p1[1],
        color,
        ancho,
        alto
    )

# Funcion para dibujar el sol

def dibujar_sol(pixels, cx, cy, radio, n_rayos, color, ancho, alto):

    for i in range(n_rayos):

        angulo = i * 2 * math.pi / n_rayos

        x = cx + int(radio * math.cos(angulo))
        y = cy + int(radio * math.sin(angulo))

        dda(
            pixels,
            cx,
            cy,
            x,
            y,
            color,
            ancho,
            alto
        )

# PROGRAMA PRINCIPAL

ancho, alto = 600, 500

# Fondo celeste
imagen = Image.new(
    "RGB",
    (ancho, alto),
    (200, 230, 255)
)

pixels = imagen.load()

# Cuerpo de la casa

dibujar_rectangulo(
    pixels,
    150, 220,
    450, 420,
    (40, 100, 200),
    ancho,
    alto
)

# Techo

dibujar_triangulo(
    pixels,
    (130, 220),
    (300, 100),
    (470, 220),
    (200, 50, 50),
    ancho,
    alto
)


# Puerta

dibujar_rectangulo(
    pixels,
    270, 320,
    330, 420,
    (120, 70, 30),
    ancho,
    alto
)

# Ventana izquierda

dibujar_rectangulo(
    pixels,
    180, 270,
    230, 320,
    (30, 180, 220),
    ancho,
    alto
)

# Ventana derecha

dibujar_rectangulo(
    pixels,
    370, 270,
    420, 320,
    (30, 180, 220),
    ancho,
    alto
)

# Sol

dibujar_sol(
    pixels,
    80,
    80,
    55,
    8,
    (255, 180, 0),
    ancho,
    alto
)


# Linea de piso

dda(
    pixels,
    0,
    420,
    ancho - 1,
    420,
    (50, 160, 70),
    ancho,
    alto
)


# Guardar imagen

imagen.save("casa.png")

print("casa.png generada correctamente")