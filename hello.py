a=range(1,30000)
c=0
for i in a:
    if (i%3==0) and ('3' in str(i)):
        c=c+1
print(c)