price=1000000
good_credit=False
dp=0
if good_credit==True:
    dp=price*0.1
elif good_credit==False:
    dp=price*0.2

print("The down payment is ",dp)