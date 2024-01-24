sentence = "Python is Awesome"
sentence = sentence.split()
reversed =""
for x in sentence:
    reversed=reversed + x[::-1] + ' '
print(reversed)    
    