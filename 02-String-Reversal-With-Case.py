sentence = "Python is Awesome"
sentence = sentence.split()
reversed =""
for x in sentence:
    if x[0].isupper():
       x = x[0:-1].lower() + x[-1].upper()
    reversed=reversed + x[::-1] + ' '
print(reversed)    