"""Faça um programa que leia um número inteiro de 3 dígitos (exemplo: 485). Usando apenas
operações matemáticas (proibido converter para string), extraia e imprima separadamente o
dígito das centenas, o das dezenas e o das unidades. Ao final, imprima o número invertido
(exemplo: 584)."""

A, B, C = map(int, input().split())
A, B = A//100, B//10
print (f"{C}\n{B}\n{A}")