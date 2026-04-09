s = input("enter the text: ")
rev = ""
for i in range(len(s)-1,-1,-1):
    rev = rev + s[i]
print(rev,sep="")