dic={"0":"Zero","1":"One","2":"Two","3":"Three","4":"Four","5":"Five","6":"Six","7":"Seven","8":"Eight","9":"Nine"}
phone=input("Phone: ")
alp=""
for i in phone:
    alp=alp+dic.get(i,"!")+" "
    
print(alp)