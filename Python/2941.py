text = input()
cnt = 0

li = ['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in li:
    if i in text:
        text = text.replace(i,"1")
print(len(text))
