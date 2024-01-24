sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
print(sample_list)
reccuring_list = []
for i in range(len(sample_list)):
    for j in range(i + 1, len(sample_list)):
        if sample_list[i] == sample_list[j]:
            reccuring_list.append(sample_list[i])
print(reccuring_list) 