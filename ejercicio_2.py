# ejercicio2_roseta.py

from PIL import Image
import math

# Funcion BRESENHAM

def bresenham(pixels, x0, y0, x1, y1, color, ancho, alto):
    dx, dy = abs(x1 - x0), abs(y1 - y0)

    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1

    err = dx - dy

    x, y = x0, y0

    while True:

        if 0 <= x < ancho and 0 <= y < alto:
            pixels[x, y] = color

        if x == x1 and y == y1:
            break

        e2 = 2 * err

        if e2 > -dy:
            err -= dy
            x += sx

        if e2 < dx:
            err += dx
            y += sy


# Generar puntos sobre una circunferencia

def generar_puntos_circulo(cx, cy, radio, n):

    puntos = []

    for i in range(n):

        angulo = 2 * math.pi * i / n

        x = cx + int(radio * math.cos(angulo))
        y = cy + int(radio * math.sin(angulo))

        puntos.append((x, y))

    return puntos

# Cakcular color 
def calcular_color(i, j, n):

    valor = (i + j) / (2 * n)

    r = int(255 * valor)
    g = int(255 * (1 - valor))

    b = int(
        128
        + 127 * math.sin(valor * math.pi)
    )

    return (r, g, b)


# Dibujar la roseta

def dibujar_roseta(pixels, puntos, ancho, alto):

    n = len(puntos)

    for i in range(n):

        for j in range(i + 1, n):

            x0, y0 = puntos[i]
            x1, y1 = puntos[j]

            color = calcular_color(i, j, n)

            bresenham(
                pixels,
                x0,
                y0,
                x1,
                y1,
                color,
                ancho,
                alto
            )


# Generar las variaciones

ancho, alto = 700, 700

cx, cy = 350, 350

radio = 300


for n in [12, 24, 36]:

    print(f"Generando roseta con N={n}...")

    imagen = Image.new(
        "RGB",
        (ancho, alto),
        "white"
    )

    pixels = imagen.load()

    puntos = generar_puntos_circulo(
        cx,
        cy,
        radio,
        n
    )

    dibujar_roseta(
        pixels,
        puntos,
        ancho,
        alto
    )

    nombre_archivo = f"roseta_{n}.png"

    imagen.save(nombre_archivo)

    print(f"✓ {nombre_archivo} generada")


print("\nSe generaron las tres rosetas.")