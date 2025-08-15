import math

def roots(a, b, c):
    r = math.sqrt(b**2 - 4*a*c)
    r1 = (-b + r)/(2*a)
    r2 = (-b - r)/(2*a)
    return r1, r2

a = float(input('กรอกค่า a: '))
b = float(input('กรอกค่า b: '))
c = float(input('กรอกค่า c: '))
x = roots(a, b, c)
print(f'{x}')

a = float(input('กรอกค่า a: '))
b = float(input('กรอกค่า b: '))
c = float(input('กรอกค่า c: '))
print(f'{roots(a, b, c)}')

def solve():
    a = float(input('กรอกค่า a: '))
    b = float(input('กรอกค่า b: '))
    c = float(input('กรอกค่า c: '))
    x = roots(a, b, c)
    print(f'{x}')

solve()
solve()
solve()
