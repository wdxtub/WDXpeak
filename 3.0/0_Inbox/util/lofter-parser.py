#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, codecs
import xml.etree.cElementTree as ET

# 使用minidom解析器打开 XML 文档
tree = ET.ElementTree(file='Import/xmlexport.do')
root = tree.getroot()
print root

# 图片的另外处理

for child in root:
    if child.tag == 'PostItem':
        title = ''
        time = ''
        tag = ''
        content = ''

        for record in child:
            if record.tag == 'title':
                title = record.text
            elif record.tag == 'publishTime':
                time = record.text
            elif record.tag == 'tag':
                tag = record.text
            elif record.tag == 'content':
                content = record.text

        if title != None:
            print title
            print time
            print tag
            print content
