# Step_1: extract a, b, and c from user input and storing it to variables.
eq = '4x^2 +4x + (-8) = 0'

a = int(eq.replace(' ', '').split('x')[0])
b = int(eq.replace(' ', '').split('+')[1].split('x')[0])
c = int(eq.replace(' ', '').split('=')[0].split('+')[2].strip('()'))

print(a,b,c) 

# Step_2: find x1 and x2
x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
x2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)

print(x1,x2)