status=input("Input your request:")
s1=0
t1=0
while status=="help":
    print('''    start...start the car
    stop...stop the car
    quit...to exit      ''')
    option=input("Enter your choice?")
    strt=False
    stp=False
    
    if option=="start" and strt==False:
        print("The car has started")
        if s1>0 :
         print("The car has already started")
        s1=s1+1

    elif option=="stop" and stp==False:
        print("The car has stopped")    
        if t1>0:
         print("The car has already started")
        t1=t1+1
    elif option=="quit":
        break    
else:
    print("Wakarimasen")    