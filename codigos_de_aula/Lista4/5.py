A, B = map(int, input("Digite 2 números para encontrar o MDC (maximo divisor comum)\n").split())
if A < B:
    while B != 0 or B != 1 or A!= 1 or B!=0:
        resto = B % A
        B = A
        A = resto
        if A == 1 or B == 1 or A == 0 or B == 0:
            break
    print(f"Resultado: {B}")
else:
    while A != 0 or A != 1 or B != 0 or B != 1:
        resto = A % B
        A = B
        B = resto
        if A == 1 or B == 1 or A == 0 or B == 0:
            break
    print(f"Resultado: {A}")