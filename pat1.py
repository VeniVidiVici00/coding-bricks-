num = int(input())

space = "  "
box = "  "
rev_num = ""
num1 = ""
fi = []
ans = []
for t in range((num+1)//2):
    num1=[]
    for i in range(1,t+2):
        num1.append(str(i))
    fi = list(num1)
    fi.reverse()
    if not t:
        num1 =[]
        
    ans.append(space*(num-t*2)+" ".join(fi)+ box*(2*t-1)+ " ".join(num1))

for i in ans:
    print(i)
for i in range(2,len(ans)+1):
    print(ans[-i])


