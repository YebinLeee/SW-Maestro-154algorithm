#10845 큐
import sys
from collections import deque
n = int(input())
q = deque([])
for i in range(n):
    cm = list(sys.stdin.readline().split())
    if cm[0] == "push":
        q.append(cm[1])
    elif cm[0] == "pop":
        if len(q)!=0:
            print(q.popleft())
        else:
            print("-1")
    elif cm[0] == "size":
        print(len(q))
    elif cm[0] == "empty":
        if len(q) == 0:
            print("1")
        else :
            print("0")
    elif cm[0]=="front":
        if len(q)==0:
            print("-1")
        else:
            print(q[0])
    elif cm[0]=="back":
        if len(q)==0:
            print("-1")
        else:
            print(q[-1])
        
