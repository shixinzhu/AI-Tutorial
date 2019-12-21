 def func01(aaa):
...    for i in range(1,aaa):
...        for j in range(1,aaa):
...            if j==i:
...                print (str(j)+"*"+str(i)+"="+str(i*j)+" ")
...            if j<i:
...                print (str(j)+"*"+str(i)+"="+str(i*j)+" ", end='')
