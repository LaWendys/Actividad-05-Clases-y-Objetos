import math
from math import sqrt

def distancia_euclidiana(origen_x, origen_y, destino_x, destino_y):
    
    x_1=origen_x
    y_1=origen_y
    x_2=destino_x
    y_2=destino_y
    
    return sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2) 
