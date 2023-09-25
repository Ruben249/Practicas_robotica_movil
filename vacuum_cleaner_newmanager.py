from GUI import GUI
from HAL import HAL
import time
# Enter sequential code!
  
tiempo = time.time()
print(tiempo)
  
def forward_state(n):
  HAL.setV(n)
  print("El robot avanza.")
  
def backward_state(n):
  HAL.setV(-n)
  print("El robot retrocede.")    
    
def spin_state(n):
  HAL.setW(n)
  print("El robot gira.")
  
def spiral_state(n, m):
  HAL.setV(n)
  HAL.setW(m)
  print("El robot esta haciendo una espiral.")
    
forward_state(2)
while True:
    spiral_state(0.4, 0.5)
    if HAL.getBumperData().state == 1:
        if HAL.getBumperData().bumper == 0:
          backward_state(2)
          spin_state(1)
          print("Choque a la izquierda")

        else:
          print("Choque centro-izquierda")
          backward_state(2)
          spin_state(-1)
      
    else:
      print("no choca")
    #Comprobar laser  
    
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
    # Enter iterative code!