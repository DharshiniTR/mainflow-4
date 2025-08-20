s=input("enter a string:")
bal=True
stack=[]
for char in s:
    if char in "{[(":
        stack.append(char)
    else:
        if not stack:
            bal=False
            break
        top=stack.pop()
        if(char=="}" and top!="{") or (char==")" and top!="(") or (char=="]" and top!="["):
            bal=False
            break
if bal and not stack:
    print("Balanced True")
else:
    print("not balanace false")

