a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
s1=a**2
s2=b**2
s3=c**2
if s1==s2+s3 or s3==s1+s2 or s2==s1+s3:
     print("true")
else:
     print("false")