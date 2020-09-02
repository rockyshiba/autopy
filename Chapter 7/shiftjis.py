import codecs

with codecs.open('shiftjis.txt',mode='r',encoding='shiftjis') as file:
    lines = file.read()

with codecs.open('utf8.txt',mode='w',encoding='utf8') as file:
    for line in lines:
        file.write(line)