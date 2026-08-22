'''Dois drones estão voando em um campo e suas posições são dadas pelas coordenadas (x, y).
Faça um programa que leia as coordenadas (x1, y1) do primeiro drone e (x2, y2) do segundo drone.
Calcule e imprima a distância em linha reta entre eles.'''

X1, Y1, X2, Y2 = map(float, input().split())
from math import sqrt
print (f"D = {sqrt((X2-X1)**2)+(Y2-Y1)**2}")