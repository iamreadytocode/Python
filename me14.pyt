def findmax(mylist):
    maxno=mylist[0]
    for num in mylist:
        if num>maxno:
            maxno=num              
    return maxno    
    

mylist=[1,3,5,67,12,56,8,9]  
print("The max number is ",findmax(mylist))  