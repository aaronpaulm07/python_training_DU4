
number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(id(number_list))
print(number_list)
length = len(number_list)
i=0
while (i<length):
    if (number_list[i]>50):
        del number_list[i]
        length-=1
    else:
        i+=1
print(id(number_list))
print(number_list)
    