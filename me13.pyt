def rd(mylist):
    flist=[]
    for item in mylist:
        if item not in flist:
            flist.append(item)
    return flist

newlist=[1,3,3,4,5,1,4]               
print(rd(newlist))