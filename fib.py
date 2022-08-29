
a=int(input("enter the number of numbers we need :"))
f1=0
f2=1
print(f1,f2)
f3=f1+f2
print(f3)
for i in range(2,a+1):
    (f1,f2)=(f2,f3)
    f3=f1+f2
    print(f3)    
    
