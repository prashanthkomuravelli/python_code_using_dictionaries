def orangecap(d):
    oc={}
    (player,score)=("",0)
    for k1 in d.keys():
        for k2 in d[k1].keys():
            if(k2 in list(oc.keys())):
               oc[k2]=oc[k2]+d[k1][k2]
            else:
               oc[k2]=d[k1][k2]
    for k3 in oc.keys():
        if oc[k3]>score :
               (player,score)=(k3,oc[k3])
    return (player,score)    
def addpoly(p1,p2):
    list=[]
    for i in p1:
        k=availble(i[1],p2)
        list.append((k[0]+i[0],i[1]))
    for j in p2:
        list.append(j)
    removezero(list)
    list.reverse()
    return(list)
def multpoly(p1,p2):
    list=[]
    for i in p1:
        for j in p2:
            
            k=availble(i[1]+j[1],list)
            list.append((k[0]+i[0]*j[0],k[1]+i[1]+j[1]))
    removezero(list)
    return list
def availble(exponent,list1):
    for k in list1:
        if(k[1]==exponent):
            list1.remove(k)
            return k
    return(0,0)
def removezero(list1):
    for m in list1:
        if m[0]==0:
            list1.remove(m)
            removezero(list1)
# Hidden code below

import ast

def todict(inp):
    inp = ast.literal_eval(inp)
    return (inp)

def topairoflists(inp):
    inp = "["+inp+"]"
    inp = ast.literal_eval(inp)
    return (inp[0],inp[1])

def tostring(s):
  lquote = s.find('"')
  rquote = s.rfind('"')
  return(s[lquote+1:rquote])

def tolist(s):
  lbrack = s.find('[')
  rbrack = s.rfind(']')
  slist = s[lbrack+1:rbrack].split(',')
  if slist == ['']:
    slist = []
  else:
    for i in range(0,len(slist)):
      slist[i] = int(slist[i])
  return(slist)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "orangecap":
   arg = todict(farg)
   print(orangecap(arg),end="")
elif fname == "addpoly":
   (arg1,arg2) = topairoflists(farg)
   print(addpoly(arg1,arg2),end="")
elif fname == "multpoly":
   (arg1,arg2) = topairoflists(farg)
   print(multpoly(arg1,arg2),end="")
else:
   print("Function", fname, "unknown")
    
