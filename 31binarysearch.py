arr=list(map(int,input("enter array of elements:").split()))
k=int(input("enter k:"))
l=0
f=False
h=len(arr)-1
while l<=h:
    m=(h+l)//2
    if arr[m]==k:
        print("{} found at {}".format(k,m))
        f=True
        break
    elif arr[m]>k:
        h=m-1
    else:
        l=m+1
if not f:
    print("{} not found".format(k))
    