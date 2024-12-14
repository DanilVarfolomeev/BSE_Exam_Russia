q=int(input())
w=0
while q!=0:
    if q%4==0 or q%9==0:
        w+=1
    q=int(input())
print(w)
