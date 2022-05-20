# Quadratic Formula Solver MH 5/22
def quadformula(a,b,c):
    discriminant=b**2-4*a*c 
    # This helps us "discriminate" the type of solution we will have.
    sol1=(-b+discriminant**.5)/2*a
    sol2=(-b-discriminant**.5)/2*a
    if discriminant==0:
        print(f'A double solution exists at x = {sol1}.')
    elif discriminant<0:
        print(f'Two complex solutions exist at x = {sol1} and x = {sol2}.')
    else:
        print(f'Two solutions exist at x = {sol1} and x = {sol2}.')

a = int(input('In the quadratic standard form ax**2 + bx + c = 0, what is the value of a? '))
b = int(input('What is the value of b? '))
c = int(input('What is the value of c? '))

quadformula(a,b,c)
