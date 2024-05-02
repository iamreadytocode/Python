lis=[43,56,101,34,34,94,67,43,34,76,94,81,94]
for num in lis:
    a=lis.count(num)
    if a>1:
        lis.remove(num)
print(lis)