s=8000
s1=(s*5)/100
s2=(s*10)/100
s3=s+s1
s4=s+s2
if s<10000:
    s5=s+(s*2)/100
    print(s)
    print(s5)
else:    
    while True:
        grade='a'
        if grade in('a','b','c'):
            if grade=='a':
                print('salary =',s)
                print('bonous=',s1)
                print('total=',s3)
                break
            if grade=='b':
                print('salary =',s)
                print('bonous=',s2)
                print('total=',s4)
                break
            else:
                print("nothing")
