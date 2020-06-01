import os
k=0
a=0
b=1
s=0
maxs=0
filename="zxc.txt"
def File(filename):
    try:
        if(os.stat(filename).st_size>=0):
            f=open(filename,"r")
            check=f.read()
            if(len(check)==0):
                print("Pustoi fail")
                f.close()
                raise Exception("Pustoi fail iskluch.")
            f.close()
            return 0
    except Exception:
        print("Oshibka")
        return 1
err=File(filename)
if err!=0:
    exit()
with open("zxc.txt") as f:
    for t in f:
        l=len(t)
        print("t=",t)
        for i in t.split(' '):
            if k==0:
                k=k+1
                a=int(i)
                s=s+a
            else:
                a=int(i)
                s=s+a
                if s>maxs:
                    maxs=s
                if s<0:
                    s=0
print("maxs=",maxs)
                
