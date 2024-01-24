ascii_dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
new={}
for key in ascii_dict:
    new[ascii_dict[key]]=key
print(new) 