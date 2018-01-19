f = open('firstnames.txt','r+')
names = f.read()
f.close()
names = names.split(" ")
print names