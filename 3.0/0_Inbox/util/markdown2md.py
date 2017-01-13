import os

files = os.listdir('.')
for f in files:
    print f
    farr = f.split('.')
    if farr[1] == '.markdown':
        #print f
        os.rename(f, farr[0]+'.md')

print 'done'
