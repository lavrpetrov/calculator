s=[]
a=0

def drop(s):
    s=s[1:]
    return s

def push(s,x):
    return s.insert(0,x)

def rotate(s):
    b=s[len(s)-1]
    s=s[0:len(s)-1]
    push(s,b)
    return s

def pull(s):
    global a
    a=int(s[0])
    return drop(s)

def sloz(s):
    global a
    s=pull(s)
    b=int(s[0])
    s[0]=a+b
    return s


def razn(s):
    global a
    s=pull(s)
    b=int(s[0])
    s[0]=a-b
    return s

def ymn(s):
    global a
    s=pull(s)
    b=int(s[0])
    s[0]=a*b
    return s

def delen(s):
    global a
    s=pull(s)
    b=int(s[0])
    s[0]=a//b
    return s

ex=list(input().split(' '))

signsstek=[]
finalstek=[]

for i in range(len(ex)):
    if ex[i].isdigit():
        finalstek.append(ex[i])
    elif ex[i] == ')':
        j=len(signsstek)-1
        while signsstek[j] !='(':
            finalstek.append(signsstek[j])
            signsstek.pop()
            j -=1
    elif ex[i]=="+" or ex[i]=="-":
        while len(signsstek)>0 and signsstek[len(signsstek)-1]!='(':
            finalstek.append(signsstek[len(signsstek)-1])
            signsstek.pop()
        signsstek.append(ex[i])
    elif ex[i]=="*" or ex[i]=="/":
        j=len(signsstek)-1
        while j>0 and (signsstek[j]=="*" or signsstek[j]=="/"):
            finalstek.append(signsstek[j])
            signsstek.pop()
            j -=1
        signsstek.append(ex[i])
    elif ex[i]=='(':
        signsstek.append(ex[i])
while len(signsstek)>0:
    finalstek.append(signsstek[len(signsstek)-1])
    signsstek.pop()

d=" ".join(finalstek)

for i in range(len(d)):
    if d[i].isdigit():
        push(s,int(d[i]))
    else:
        if d[i]=='+':
            s=sloz(s)
        elif d[i]=='-':
            s=razn(s)
        elif d[i]=='*':
            s=ymn(s)
        elif d[i]=='/':
            s=delen(s)
print(s[0])
