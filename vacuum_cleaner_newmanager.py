from GUI import GUI
from HAL import HAL
import time
import random

actual_time = time.time()


def forward_state(n):
    HAL.setW(0)
    HAL.setV(n)


def backward_state(n):
    HAL.setW(0)
    HAL.setV(-n)
    print("El robot retrocede.")


def spin_state(n):
    HAL.setW(n)
    HAL.setV(1)
    print("El robot gira.")


def spiral_state(n, m):
    HAL.setV(n)
    HAL.setW(m)
    print("El robot esta haciendo una espiral.")


def contador_choque():
    tiempo_choque = time.time()
    backward_state(0.5)
    controlador = True

    while controlador:
        tiempo_actualizado = time.time()
        if tiempo_actualizado - tiempo_choque >= 2:
            controlador = False
        else:
            backward_state(0.5)


def contador_giro(n):
    tiempo_giro = time.time()
    spin_state(n)
    controlador = True

    while controlador:
        tiempo_actualizado = time.time()
        if tiempo_actualizado - tiempo_giro >= 1:
            forward_state(1)
            controlador = False
        else:
            spin_state(n)


forward_state(1)

while True:
    new_time = time.time()

    if new_time - actual_time >= 7:
        actual_time = new_time
        dado = random.randint(1, 100)
        print("Lanzar dados")
        if dado <= 33:
            vel_angular = random.uniform(0, 1.5)
            vel_lineal = vel_angular + 0.4
            spiral_state(vel_lineal, vel_angular)

    if HAL.getBumperData().state == 1:
        if HAL.getBumperData().bumper == 0:
            contador_choque()
            contador_giro(2.5)
            print("Choque a la izquierda")

        elif HAL.getBumperData().bumper == 2:
            print("Choque derecha")
            contador_choque()
            contador_giro(-1.3)

        else:
            print("Choque centro")
            contador_choque()
            lado = random.randint(1, 2)
            if lado == 1:
                contador_giro(-1.2)
            else:
                contador_giro(1.4)


    else:
        print("no choca")
    # Comprobar laser  