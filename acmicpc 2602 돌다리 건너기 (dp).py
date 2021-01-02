magic=input()
devil=input()
angel=input()

dp=[[[0]*2 for _ in range(len(angel)+1)] for _ in range(len(magic)+1)]


for i in range(len(angel)+1):
    dp[0][i][0]=1
    dp[0][i][1]=1

n=len(magic)
k=len(angel)

for i in range(1,n+1):
    for j in range(1,k+1):
        if magic[i-1]==angel[j-1]:
            dp[i][j][0]+=dp[i-1][j-1][1]
        if magic[i-1]==devil[j-1]:
            dp[i][j][1]=dp[i-1][j-1][0]

        dp[i][j][0]+=dp[i][j-1][0]
        dp[i][j][1]+=dp[i][j-1][1]

res=dp[n][k][0]+dp[n][k][1]
print(res)