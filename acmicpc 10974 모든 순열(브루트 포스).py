def dfs(cnt):
    if cnt==n:
        for num in nums:
            print(num, end=' ')
        print()
        return

    for i in range(1,n+1):
        if visited[i]==False:
            visited[i]=True
            nums.append(i)
            dfs(cnt+1)
            nums.pop()
            visited[i]=False

n=int(input())
nums=[]
visited=[False]*(n+1)
dfs(0)
