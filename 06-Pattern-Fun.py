row_count = int(input("Enter number:"))
i=1
l =row_count
while (i <= row_count):
    for k in range(0,l):
       print(i," ",end="")
    i+=1
    l-=1
    print()