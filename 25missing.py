l=list(map(int,input("enter list of elements:").split()))
n=len(l)
exp_sum=((n+1)*(n+2))//2
mis=exp_sum-sum(l)
print("missing number:",mis)