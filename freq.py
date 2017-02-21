f = open('text.txt', 'rU')
text = f.read()
dct = {}
for char in text:
    if char in dct:
        dct[char] += 1
    else:
        dct[char] = 1

def ret_2(tuple):
    return tuple[1]

result = sorted(dct.items(), reverse=True, key=ret_2)

''' printing sorted list
for k, v in result:
    print "%s : %d" % (k, v)
'''

word = [x[0] for x in result]
print "".join(word[:word.index('_')])
