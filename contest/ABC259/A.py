N,M,X,T,D=map(int,input().split())

if M>=X:
    print(T)

else:
    ans=T-X*D+M*D
    

    print(ans)
