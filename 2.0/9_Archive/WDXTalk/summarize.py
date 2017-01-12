# -*- coding: utf-8 -*-
import os, sys, codecs, json

# Must have a readme.md file for each folder
# 博客具体格式需要规整规定一下

reload(sys)
sys.setdefaultencoding('utf-8')

summary = codecs.open('./SUMMARY.md', 'w', 'utf-8')
summary.write('# Summary\n')
summary.write('\nThis is the summary of my book.\n\n')

folders = os.listdir('.')
for fo in folders:
    if fo[0] == '.': continue
    if fo[-3:] == '.py' or fo[-3:] == '.md': continue

    if os.path.isdir(fo):
        summary.write('* [' + fo + '](' + fo + '/README.md)\n')

        posts = os.listdir(fo)

        for p in posts:
            if p[0] == '.': continue
            if p == 'README.md' : continue
            path = os.path.join(fo, p)
            if os.path.isfile(path):
                print path
                h = codecs.open(path, 'r', 'utf-8')
                text = h.readline()
                summary.write('    * [' + text[2:len(text)-1] + '](' + path + ')\n')

print 'done'
