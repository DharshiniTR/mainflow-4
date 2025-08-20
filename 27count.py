s=input("enter a string:")
words=s.split()
l=""
for word in words:
    if len(word)>len(l):
        l=word
print("longest word:",l)