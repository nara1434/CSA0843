
a=float(input("enter the vlaue of a:"))
b=float(input("enter the value of b:"))
c=float(input("enter the value of c:"))
dis=(b**2)-(4*a*c)
if(dis>0):
    print('roots are real')
elif(dis<0):
    print('roots are imaginary')
elif(dis==0):
    print('roots are real')
else:
    print('enter the vakid expression')
r1=(-b+(dis**0.5))/2*a
r2=(-b-(dis**0.5))/2*a
print(r1)
print(r2)
